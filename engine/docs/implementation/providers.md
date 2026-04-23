# Providers

## Overview

Providers implement the `LLMProvider` base interface with two methods:
- `generate_json(prompt, max_output_tokens) -> dict | list` — for structured output
- `generate_text(prompt, max_output_tokens) -> str` — for free-text output

Both methods include a hard timeout (`asyncio.wait_for`) and JSON repair for `generate_json`.

---

## Ollama

**File:** `engine/src/synthdata_engine/providers/ollama.py`

**Setup:**
1. Install Ollama from [ollama.ai](https://ollama.ai)
2. Pull your model: `ollama pull gemma4:e4b`
3. Run: `ollama serve`

**Key implementation details:**
- `warmup()` sends a cheap 1-token generation to load the model before Stage 1 starts. Without this, the first real call absorbs a 30–90s cold start.
- `keep_alive="30m"` on every call keeps the model in VRAM between stages.
- `num_predict: max_output_tokens` caps generation length and prevents hung calls on models that generate until context window.
- Concurrency **must be 1**. Ollama's default `NUM_PARALLEL=1` means all concurrent calls queue and eat their timeouts.

**Performance:** ~60–90s per call on gemma4:e4b (Apple M-series). Full pipeline at target=10: ~22 minutes.

---

## AWS Bedrock

**File:** `engine/src/synthdata_engine/providers/bedrock.py`

**Setup:**
1. Create an AWS account with Bedrock access enabled
2. Enable model access for your chosen model in the Bedrock console
3. Create an IAM user or role with `bedrock:InvokeModel` permission
4. Add credentials to `.env` at repo root:

```env
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=...
AWS_REGION=us-east-1
AWS_MODEL_ID=google.gemma-3-27b-it-qat-q8-0:2:2
```

**Key implementation details:**
- Uses `boto3.client("bedrock-runtime").converse()` — the unified Bedrock API that works across model families
- `asyncio.to_thread` wraps the synchronous boto3 call so it doesn't block the event loop
- `asyncio.wait_for` provides a hard timeout around the thread call
- JSON reinforcement suffix appended to every user prompt since Bedrock has no native JSON mode on all models
- Reuses `_repair_json()` and `_looks_like_refusal()` from the Ollama provider

**Performance:** ~5–15s per call on gemma-3-27b-it. Full pipeline at target=10: ~50s (26× faster than local Ollama).

**Recommended models (us-east-1):**
| Model ID | Notes |
|---|---|
| `google.gemma-3-27b-it-qat-q8-0:2:2` | Tested baseline — high quality, fast |
| `us.amazon.nova-pro-v1:0` | Amazon's flagship — strong reasoning |
| `anthropic.claude-3-5-haiku-20241022-v1:0` | Fast + accurate, higher cost |

---

## Adding a new provider

1. Create `engine/src/synthdata_engine/providers/myprovider.py`
2. Implement `LLMProvider` interface from `providers/base.py`
3. Add `type: myprovider` to `ProviderConfig.type` literal in `config.py`
4. Add dispatch case in `pipeline._build_provider()` and `pipeline._build_judge_provider()`
