"""Stage 3 — Prompt composer + persona pool.

Persona pool: cached per project. Each generation call injects one random
persona, random seed IDs, per-enum-value descriptions as rules, and any
anti-seeds as explicit "DO NOT" examples.
"""

from __future__ import annotations

import json
import random
import time
from uuid import uuid4

from ..config import AntiSeed, JobConfig
from ..debug import DebugWriter, _fence, _json
from ..providers.base import LLMProvider
from ..schema import DatasetSchema
from .logic_filter import Combination

_PERSONA_SYSTEM = "You generate diverse writer personas. Output strict JSON only."

_PERSONA_USER = """Generate {n} distinct personas that could plausibly AUTHOR
messages in this domain. Each persona is a short description (12-25 words)
covering: role, context, writing style.

DOMAIN:
{domain}

DATASET PURPOSE:
{purpose}

{speaker_block}

HARD CONSTRAINTS:
- Every persona must represent an IN-SCOPE speaker (if scope is listed above).
- Never invent a persona for an OUT-OF-SCOPE speaker type.

Return JSON:
{{"personas": ["persona 1...", "persona 2...", ...]}}

JSON only."""


_GEN_SYSTEM = """You generate ONE realistic training example for an NLP dataset.
Output strict JSON matching the requested schema. No prose, no explanation."""

_DIVERSITY_DIRECTIVES = {
    "standard": "",
    "high": (
        "DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. "
        "Avoid the most obvious or generic expression. "
        "Vary sentence length, vocabulary, cultural context, or phrasing. "
        "Make this example as distinct as possible from a typical training sample.\n\n"
    ),
    "edge_cases": (
        "DIVERSITY DIRECTIVE: Generate an EDGE CASE or AMBIGUOUS example — "
        "something subtle, borderline, or easily mislabeled. "
        "The correct classification should require careful reading. "
        "Avoid clear-cut, obvious examples.\n\n"
    ),
}

_GEN_USER_TEMPLATE = """Generate ONE example matching this schema:

{schema_hint}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
{combo_lines}
- Speaker persona: {persona}
- Unique seed: {seed}

{speaker_block}{seed_block}{anti_seed_block}{diversity_block}HARD RULES:
{rule_lines}

Return JSON only — a single object matching the schema above."""


async def build_persona_pool(
    cfg: JobConfig,
    provider: LLMProvider,
    *,
    debug: DebugWriter | None = None,
) -> list[str]:
    speaker_block = cfg.project.speakers.as_prompt_block() or "SPEAKERS: (not constrained)"
    user = _PERSONA_USER.format(
        n=cfg.dataset.persona_pool_size,
        domain=cfg.project.domain_brief,
        purpose=cfg.dataset.brief,
        speaker_block=speaker_block,
    )
    t0 = time.monotonic()
    resp = await provider.generate_json(_PERSONA_SYSTEM, user, max_retries=3)
    elapsed = time.monotonic() - t0

    fallback = [f"In-scope practitioner #{i}, writes naturally" for i in range(20)]
    if resp.outcome != "success" or not isinstance(resp.parsed, dict):
        personas = fallback
    else:
        raw = resp.parsed.get("personas")
        personas = [str(p) for p in raw if isinstance(p, str) and p.strip()] if isinstance(raw, list) and raw else fallback

    if debug:
        numbered = "\n".join(f"{i+1}. {p}" for i, p in enumerate(personas))
        debug.write(
            "04_personas.md",
            f"# Stage 3 — Persona Pool\n\n"
            f"## System Prompt\n{_fence(_PERSONA_SYSTEM)}\n\n"
            f"## User Prompt\n{_fence(user)}\n\n"
            f"## Raw LLM Response\n{_fence(resp.raw_text)}\n\n"
            f"## Generated Personas ({len(personas)})\n\n{numbered}\n\n"
            f"## Stats\n- Outcome: {resp.outcome}\n- Duration: {elapsed:.1f}s\n",
        )

    return personas


def compose_prompt(
    combination: Combination,
    *,
    schema: DatasetSchema,
    seeds: list[dict],
    anti_seeds: list[AntiSeed],
    personas: list[str],
    speaker_block: str,
    rng: random.Random,
    diversity: str = "standard",
) -> tuple[str, str]:
    """Return (system, user) for a single generation call."""
    combo_lines = "\n".join(f"- {k}: {v}" for k, v in combination.items())
    persona = rng.choice(personas)
    seed = uuid4().hex[:8]

    seed_block = ""
    if seeds:
        shown = rng.sample(seeds, k=min(2, len(seeds)))
        seed_block = (
            "REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):\n"
            + "\n".join(json.dumps(s, ensure_ascii=False) for s in shown)
            + "\n\n"
        )

    anti_seed_block = ""
    if anti_seeds:
        anti_seed_block = "ANTI-EXAMPLES (DO NOT generate anything resembling these):\n"
        for a in anti_seeds:
            anti_seed_block += f'- "{a.text}" — reason: {a.reason}\n'
        anti_seed_block += "\n"

    speaker_pre = ""
    if speaker_block:
        speaker_pre = speaker_block + "\n\n"

    rule_lines = _build_rules(schema, combination)
    diversity_block = _DIVERSITY_DIRECTIVES.get(diversity, "")
    user = _GEN_USER_TEMPLATE.format(
        schema_hint=json.dumps(schema.json_example(), indent=2),
        combo_lines=combo_lines,
        persona=persona,
        seed=seed,
        speaker_block=speaker_pre,
        seed_block=seed_block,
        anti_seed_block=anti_seed_block,
        diversity_block=diversity_block,
        rule_lines=rule_lines,
    )
    return _GEN_SYSTEM, user


def _build_rules(schema: DatasetSchema, combination: Combination) -> str:
    """Compose per-field rules, inlining enum-value semantics when pinned."""
    rules: list[str] = []
    for f in schema.fields:
        if f.name in combination:
            # Axis pins this field: pin + show what this specific value means.
            pinned_val = combination[f.name]
            explanation = ""
            if f.type == "enum" and f.values:
                match = next((v for v in f.values if v.name == pinned_val), None)
                if match and match.description:
                    explanation = f' — meaning: {match.description}'
            rules.append(f'- "{f.name}" must equal "{pinned_val}"{explanation}')
        elif f.type == "enum":
            # Field not pinned: list allowed values with their meanings so the
            # model picks the right one rather than the most obvious one.
            rules.append(f'- "{f.name}" must be one of:')
            for ev in f.values or []:
                if ev.description:
                    rules.append(f'    * "{ev.name}" — {ev.description}')
                else:
                    rules.append(f'    * "{ev.name}"')
        elif f.type == "float" and (f.min is not None or f.max is not None):
            rules.append(f'- "{f.name}" must be between {f.min} and {f.max}')
        elif f.type == "object":
            desc = f" — {f.description}" if f.description else ""
            rules.append(f'- "{f.name}" must be an object{desc} matching the structure shown above')
        elif f.type == "array":
            desc = f" — {f.description}" if f.description else ""
            rules.append(f'- "{f.name}" must be an array{desc} of items matching the structure shown above')
    if not rules:
        rules.append("- all fields must match the schema types above")
    return "\n".join(rules)
