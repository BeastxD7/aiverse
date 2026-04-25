"""Stage 6 — MinHash LSH deduplication.

Catches near-duplicates (case / punctuation / whitespace variants) in near-linear
time. Preserves valuable paraphrases — we're not doing semantic dedup here.
"""

from __future__ import annotations

import re

from datasketch import MinHash, MinHashLSH

from ..debug import DebugWriter

_TOKEN_RE = re.compile(r"[a-z0-9]+")


def _tokens(text: str) -> set[str]:
    return set(_TOKEN_RE.findall(text.lower()))


def _resolve_path(row: dict, path: str) -> list[str]:
    """Resolve a dotted/array path to all matching string leaf values.

    Supports simple keys ("text"), dotted nesting ("metadata.source"),
    and array expansion ("spans[].text").
    """
    parts = path.replace("[]", "[*]").split(".")
    current: list = [row]
    for part in parts:
        if part.endswith("[*]"):
            key = part[:-3]
            next_level: list = []
            for node in current:
                if isinstance(node, dict):
                    val = node.get(key, [])
                    if isinstance(val, list):
                        next_level.extend(val)
            current = next_level
        else:
            next_level = []
            for node in current:
                if isinstance(node, dict) and part in node:
                    next_level.append(node[part])
            current = next_level
    return [str(v) for v in current if isinstance(v, str)]


def _primary_text(row: dict, text_fields: list[str]) -> str:
    """Concatenate the primary text fields for signature computation."""
    parts: list[str] = []
    for f in text_fields:
        if "." in f or "[]" in f:
            parts.extend(_resolve_path(row, f))
        else:
            val = row.get(f, "")
            if val:
                parts.append(str(val))
    return " ".join(p for p in parts if p)


def dedupe(
    samples: list[dict],
    *,
    text_fields: list[str],
    threshold: float = 0.85,
    num_perm: int = 128,
    debug: DebugWriter | None = None,
) -> tuple[list[dict], int]:
    """Return (unique_samples, duplicates_removed_count)."""
    if not samples:
        return [], 0

    lsh = MinHashLSH(threshold=threshold, num_perm=num_perm)
    unique: list[dict] = []
    removed_samples: list[str] = []

    for i, row in enumerate(samples):
        text = _primary_text(row, text_fields)
        if not text.strip():
            unique.append(row)
            continue

        toks = _tokens(text)
        if not toks:
            unique.append(row)
            continue

        mh = MinHash(num_perm=num_perm)
        for t in toks:
            mh.update(t.encode("utf-8"))

        if lsh.query(mh):
            removed_samples.append(text[:120])
            continue

        lsh.insert(str(i), mh)
        unique.append(row)

    removed = len(removed_samples)
    if debug:
        removed_lines = "\n".join(f"{i+1}. `{t}`" for i, t in enumerate(removed_samples)) or "_None removed_"
        debug.write(
            "07_dedup.md",
            f"# Stage 6 — Near-Duplicate Removal\n\n"
            f"## Settings\n"
            f"- Threshold: {threshold} (Jaccard similarity)\n"
            f"- MinHash permutations: {num_perm}\n"
            f"- Text fields checked: {text_fields}\n\n"
            f"## Result\n"
            f"- Input: {len(samples)} samples\n"
            f"- Removed: {removed} near-duplicates\n"
            f"- Kept: {len(unique)} samples\n\n"
            f"## Removed Sample Texts\n\n{removed_lines}\n",
        )

    return unique, removed


def pick_text_fields(schema) -> list[str]:
    """Use string fields for dedup; fall back to all fields if none.

    Skips enum fields since they collapse variety artificially.
    Walks nested object/array fields to find string leaves.
    """
    strings = schema.string_field_paths()
    if strings:
        return strings
    return [f.name for f in schema.fields]
