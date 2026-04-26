# Stage 1.5 — Logic Filter

## Purpose

Remove semantically invalid axis combinations before allocation and generation. For example, a combination of `{tone: "formal", speaker_type: "startup founder", label: "delete_jd"}` might be valid, but `{tone: "casual", label: "delete_jd", urgency: "critical"}` might be contradictory in context.

## Input

- All combinations from the Cartesian product of discovered axes
- `cfg.project.domain_brief` and `cfg.dataset.brief` as context
- `cfg.logic_filter.batch_size` — how many combinations per LLM call (default 25)

## Output

`list[Combination]` — only the combinations the LLM scored as valid

## Pre-sampling

Before the logic filter runs, we cap the combination pool to `max(target_count × 3, 100)` using a seeded random sample. This prevents wasting LLM calls on thousands of combinations when only a fraction will be used.

## Batching

Combinations are grouped into batches of `batch_size` and sent as parallel LLM calls. Each batch returns a list of valid combination indices. Results are merged across batches.

## When to disable

Set `logic_filter.enabled: false` in the config when:
- Using Ollama (LLM calls are slow; filter takes 5+ min per batch on local models)
- The domain is simple enough that all combinations are plausible
- Speed matters more than combination quality

Default: **off** for Ollama configs, **on** for Bedrock configs.

## File

`engine/src/synthdata_engine/stages/logic_filter.py`
