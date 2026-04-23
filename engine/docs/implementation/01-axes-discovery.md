# Stage 1 — Axes Discovery

## Purpose

Ask the LLM to identify the variation dimensions (axes) for the dataset. An axis is a categorical dimension like "tone", "speaker_type", or "urgency" with 2–6 possible values. Axes are the building blocks for combination-based generation diversity.

## Input

- `cfg.project.domain_brief` — plain-English description of the domain
- `cfg.dataset.brief` — what kind of data we want and why
- `cfg.dataset_schema` — field definitions including enum value names + descriptions
- `cfg.project.speakers` — in-scope and out-of-scope speaker types

## Output

`dict[str, list[str]]` — e.g. `{"tone": ["casual", "formal", "urgent"], "speaker_type": ["HR manager", "startup founder", ...]}`

## Key design decisions

**Schema reconciliation**: After the LLM returns axes, we cross-check every enum field in the schema. If an enum field (e.g. `label`) is not already in the returned axes, we inject it with its defined value names. This prevents the planner from ever missing a required label and is how we avoid label drift where the LLM forgets about certain enum values.

**Speaker constraint**: The prompt explicitly tells the LLM "Only include in-scope speaker types" and "Never include out-of-scope speaker types as axis values." Without this, LLMs tend to invent audience segments (e.g. "Candidate" in an HR product) based on domain knowledge rather than the config.

**Rich schema hint**: The prompt includes enum field names plus per-value descriptions so the LLM understands the semantic difference between values like `hide_jd` vs `delete_jd`.

## File

`engine/src/synthdata_engine/stages/discover.py`
