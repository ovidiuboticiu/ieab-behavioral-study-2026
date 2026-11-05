"""IEAB v0.4.4 behavioral runner (unchanged logic from v0.4.3) — simple, append-only, first complete response wins.

Usage (Windows PowerShell, from this folder):
    py -3 behavioral_runner.py plan   --model qwen3.5-4b
    py -3 behavioral_runner.py run    --model qwen3.5-4b --limit 10 --send
    py -3 behavioral_runner.py status --model qwen3.5-4b
    py -3 behavioral_runner.py export --model qwen3.5-4b

Rules (see research/DESIGN_IEAB_v0.4.3_AMENDMENT_DRAFT.md and DESIGN_IEAB_v0.4.4_PREREGISTRATION.md):
- every request and every response is appended to ONE JSONL log per model;
- the result of a key is the FIRST complete response recorded for it (HTTP 200,
  correct model); later duplicates are kept and reported, never used;
- a key whose request got no complete response may be sent again on resume;
- an individually invalid response is final for its key (no retry);
- wrong model / non-200 / transport error / changed input package -> STOP;
- choices are never printed while the schedule is not exhausted.

Nothing is sent without the explicit --send flag. Importing this module sends nothing.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import socket
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from behavioral_inputs import BUNDLE, MODEL_IDS, SCHEDULE, SOURCES, bind_schedule, request_bytes

VERSION = "IEAB_v0.4.4"
URL = "http://127.0.0.1:1234/v1/chat/completions"
TIMEOUT_SECONDS = 300  # v0.4.4: technical ceiling only (larger models on CPU); a timeout yields no data, key is resent on resume
HERE = Path(__file__).resolve().parent
FINAL_VERDICTS = ("VALID", "INVALID")


class Stop(Exception):
    """Run must stop; message is a diagnostic code plus detail."""


# ---------------------------------------------------------------- package identity

def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def package_fingerprint(bundle: Path = BUNDLE) -> dict:
    """Hashes of everything that defines what is sent. Must not change within one log."""
    files = {name: _sha256_file(bundle / name) for name, _ in SOURCES}
    files[SCHEDULE] = _sha256_file(bundle / SCHEDULE)
    files["behavioral_inputs.py"] = _sha256_file(HERE / "behavioral_inputs.py")
    files["behavioral_runner.py"] = _sha256_file(Path(__file__).resolve())
    return files


def default_log(model: str) -> Path:
    base = os.environ.get("LOCALAPPDATA")
    root = Path(base) / "IEAB-Restart" if base else Path.home() / ".ieab-restart"
    return root / f"behavioral-{VERSION}-{model}.jsonl"


# ---------------------------------------------------------------- strict parsing

def _unique(pairs):
    obj = {}
    for k, v in pairs:
        if k in obj:
            raise ValueError("duplicate key")
        obj[k] = v
    return obj


def classify(model: str, status: int, raw: bytes) -> tuple[str, str, str | None]:
    """Return (verdict, reason, chosen_claim).

    SYSTEMIC = not a scientific observation of the approved configuration (stop the run).
    INVALID  = complete response from the right model that breaks the response contract.
    VALID    = exactly {"chosen_claim": "CLAIM_A" | "CLAIM_B"}.
    """
    if status != 200:
        return "SYSTEMIC", f"HTTP_{status}", None
    try:
        env = json.loads(raw.decode("utf-8"), object_pairs_hook=_unique)
    except (ValueError, UnicodeError):
        return "SYSTEMIC", "ENVELOPE_NOT_JSON", None
    if type(env) is not dict or env.get("model") != model:
        return "SYSTEMIC", "RESPONSE_MODEL_MISMATCH", None
    choices = env.get("choices")
    if type(choices) is not list or len(choices) != 1 or type(choices[0]) is not dict:
        return "INVALID", "CHOICES_NOT_EXACTLY_ONE", None
    choice = choices[0]
    message = choice.get("message")
    if type(message) is not dict:
        return "INVALID", "MESSAGE_MISSING", None
    for field in ("reasoning_content", "reasoning"):
        if message.get(field) not in (None, "", [], {}):
            return "INVALID", "NONEMPTY_REASONING", None
    if choice.get("finish_reason") != "stop":
        return "INVALID", f"FINISH_REASON_{choice.get('finish_reason')}", None
    content = message.get("content")
    if type(content) is not str:
        return "INVALID", "CONTENT_NOT_TEXT", None
    try:
        obj = json.loads(content.strip(), object_pairs_hook=_unique)
    except ValueError:
        return "INVALID", "CONTENT_NOT_SINGLE_JSON_OBJECT", None
    if type(obj) is not dict or set(obj) != {"chosen_claim"}:
        return "INVALID", "WRONG_FIELDS", None
    if obj["chosen_claim"] not in ("CLAIM_A", "CLAIM_B"):
        return "INVALID", "CHOICE_NOT_IN_ENUM", None
    return "VALID", "OK", obj["chosen_claim"]


# ---------------------------------------------------------------- the log

class Log:
    def __init__(self, path: Path):
        self.path = path
        self.events: list[dict] = []
        self._needs_newline = False
        if path.exists():
            lines = path.read_bytes().split(b"\n")
            for i, line in enumerate(lines):
                if not line.strip():
                    continue
                try:
                    self.events.append(json.loads(line.decode("utf-8")))
                    continue
                except (ValueError, UnicodeError):
                    pass
                # A fragment is allowed only as the unterminated last line (crash mid-write),
                # or when the next line is the marker written when we recovered from it.
                if i == len(lines) - 1:
                    self._needs_newline = True
                    continue
                nxt = lines[i + 1] if i + 1 < len(lines) else b""
                try:
                    marker = json.loads(nxt.decode("utf-8")).get("event")
                except (ValueError, UnicodeError, AttributeError):
                    marker = None
                if marker != "TRUNCATED_PREVIOUS_LINE":
                    raise Stop(f"LOG_CORRUPT_LINE: {path} line {i + 1}")

    def append(self, event: dict) -> None:
        event = {"t": time.strftime("%Y-%m-%dT%H:%M:%S%z"), **event}
        line = json.dumps(event, ensure_ascii=False, separators=(",", ":"))
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.path, "a", encoding="utf-8", newline="\n") as f:
            if self._needs_newline:  # terminate the crash fragment and mark it, never delete it
                f.write("\n" + json.dumps({"event": "TRUNCATED_PREVIOUS_LINE"}) + "\n")
                self._needs_newline = False
            f.write(line + "\n")
            f.flush()
            os.fsync(f.fileno())
        self.events.append(event)

    def first_results(self) -> dict[str, dict]:
        """key -> first complete (VALID/INVALID) response event."""
        out: dict[str, dict] = {}
        for e in self.events:
            if e.get("event") == "RESPONSE" and e.get("verdict") in FINAL_VERDICTS:
                out.setdefault(e["key"], e)
        return out

    def fingerprint(self) -> dict | None:
        for e in self.events:
            if e.get("event") == "RUN_START":
                return e["package"]
        return None


class Lock:
    """OS lock on <log>.lock; released automatically if the process dies."""

    def __init__(self, log_path: Path):
        self.path = log_path.with_suffix(log_path.suffix + ".lock")
        self.fh = None

    def __enter__(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.fh = open(self.path, "a+")
        try:
            if os.name == "nt":
                import msvcrt
                self.fh.seek(0)
                msvcrt.locking(self.fh.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(self.fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            self.fh.close()
            raise Stop(f"ANOTHER_RUNNER_IS_USING_THIS_LOG: {self.path}") from exc
        return self

    def __exit__(self, *exc):
        self.fh.close()  # closing releases the lock on both platforms


# ---------------------------------------------------------------- transport

class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def http_post(body: bytes) -> tuple[int, bytes]:
    req = urllib.request.Request(URL, data=body, method="POST",
                                 headers={"Content-Type": "application/json"})
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), _NoRedirect())
    try:
        with opener.open(req, timeout=TIMEOUT_SECONDS) as r:
            return int(r.status), r.read()
    except urllib.error.HTTPError as exc:
        return int(exc.code), exc.read()


# ---------------------------------------------------------------- commands

def summarize(log: Log, schedule) -> dict:
    results = log.first_results()
    blocks = {t.trajectory_id: t.block for t in schedule}
    requests: dict[str, int] = {}
    for e in log.events:
        if e.get("event") == "REQUEST":
            requests[e["key"]] = requests.get(e["key"], 0) + 1
    invalid_reasons: dict[str, int] = {}
    per_block = {b: {"planned": 0, "valid": 0, "invalid": 0} for b in ("CORE", "DEPENDENT", "A1", "A2")}
    for t in schedule:
        per_block[t.block]["planned"] += 1
        r = results.get(t.trajectory_id)
        if r:
            per_block[t.block]["valid" if r["verdict"] == "VALID" else "invalid"] += 1
            if r["verdict"] == "INVALID":
                invalid_reasons[r["reason"]] = invalid_reasons.get(r["reason"], 0) + 1
    extra = sorted(set(results) - set(blocks))
    if extra:
        raise Stop(f"LOG_HAS_KEYS_OUTSIDE_SCHEDULE: {extra[:3]}")
    finalized = len(results)
    return {
        "planned": len(schedule),
        "finalized": finalized,
        "valid": sum(1 for r in results.values() if r["verdict"] == "VALID"),
        "invalid": sum(1 for r in results.values() if r["verdict"] == "INVALID"),
        "remaining": len(schedule) - finalized,
        "keys_sent_more_than_once": sum(1 for n in requests.values() if n > 1),
        "systemic_responses": sum(1 for e in log.events
                                  if e.get("event") == "RESPONSE" and e.get("verdict") == "SYSTEMIC"),
        "transport_errors": sum(1 for e in log.events if e.get("event") == "TRANSPORT_ERROR"),
        "invalid_reasons": invalid_reasons,
        "per_block": per_block,
        "status": ("COMPLETE_VALID_MAP" if finalized == len(schedule) and not invalid_reasons
                   else "SCHEDULE_EXHAUSTED_PARTIAL_COVERAGE" if finalized == len(schedule)
                   else "IN_PROGRESS"),
    }


def run(model: str, log_path: Path, *, send: bool, limit: int | None,
        transport=http_post, out=print) -> int:
    if model not in MODEL_IDS:
        raise Stop(f"UNKNOWN_MODEL: {model}")
    schedule = bind_schedule()
    package = package_fingerprint()
    out(f"Versiune: {VERSION}   Model: {model}")
    out(f"Jurnal (fișierul cu rezultate): {log_path.resolve()}")
    out(f"Endpoint: {URL}")
    with Lock(log_path):
        log = Log(log_path)
        previous = log.fingerprint()
        if previous is not None and previous != package:
            changed = sorted(k for k in set(previous) | set(package) if previous.get(k) != package.get(k))
            raise Stop(f"INPUT_PACKAGE_CHANGED_SINCE_FIRST_RUN: {changed}")
        done = log.first_results()
        todo = [t for t in schedule if t.trajectory_id not in done]
        out(f"Chei finalizate: {len(done)}/360   Rămase: {len(todo)}")
        if not todo:
            out("Programul este epuizat. Nimic de trimis.")
            return 0
        if not send:
            out(f"PLAN ONLY — nu s-a trimis nimic. Următoarea cheie: poziția {todo[0].position}.")
            out("Pentru trimitere adaugă --send (și opțional --limit N).")
            return 0
        log.append({"event": "RUN_START", "version": VERSION, "model": model, "url": URL,
                    "package": package, "pid": os.getpid(), "host": socket.gethostname(),
                    "limit": limit})
        out("Alegerile modelului NU sunt afișate în timpul rulării.")
        sent = 0
        for t in todo:
            if limit is not None and sent >= limit:
                out(f"Limita de {limit} cereri atinsă. Oprire curată; reluarea continuă de aici.")
                break
            body = request_bytes(model, t)
            log.append({"event": "REQUEST", "key": t.trajectory_id, "position": t.position,
                        "request_sha256": hashlib.sha256(body).hexdigest()})
            sent += 1
            start = time.monotonic()
            try:
                status, raw = transport(body)
            except Exception as exc:  # noqa: BLE001 — every transport failure stops the run
                log.append({"event": "TRANSPORT_ERROR", "key": t.trajectory_id,
                            "error": f"{type(exc).__name__}: {exc}"})
                raise Stop(f"TRANSPORT_ERROR at position {t.position}: {type(exc).__name__}: {exc}. "
                           "Cheia poate fi retrimisă la reluare (regula v0.4.3).") from exc
            verdict, reason, chosen = classify(model, status, raw)
            event = {"event": "RESPONSE", "key": t.trajectory_id, "position": t.position,
                     "http_status": status, "raw_sha256": hashlib.sha256(raw).hexdigest(),
                     "elapsed_s": round(time.monotonic() - start, 3),
                     "verdict": verdict, "reason": reason, "chosen_claim": chosen}
            try:
                event["raw_text"] = raw.decode("utf-8")
            except UnicodeError:
                event["raw_b64"] = base64.b64encode(raw).decode("ascii")
            log.append(event)
            out(f"[{t.position:3d}/360] {verdict}" + ("" if verdict == "VALID" else f" ({reason})"))
            if verdict == "SYSTEMIC":
                raise Stop(f"SYSTEMIC_RESPONSE at position {t.position}: {reason}. "
                           "Verifică modelul încărcat / serverul, apoi reia.")
        s = summarize(log, schedule)
        out(f"Rezumat: finalizate {s['finalized']}/360, valide {s['valid']}, "
            f"invalide {s['invalid']}, stare {s['status']}")
        return 0


def status(model: str, log_path: Path, out=print) -> int:
    schedule = bind_schedule()
    out(f"Jurnal: {log_path.resolve()}")
    if not log_path.exists():
        out("Jurnalul nu există încă (nicio cerere trimisă).")
        return 0
    s = summarize(Log(log_path), schedule)
    out(json.dumps(s, ensure_ascii=False, indent=2))  # counts only, never choices
    return 0


def export(model: str, log_path: Path, dest: Path, out=print) -> int:
    schedule = bind_schedule()
    log = Log(log_path)
    s = summarize(log, schedule)
    if s["remaining"]:
        raise Stop(f"SCHEDULE_NOT_EXHAUSTED: {s['remaining']} chei rămase; alegerile rămân ascunse.")
    results = log.first_results()
    rows = [{"position": t.position, "trajectory_id": t.trajectory_id, "block": t.block,
             "verdict": results[t.trajectory_id]["verdict"],
             "reason": results[t.trajectory_id]["reason"],
             "chosen_claim": results[t.trajectory_id]["chosen_claim"]} for t in schedule]
    dest.write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")
    out(f"Exportat {len(rows)} rânduri în {dest.resolve()} (stare {s['status']}).")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="IEAB v0.4.4 behavioral runner")
    p.add_argument("command", choices=["plan", "run", "status", "export"])
    p.add_argument("--model", required=True, choices=sorted(MODEL_IDS))
    p.add_argument("--log", type=Path, help="cale jurnal (implicit în %%LOCALAPPDATA%%\\IEAB-Restart)")
    p.add_argument("--send", action="store_true", help="trimite efectiv cereri (doar cu run)")
    p.add_argument("--limit", type=int, help="număr maxim de cereri în această invocare")
    p.add_argument("--out", type=Path, help="fișier pentru export")
    a = p.parse_args(argv)
    for stream in (sys.stdout, sys.stderr):  # Romanian diacritics even when redirected on Windows
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    log_path = a.log or default_log(a.model)
    try:
        if a.command == "plan":
            return run(a.model, log_path, send=False, limit=None)
        if a.command == "run":
            return run(a.model, log_path, send=a.send, limit=a.limit)
        if a.command == "status":
            return status(a.model, log_path)
        dest = a.out or log_path.with_name(log_path.stem + "-results.jsonl")
        return export(a.model, log_path, dest)
    except Stop as exc:
        print(f"STOP: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
