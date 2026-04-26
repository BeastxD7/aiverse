# aiverse

A collection of AI-powered tools for building, testing, and shipping intelligent products.

---

## What's Inside

| Module | Description | Status |
|---|---|---|
| [`engine/`](engine/) | SynthData Engine — generate labeled NLP training datasets from a YAML config | v0.1.0 |

---

## SynthData Engine

Generate high-quality synthetic NLP training data using any LLM (AWS Bedrock or local Ollama). Define your schema and domain in a YAML config file — the engine handles everything else.

**Full pipeline in ~50 seconds on AWS Bedrock:**

```
Axes Discovery → Logic Filter → Allocation Plan → Persona Generation → LLM Generation → Quality Judge → Deduplication
```

**Key features:**

- **BYOK** — Bring Your Own Key. Works with AWS Bedrock or local Ollama; no vendor lock-in
- **Schema-driven** — define `string`, `enum`, `integer`, `float`, `boolean`, `array`, and nested `object` fields; all validated at generation time
- **Balanced class coverage** — `require_balanced: true` guarantees every label class appears in output
- **Quality judge** — Chain-of-Thought LLM judge scores each sample on correctness, realism, and distinctiveness; rejects below threshold
- **Near-duplicate removal** — MinHash LSH dedup removes surface variants while preserving paraphrases
- **Checkpoint & resume** — interrupt and resume long runs without losing progress
- **Dry-run mode** — preview the generation plan and estimated token cost before committing

### Quick Start

```bash
# Install
cd engine
uv sync

# Run with AWS Bedrock
uv run synthdata configs/emotion_detection_bedrock.yaml

# Preview the plan without generating
uv run synthdata configs/emotion_detection_bedrock.yaml --dry-run

# Override target count
uv run synthdata configs/emotion_detection_bedrock.yaml --target 500
```

### Providers

| Provider | Best for | Setup guide |
|---|---|---|
| [AWS Bedrock](docs/providers/bedrock.md) | Quality runs, large targets, production | [docs/providers/bedrock.md](docs/providers/bedrock.md) |
| [Ollama](docs/providers/ollama.md) | Offline / local / no API key | [docs/providers/ollama.md](docs/providers/ollama.md) |

### Minimal Config

```yaml
project:
  name: Sentiment Classifier
  domain_brief: Product reviews from e-commerce customers rating their purchase.

dataset:
  brief: Training data for a 3-class sentiment classifier.
  target_count: 100
  require_balanced: true

schema:
  fields:
    - name: text
      type: string
      description: The customer review text.
    - name: label
      type: enum
      description: Sentiment of the review.
      values:
        - name: positive
          description: Customer is satisfied or happy.
        - name: negative
          description: Customer is dissatisfied or unhappy.
        - name: neutral
          description: Factual or mixed — no clear positive or negative signal.

seeds:
  - text: "Arrived on time and works exactly as described."
    label: positive

provider:
  type: bedrock
  concurrency: 8
```

### Performance

| Provider | Model | target=10 | target=50 | target=100 |
|---|---|---|---|---|
| AWS Bedrock | google.gemma-3-27b-it | ~50s | ~60s | ~2–3 min |
| Ollama (M-series Mac) | gemma4:e4b | ~22 min | ~90 min | ~3 hrs |

**Full documentation:** [`engine/README.md`](engine/README.md)  
**Architecture deep-dive:** [`docs/explanation.md`](docs/explanation.md)  
**Provider guides:** [Bedrock](docs/providers/bedrock.md) · [Ollama](docs/providers/ollama.md)

---

## Requirements

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) package manager

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## Running Tests

```bash
cd engine
uv run pytest
```

92 tests covering every pipeline stage, schema validation, quality module, and dedup logic.

---

## License

MIT
