# Providers

## Overview

Providers implement the `LLMProvider` protocol from `providers/base.py` with two async methods:

```python
async def generate_json(self, system, user, *, max_retries=3, temperature=0.8) -> LLMResponse
async def generate_text(self, system, user, *, max_retries=3, temperature=0.8) -> LLMResponse
```

`LLMResponse` carries `outcome` (`"success"` | `"error"` | `"refusal"` | `"throttled"`), `raw_text`, `parsed`, `error`, and `attempts`.

The `temperature` parameter is passed through to the model on every call. Axis discovery uses `temperature=0.3` for consistency; generation and judging use `0.8`.

---

## Ollama

**File:** `src/synthdata_engine/providers/ollama.py`

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

**File:** `src/synthdata_engine/providers/bedrock.py`

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

**Throttle handling:**

The provider detects AWS rate-limit errors and applies exponential backoff automatically — no config required.

Detected error codes:
```
ThrottlingException, TooManyRequestsException, RequestLimitExceeded,
ServiceUnavailableException, ModelNotReadyException
```

Backoff formula: `base = min(30 × attempt, 120)s` + `jitter = uniform(0, base × 0.25)`. Non-throttle errors (auth failure, model not found) are surfaced immediately without retrying.

At sustained 100K+ scale on Bedrock, expect throttling from AWS after ~30 minutes of continuous load. The backoff handles this automatically — runs slow down but never fail.

**Performance:** ~3–15s per call on gemma-3-27b-it. Full pipeline at target=10: ~50s (26× faster than local Ollama).

**Recommended models (us-east-1):**
| Model ID | Notes |
|---|---|
| `google.gemma-3-27b-it-qat-q8-0:2:2` | Tested baseline — high quality, fast |
| `us.amazon.nova-pro-v1:0` | Amazon's flagship — strong reasoning |
| `anthropic.claude-3-5-haiku-20241022-v1:0` | Fast + accurate, higher cost |

**Judge model override:**

Set `provider.judge_model` to use a stronger model for the quality judge while keeping a faster/cheaper model for generation:

```yaml
provider:
  type: bedrock
  model: google.gemma-3-27b-it-qat-q8-0:2:2         # generation
  judge_model: anthropic.claude-3-5-haiku-20241022-v1:0  # judge
```

---

## Adding a new provider

1. Create `src/synthdata_engine/providers/myprovider.py`
2. Implement the `LLMProvider` protocol from `providers/base.py` — both `generate_json` and `generate_text` with the `temperature` kwarg
3. Add `"myprovider"` to the `ProviderConfig.type` literal in `config.py`
4. Add dispatch cases in `pipeline._build_provider()` and `pipeline._build_judge_provider()`
