# Stage 4 — Generation

## Purpose

Call the LLM for each combination row in the allocation plan, collect valid samples, and retry failures up to a limit.

## Concurrency

All plan rows are dispatched as asyncio tasks simultaneously, bounded by a semaphore at `cfg.provider.concurrency`:
- **Ollama:** `concurrency=1` (Ollama serializes at `NUM_PARALLEL=1` by default; higher values queue and hit timeouts)
- **Bedrock:** `concurrency=8` (parallelizes natively via separate HTTP connections; safe to raise to 16–32 for very large runs)

At 100K+ scale, the planner may produce rows with thousands of samples each. All tasks are created upfront — asyncio handles this efficiently (tasks are lightweight coroutine wrappers, not threads). The semaphore limits actual in-flight calls at any moment.

## JSON repair loop

Every LLM response goes through `_repair_json()`:
1. Direct `json.loads()`
2. Extract from fenced code block (` ```json ... ``` `)
3. Regex for first `{...}` or `[...]` outer object/array
4. Give up → mark as error, trigger corrective retry

## Refusal detection

`_looks_like_refusal()` flags a response as a refusal if:
- Response is short (< 50 chars) AND
- Contains apology keywords ("sorry", "cannot", "I'm not able", etc.) AND
- No `{` present (so valid JSON that happens to be short isn't misflagged)

## Schema validation and retry

After JSON repair, each sample is validated against `cfg.dataset_schema` via `schema.validate_row()`. On failure:
1. A corrective retry prompt is sent with the specific validation errors
2. If the retry also fails, the sample is discarded and counted in `GenStats.schema_failed`

## Per-sample checkpoint callback

After each successful sample, the `on_sample` callback fires. In pipeline runs with `--checkpoint-dir`, this writes the sample to `<dir>/<hash>.jsonl` immediately. At 100K scale this means the checkpoint file grows incrementally throughout the run — no data is lost if the run is interrupted.

## Progress reporting

Progress events fire on every sample. The CLI logs a milestone every `max(10, target_count // 100)` samples — at 100K that's every 1 000 samples, producing ~100 log lines total rather than 10 000.

## Stats

`GenStats(attempted, succeeded, schema_failed, refusals, errors, retries)` — surfaced in the CLI summary table and accumulated across the main run and all backfill passes.

## File

`src/synthdata_engine/stages/generate.py`
