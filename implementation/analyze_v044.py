"""IEAB v0.4.4 prespecified analysis (P1-P5). Read-only; no network.

Usage:  py -3 analyze_v044.py <export.jsonl> [<export.jsonl> ...]
Each export is the 360-row file produced by `behavioral_runner.py export`.
Definitions and decision thresholds: research/DESIGN_IEAB_v0.4.4_PREREGISTRATION.md.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BUNDLE = Path(__file__).resolve().parent / "dry_run_v0.4.1"


def load_prompts() -> dict:
    meta = {}
    for name in ("core", "dependent", "anchor"):
        for line in (BUNDLE / f"{name}_prompts_v0.4.1.jsonl").read_text(encoding="utf-8").splitlines():
            d = json.loads(line)
            meta[d["trajectory_id"]] = d
    return meta


def classify_n2(rep: dict) -> str:
    if rep["0.60"] <= 4 and rep["0.65"] <= 4 and rep["0.70"] >= 12:
        return "FOLLOWS"
    if rep["0.60"] >= 8 and rep["0.65"] >= 8:
        return "NOT_FOLLOWS"
    return "INTERMEDIATE"


def classify_n3(rep: dict) -> str:
    if rep["0.60"] <= 4 and rep["0.65"] >= 12 and rep["0.70"] >= 12:
        return "FOLLOWS"
    if rep["0.60"] >= 8:
        return "NOT_FOLLOWS"
    return "INTERMEDIATE"


def analyze(export: Path, meta: dict) -> dict:
    rows = [json.loads(l) for l in export.read_text(encoding="utf-8").splitlines() if l.strip()]
    if len(rows) != 360 or len({r["trajectory_id"] for r in rows}) != 360:
        raise SystemExit(f"{export}: expected 360 unique rows")
    ch = {r["trajectory_id"]: (r["chosen_claim"] if r["verdict"] == "VALID" else None) for r in rows}

    def repeated(tid):
        c = ch[tid]
        return None if c is None else c == meta[tid]["assignment"]["repeated_label"]

    core = {t: d for t, d in meta.items() if d["block"] == "CORE"}
    out = {"file": export.name, "valid": sum(c is not None for c in ch.values())}
    for n, fn in ((2, classify_n2), (3, classify_n3)):
        rep = {r: 0 for r in ("0.60", "0.65", "0.70")}
        valid = {r: 0 for r in rep}
        for t, d in core.items():
            if d["n"] == n and repeated(t) is not None:
                valid[d["r"]] += 1
                rep[d["r"]] += repeated(t)
        out[f"P1_n{n}_repeated_of_16"] = rep
        out[f"P1_n{n}_valid"] = valid
        out[f"P1_n{n}_class"] = fn(rep) if all(v == 16 for v in valid.values()) else "NOT_EVALUABLE"
    for b in ("B1", "B3"):
        ok = tot = 0
        for t, d in core.items():
            if repeated(t) is None:
                continue
            tot += 1
            ok += ("REPEATED" if repeated(t) else "SINGLE_080") == d["rules"][b]
        out[f"P2_{b}"] = f"{ok}/{tot}"
    cats = {"normative_switch": 0, "reverse": 0, "same_repeated": 0, "same_single": 0, "missing": 0}
    for t, d in meta.items():
        if d["block"] != "DEPENDENT":
            continue
        i, dd = repeated("CORE" + t[3:]), repeated(t)
        if i is None or dd is None:
            cats["missing"] += 1
        elif i and not dd:
            cats["normative_switch"] += 1
        elif not i and dd:
            cats["reverse"] += 1
        else:
            cats["same_repeated" if i else "same_single"] += 1
    informative = cats["normative_switch"] + cats["same_repeated"]
    out["P3_M6"] = cats
    out["P3_informative_switch"] = f"{cats['normative_switch']}/{informative}"
    first_only = last_only = same = 0
    for t, d in core.items():
        if d["evidence_order"] != "COUNTER_FIRST":
            continue
        a, b = repeated(t), repeated(t.replace(":FIRST", ":LAST"))
        if a is None or b is None:
            continue
        if a == b:
            same += 1
        elif a:
            first_only += 1  # repeated chosen only when its block is presented LAST
        else:
            last_only += 1   # repeated chosen only when its block is presented FIRST
    out["P4_M5"] = {"same": same, "repeated_only_when_block_last": first_only,
                    "repeated_only_when_block_first": last_only}
    out["P4_direction"] = ("FAVOURS_FIRST" if last_only > first_only else
                           "FAVOURS_LAST" if first_only > last_only else "NONE")
    a2 = [t for t, d in meta.items() if d["block"] == "A2" and ch[t] is not None]
    out["P5_anchors"] = {
        "A1": f"{sum(ch[t] == meta[t]['normative']['choice'] for t, d in meta.items() if d['block'] == 'A1' and ch[t])}/8",
        "A2": f"{sum(ch[t] == meta[t]['normative']['choice'] for t in a2)}/16",
    }
    return out


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    meta = load_prompts()
    for p in argv:
        print(json.dumps(analyze(Path(p), meta), ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
