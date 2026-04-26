# Stage 5 — CoT Judge

## Purpose

A second LLM pass scores each generated sample on three dimensions and removes low-quality examples before dedup. This is the primary quality gate.

## Scoring dimensions

| Dimension | Default min | What it checks |
|---|---|---|
| `correctness` | 7 / 10 | Label is accurate given the message text; speaker is in-scope |
| `realism` | 7 / 10 | Message reads like something a real user would type |
| `distinctiveness` | 6 / 10 | Message adds value; not a trivial paraphrase of another example |

All three thresholds are configurable in `cfg.judge` (`min_correctness`, `min_realism`, `min_distinctiveness`).

## Prompt design

The judge prompt includes:
- **Label definitions**: All enum fields with per-value descriptions (from config) so the judge knows the exact semantics of each label
- **Speaker block**: In-scope/out-of-scope constraints — judge auto-fails any sample from an out-of-scope speaker
- **Chain-of-thought**: Judge is asked to reason before scoring; scores are extracted from a trailing JSON block

## Concurrency

Judging runs concurrently at `cfg.judge.concurrency` (default 8). This is independent of `provider.concurrency` — you can judge faster than you generate, or vice versa. At 100K scale, raising judge concurrency to 16–32 reduces overall pipeline time significantly.

## Fail-open on parse error

If the judge response can't be parsed (no trailing JSON, truncated response, refusal), the sample is kept (`unparseable` counter incremented). This prevents a flaky judge from silently discarding valid data.

## Judge model override

By default the judge uses the same model as generation. For higher accuracy, configure a separate (typically stronger) model:

```yaml
provider:
  type: bedrock
  model: google.gemma-3-27b-it-qat-q8-0:2:2         # generation model
  judge_model: anthropic.claude-3-5-haiku-20241022-v1:0  # judge model
```

Using a stronger judge with a cheaper generator is the best cost/quality trade-off for large runs.

## Interaction with backfill

The judge runs on every backfill pass, not just the initial generation. At high thresholds (min=8+) in a narrow domain, expect 2–3 backfill passes to converge. The pipeline handles this automatically with escalating overshoot per pass.

## When to disable

Set `judge.enabled: false` when:
- Using Ollama (adds ~5–15 min of LLM calls per 10 samples)
- Running a quick sanity check and don't need quality filtering
- Target is very small (< 20) and you want to inspect raw output

Default: **off** for Ollama configs, **on** for Bedrock configs.

## Stats

`JudgeStats(judged, passed, failed, unparseable)` — surfaced in CLI summary.

## File

`src/synthdata_engine/stages/judge.py`
