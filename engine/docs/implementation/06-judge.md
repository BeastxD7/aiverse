# Stage 5 — CoT Judge

## Purpose

A second LLM pass scores each generated sample on three dimensions and removes low-quality examples before dedup. This is the main quality gate.

## Scoring dimensions

| Dimension | Min score to pass | What it checks |
|---|---|---|
| `correctness` | 7 / 10 | Label is accurate given the message text; speaker is in-scope |
| `realism` | 7 / 10 | Message reads like something a real user would type |
| `distinctiveness` | 7 / 10 | Message adds value; not a trivial paraphrase of another example |

All three thresholds are configurable in `cfg.judge` (`min_correctness`, `min_realism`, `min_distinctiveness`).

## Prompt design

The judge prompt includes:
- **Label definitions**: All enum fields with per-value descriptions (from config) so the judge knows the exact semantics of each label
- **Speaker block**: In-scope/out-of-scope constraints — judge auto-fails any sample from an out-of-scope speaker
- **Chain-of-thought**: Judge is asked to reason before scoring; scores are extracted from structured JSON output

## When to disable

Set `judge.enabled: false` when:
- Using Ollama (adds ~5–15 min of LLM calls per 10 samples)
- Running a quick sanity check and don't need quality filtering
- Target is very small (< 20) and you want to inspect raw output

Default: **off** for Ollama configs, **on** for Bedrock configs.

## Stats

`JudgeStats(judged, passed, failed)` — surfaced in CLI summary.

## File

`engine/src/synthdata_engine/stages/judge.py`
