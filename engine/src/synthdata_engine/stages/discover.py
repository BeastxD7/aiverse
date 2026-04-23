"""Stage 1 — Axes discovery.

Given a domain brief + dataset purpose + schema + speaker scope, ask the LLM
to name the 3-6 dimensions that naturally vary in this domain. Speaker scope
is a hard constraint: axes must never include out-of-scope user types.
"""

from __future__ import annotations

import json
import time

from ..config import JobConfig
from ..debug import DebugWriter, _fence, _json
from ..providers.base import LLMProvider

_SYSTEM = """You design synthetic-data generation plans for NLP fine-tuning.
Output strict JSON only."""

_USER_TEMPLATE = """I'm generating a dataset for this domain:

PROJECT: {project_name}

DOMAIN BRIEF:
{domain_brief}

DATASET PURPOSE:
{dataset_brief}

{speaker_block}

SCHEMA FIELDS (with per-value semantics where declared):
{schema_hint}

Identify the 3 to 6 independent DIMENSIONS (called "axes") that naturally vary in
this domain. For each axis, list 3 to 8 representative VALUES the axis can take.

HARD CONSTRAINTS:
- Good axes are orthogonal — changing one shouldn't force changing another.
- If you use a persona/user/speaker axis, draw ONLY from the SPEAKERS IN SCOPE above.
  Never include any out-of-scope speaker as a value, and never invent speaker
  types beyond what is listed.
- Do NOT use the dataset's output label as an axis unless it's a genuinely
  controllable input dimension (when in doubt, skip it).

Return JSON of the form:
{{
  "axes": {{
    "<axis_name>": ["val1", "val2", ...],
    ...
  }}
}}

No prose, no explanation — JSON only."""


def _rich_schema_hint(cfg: JobConfig) -> str:
    """Schema hint that includes enum value semantics when the user provided them."""
    lines: list[str] = []
    for f in cfg.dataset_schema.fields:
        if f.type == "enum":
            lines.append(f'- {f.name} (enum): {f.description or "one of:"}')
            for ev in f.values or []:
                if ev.description:
                    lines.append(f"    * {ev.name} — {ev.description}")
                else:
                    lines.append(f"    * {ev.name}")
        else:
            hint = f"{f.type}"
            if f.type == "float" and (f.min is not None or f.max is not None):
                hint += f" in [{f.min}, {f.max}]"
            desc = f" — {f.description}" if f.description else ""
            lines.append(f"- {f.name} ({hint}){desc}")
    return "\n".join(lines)


async def discover_axes(
    cfg: JobConfig,
    provider: LLMProvider,
    *,
    debug: DebugWriter | None = None,
) -> dict[str, list[str]]:
    speaker_block = cfg.project.speakers.as_prompt_block()
    user = _USER_TEMPLATE.format(
        project_name=cfg.project.name,
        domain_brief=cfg.project.domain_brief,
        dataset_brief=cfg.dataset.brief,
        speaker_block=speaker_block or "SPEAKERS: (not constrained)",
        schema_hint=_rich_schema_hint(cfg),
    )
    t0 = time.monotonic()
    resp = await provider.generate_json(_SYSTEM, user, max_retries=3)
    elapsed = time.monotonic() - t0

    if resp.outcome != "success" or not isinstance(resp.parsed, dict):
        if debug:
            debug.write("01_axes_discovery.md", _axes_fail_doc(_SYSTEM, user, resp, elapsed))
        raise RuntimeError(f"axes discovery failed: {resp.outcome} — {resp.error}")

    axes_raw = resp.parsed.get("axes")
    if not isinstance(axes_raw, dict) or not axes_raw:
        raise RuntimeError(f"axes response missing 'axes' dict: {resp.parsed}")

    axes: dict[str, list[str]] = {}
    for name, vals in axes_raw.items():
        if not isinstance(vals, list) or len(vals) < 2:
            continue
        axes[str(name)] = [str(v) for v in vals if isinstance(v, (str, int, float))]

    if len(axes) < 2:
        raise RuntimeError(f"too few usable axes returned: {axes}")

    # Reconcile: if an axis name matches an enum field, force its values to the
    # enum values so combinations never pin an impossible label.
    for f in cfg.dataset_schema.fields:
        if f.type == "enum" and f.name in axes and f.values:
            axes[f.name] = f.value_names()

    if debug:
        debug.write("01_axes_discovery.md", _axes_doc(_SYSTEM, user, resp, axes, elapsed))
    return axes


def _axes_doc(system: str, user: str, resp, axes: dict, elapsed: float) -> str:
    return f"""# Stage 1 — Axes Discovery

## System Prompt
{_fence(system)}

## User Prompt
{_fence(user)}

## Raw LLM Response
{_fence(resp.raw_text)}

## Parsed Axes
{_fence(_json(axes), "json")}

## Stats
- Outcome: {resp.outcome}
- Attempts: {resp.attempts}
- Duration: {elapsed:.1f}s
"""


def _axes_fail_doc(system: str, user: str, resp, elapsed: float) -> str:
    return f"""# Stage 1 — Axes Discovery — FAILED

## System Prompt
{_fence(system)}

## User Prompt
{_fence(user)}

## Raw LLM Response
{_fence(resp.raw_text)}

## Error
- Outcome: {resp.outcome}
- Error: {resp.error}
- Attempts: {resp.attempts}
- Duration: {elapsed:.1f}s
"""
