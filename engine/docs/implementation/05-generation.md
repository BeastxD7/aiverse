# Stage 4 — Generation

## Purpose

Call the LLM for each combination row in the allocation plan, collect valid samples, and retry failures up to a limit.

## Concurrency

Generation calls are batched across all plan rows using `asyncio.gather`. The provider's concurrency setting controls how many LLM calls run in parallel:
- Ollama: `concurrency=1` (Ollama serializes at `NUM_PARALLEL=1` by default; higher values queue and hit timeouts)
- Bedrock: `concurrency=8` (parallelizes natively via separate HTTP connections)

## JSON repair loop

Every LLM response goes through `_repair_json()`:
1. Direct `json.loads()`
2. Extract from fenced code block (` ```json ... ``` `)
3. Regex for first `{...}` or `[...]` outer object/array
4. Give up → mark as schema fail

## Refusal detection

`_looks_like_refusal()` flags a response as a refusal if:
- Response is short (< 50 chars) AND
- Contains apology keywords ("sorry", "cannot", "I'm not able", etc.) AND
- No `{` present (so valid JSON that happens to be short isn't misflagged)

## Schema validation

After JSON repair, each sample is validated against `cfg.dataset_schema` via `schema.validate_row()`. Schema fails are discarded and counted in `GenStats.schema_failed`.

## Retry

Each combination row retries up to `max_retries=3` if it undershoots its target. Total retry count is tracked in `GenStats.retries`.

## Stats

`GenStats(succeeded, schema_failed, refusals, errors, retries)` — surfaced in the CLI summary table.

## File

`engine/src/synthdata_engine/stages/generate.py`
