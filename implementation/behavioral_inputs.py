"""IEAB v0.4.2: read-only scientific inputs and pure API request construction.

No networking, no SQLite mutations, no model calls, and no CLI. The historical
360-key schedule and prompt files are *read*, not regenerated or reordered.
This module is NOT a behavioral runner and does not authorize a model send.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

BUNDLE = Path(__file__).resolve().parent / "dry_run_v0.4.1"
MODEL_IDS = frozenset({
    "qwen3.5-4b", "gemma-4-e4b-it", "ministral-3-8b-instruct-2512",
    # v0.4.4: same-family larger configurations (see DESIGN_IEAB_v0.4.4_PREREGISTRATION.md)
    "qwen3.5-9b", "gemma-4-12b-it",
})
SCHEDULE = "schedule_v0.4.1.jsonl"
SOURCES = (
    ("core_prompts_v0.4.1.jsonl", {"CORE": 240}),
    ("dependent_prompts_v0.4.1.jsonl", {"DEPENDENT": 96}),
    ("anchor_prompts_v0.4.1.jsonl", {"A1": 8, "A2": 16}),
)
SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "ieab_choice", "strict": True,
        "schema": {
            "type": "object",
            "properties": {"chosen_claim": {"type": "string", "enum": ["CLAIM_A", "CLAIM_B"]}},
            "required": ["chosen_claim"], "additionalProperties": False,
        },
    },
}


class InputError(ValueError):
    """Scientific package cannot be bound without changing it."""


@dataclass(frozen=True)
class Trajectory:
    position: int
    trajectory_id: str
    block: str
    prompt: str


def _jsonl(path: Path) -> list[dict]:
    """Reject duplicates, non-object lines, empty/truncated or absent files."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise InputError(f"SOURCE_NOT_READABLE: {path.name}") from exc
    if not lines:
        raise InputError(f"SOURCE_EMPTY: {path.name}")
    result = []
    for number, line in enumerate(lines, 1):
        def unique(pairs):
            obj = {}
            for k, v in pairs:
                if k in obj:
                    raise ValueError("duplicate field")
                obj[k] = v
            return obj
        try:
            obj = json.loads(line, object_pairs_hook=unique)
        except (ValueError, TypeError) as exc:
            raise InputError(f"BAD_JSONL: {path.name}:{number}") from exc
        if type(obj) is not dict:
            raise InputError(f"NOT_AN_OBJECT: {path.name}:{number}")
        result.append(obj)
    return result


def bind_schedule(bundle: Path = BUNDLE) -> tuple[Trajectory, ...]:
    """Return the existing, unaltered 360-key schedule with exact corresponding prompts."""
    by_id: dict[str, dict] = {}
    counts = {"CORE": 0, "DEPENDENT": 0, "A1": 0, "A2": 0}
    for filename, expected in SOURCES:
        rows = _jsonl(bundle / filename)
        if len(rows) != sum(expected.values()):
            raise InputError(f"WRONG_SOURCE_COUNT: {filename}")
        for row in rows:
            tid, block, prompt = row.get("trajectory_id"), row.get("block"), row.get("prompt")
            if type(tid) is not str or not tid or tid in by_id:
                raise InputError(f"DUPLICATE_OR_INVALID_ID: {filename}")
            if block not in expected or type(prompt) is not str or not prompt:
                raise InputError(f"WRONG_BLOCK_OR_EMPTY_PROMPT: {tid}")
            if row.get("prompt_char_count") != len(prompt):
                raise InputError(f"PROMPT_LENGTH_MISMATCH: {tid}")
            counts[block] += 1
            by_id[tid] = row
        if any(counts[k] != count for k, count in expected.items()):
            raise InputError(f"WRONG_BLOCK_COUNTS: {filename}")

    schedule = _jsonl(bundle / SCHEDULE)
    if len(schedule) != 360 or len(by_id) != 360:
        raise InputError("SCHEDULE_COUNT_NOT_360")
    ordered = []
    seen = set()
    for i, record in enumerate(schedule, 1):
        tid = record.get("trajectory_id")
        if record.get("schedule_index") != i or type(tid) is not str or tid not in by_id or tid in seen:
            raise InputError(f"INVALID_SCHEDULE_KEY_OR_ORDER: {i}")
        seen.add(tid)
        row = by_id[tid]
        ordered.append(Trajectory(i, tid, row["block"], row["prompt"]))
    if seen != set(by_id):
        raise InputError("SCHEDULE_DOES_NOT_MATCH_PROMPT_SET")
    return tuple(ordered)


def request_bytes(model_api_id: str, trajectory: Trajectory) -> bytes:
    """Pure OpenAI-compatible payload; TOP P is omitted as in all three IEAB presets.

    No runtime identity claims or authorization; the future runner must pin both.
    """
    if model_api_id not in MODEL_IDS:
        raise InputError("MODEL_NOT_IN_PRIMARY_CONFIGURATIONS")
    if not isinstance(trajectory, Trajectory) or not trajectory.prompt:
        raise InputError("INVALID_TRAJECTORY")
    request = {
        "model": model_api_id,
        "messages": [{"role": "user", "content": trajectory.prompt}],
        "temperature": 0,
        "top_k": 40,
        "seed": 42,
        "max_tokens": 64,
        "stream": False,
        "response_format": SCHEMA,
    }
    return json.dumps(request, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
