# SynthData Engine

Generate high-quality synthetic NLP training datasets from a plain-English YAML config. The engine runs a 6-stage pipeline — axis discovery, combination filtering, allocation planning, persona-based generation, CoT quality judging, and near-duplicate removal — and outputs a clean `jsonl`, `json`, or `csv` file ready for model training.

---

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Provider Setup](#provider-setup)
  - [AWS Bedrock (recommended)](#aws-bedrock-recommended)
  - [Ollama (offline / local)](#ollama-offline--local)
- [Running a Job](#running-a-job)
- [CLI Reference](#cli-reference)
- [Debug Mode](#debug-mode)
- [Config Reference](#config-reference)
- [Included Configs](#included-configs)
- [Project Structure](#project-structure)

---

## Requirements

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) — package manager

Install `uv` if you don't have it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## Installation

```bash
# Clone the repo
git clone <repo-url>
cd aiverse/engine

# Install dependencies
uv sync

# Verify the CLI is available
uv run synthdata --help
```

---

## Provider Setup

### AWS Bedrock (recommended)

Bedrock is the recommended provider — it's ~26× faster than local Ollama and produces higher quality output. Full pipeline at `target=10` takes ~50s.

**Step 1 — Enable model access**

1. Log into the [AWS Console](https://console.aws.amazon.com)
2. Go to **Amazon Bedrock → Model access**
3. Request access for your chosen model (e.g. `google.gemma-3-27b-it`)
4. Wait for approval (instant for most models)

**Step 2 — Create IAM credentials**

Create an IAM user or role with this policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "bedrock:InvokeModel",
      "Resource": "*"
    }
  ]
}
```

**Step 3 — Add credentials to `.env`**

Create a `.env` file at the **repo root** (one level above `engine/`):

```env
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=us-east-1
AWS_MODEL_ID=google.gemma-3-27b-it-qat-q8-0:2:2
```

The engine auto-loads this file from any subdirectory — you don't need to copy it.

**Recommended models (us-east-1)**

| Model ID | Speed | Quality | Notes |
|---|---|---|---|
| `google.gemma-3-27b-it-qat-q8-0:2:2` | Fast | High | Tested baseline |
| `us.amazon.nova-pro-v1:0` | Fast | High | Strong reasoning |
| `anthropic.claude-3-5-haiku-20241022-v1:0` | Very fast | Very high | Higher cost |

To use a different model, change `AWS_MODEL_ID` in `.env` — or pin it in the config:

```yaml
provider:
  type: bedrock
  model: us.amazon.nova-pro-v1:0   # overrides AWS_MODEL_ID
```

---

### Ollama (offline / local)

Use Ollama when you need to run without any cloud provider or API key. Expect ~22 minutes for `target=10` on an Apple M-series Mac (local models serialize requests).

**Step 1 — Install Ollama**

```bash
# macOS
brew install ollama

# Or download from https://ollama.ai
```

**Step 2 — Pull a model**

```bash
ollama pull gemma4:e4b
```

**Step 3 — Start the server**

```bash
ollama serve
```

Ollama runs at `http://localhost:11434` by default. The engine connects there automatically.

**Important:** Always use `concurrency: 1` for Ollama in your config. Ollama defaults to `NUM_PARALLEL=1` — multiple concurrent requests just queue up and time out.

```yaml
provider:
  type: ollama
  model: gemma4:e4b
  concurrency: 1        # must be 1
  timeout_seconds: 300
```

---

## Running a Job

```bash
uv run synthdata run configs/emotion_detection_bedrock.yaml
```

**With options:**

```bash
# Override target count
uv run synthdata run configs/emotion_detection_bedrock.yaml --target 100

# Change output file and format
uv run synthdata run configs/emotion_detection_bedrock.yaml \
  --output datasets/emotion_100.jsonl \
  --format jsonl

# Export as CSV
uv run synthdata run configs/emotion_detection_bedrock.yaml \
  --output datasets/emotion.csv \
  --format csv

# Export as a single JSON array
uv run synthdata run configs/emotion_detection_bedrock.yaml \
  --output datasets/emotion.json \
  --format json

# Enable debug logs (writes per-stage markdown files)
uv run synthdata run configs/emotion_detection_bedrock.yaml \
  --debug-dir debug/test1

# All options combined
uv run synthdata run configs/emotion_detection_bedrock.yaml \
  --target 50 \
  --output out/emotion_50.jsonl \
  --debug-dir debug/run1
```

---

## CLI Reference

```
uv run synthdata run <config.yaml> [OPTIONS]

Arguments:
  config.yaml           Path to the YAML config file (required)

Options:
  -o, --output PATH     Output file path (default: out.jsonl)
  -f, --format TEXT     Output format: jsonl | json | csv (default: jsonl)
  --target INT          Override dataset.target_count from config
  -d, --debug-dir PATH  Write per-stage debug logs to this folder
  --help                Show this message and exit
```

---

## Debug Mode

Pass `--debug-dir <folder>` to write detailed per-stage logs after every run. Each run creates a timestamped subfolder inside the directory you specify.

```bash
uv run synthdata run configs/emotion_detection_bedrock.yaml \
  --target 20 \
  --debug-dir debug/test1
```

Inside `debug/test1/run_<timestamp>/` you'll find:

| File | What it shows |
|---|---|
| `01_axes_discovery.md` | Exact prompt sent to LLM + raw response + parsed axes |
| `02_logic_filter.md` | Per-batch: prompt, response, which combinations were kept vs removed |
| `03_allocation_plan.md` | Table of combination → target sample count |
| `04_personas.md` | Persona generation prompt + full list of generated personas |
| `05_generation.md` | Every sample attempt: combination, prompt, raw LLM response, parse result, PASS/FAIL/RETRY |
| `06_judge.md` | Every sample scored: LLM reasoning + correctness / realism / distinctiveness scores |
| `07_dedup.md` | Which samples were removed as near-duplicates |

Open these files in VS Code or any markdown viewer to inspect exactly what the LLM received and returned at every step.

---

## Config Reference

A config is a YAML file with these top-level sections:

```yaml
project:      # Who uses the product and what it does
dataset:      # What data to generate and how much
schema:       # Output row structure (fields, types, enum values)
seeds:        # Positive examples (must pass schema validation)
anti_seeds:   # Negative examples the LLM must never replicate
provider:     # LLM provider and concurrency settings
dedup:        # Near-duplicate removal threshold
judge:        # Quality judge settings
logic_filter: # Combination validity filter
```

### Minimal example

```yaml
project:
  name: Sentiment Classifier
  domain_brief: Product reviews from e-commerce customers rating their purchase.

dataset:
  brief: Training data for a 3-class sentiment classifier.
  target_count: 100

schema:
  fields:
    - name: text
      type: string
      description: The customer review text.
    - name: label
      type: enum
      description: Sentiment of the review
      values:
        - name: positive
          description: Customer is satisfied or happy with the product.
        - name: negative
          description: Customer is dissatisfied or unhappy.
        - name: neutral
          description: Factual or mixed — no clear positive or negative signal.

seeds:
  - text: "Arrived on time and works exactly as described."
    label: positive
    source: synthetic

provider:
  type: bedrock
  concurrency: 8
```

### Key fields

**`project.domain_brief`** — The most important field. Describe WHO the speakers are, WHAT they're trying to do, and in WHAT context. This grounds every stage of the pipeline.

**`project.speakers.in_scope` / `out_of_scope`** — Constrain which user types appear. The engine enforces these throughout axis discovery, persona generation, and per-sample generation.

**`schema.fields[].values[].description`** — Per-enum-value descriptions dramatically improve label accuracy. Always include them for label fields.

**`anti_seeds`** — Negative examples the LLM must never generate. Use for the most common failure modes in your domain (out-of-scope speakers, mislabeled edge cases, etc.).

**`judge.enabled`** — Runs a second LLM pass scoring each sample 1-10 on correctness, realism, and distinctiveness. Removes samples below threshold. Adds ~30% to runtime but significantly improves quality. Recommended for Bedrock; disable for Ollama.

**`logic_filter.enabled`** — Filters out implausible axis combinations before generation. Recommended for Bedrock; disable for Ollama.

Full config documentation: [`docs/implementation/config-reference.md`](docs/implementation/config-reference.md)

---

## Included Configs

| Config | Provider | Labels | Judge | Logic Filter |
|---|---|---|---|---|
| `configs/emotion_detection_bedrock.yaml` | Bedrock | happy, sad, angry, out_of_scope | ✓ | ✓ |
| `configs/hr_intent_bedrock.yaml` | Bedrock | create_jd, refine_jd, delete_jd, hide_jd | ✓ | ✓ |
| `configs/hr_intent.yaml` | Ollama | create_jd, refine_jd, delete_jd, hide_jd | ✗ | ✗ |

**To switch a config from Bedrock to Ollama**, change the provider block:

```yaml
# Before (Bedrock)
provider:
  type: bedrock
  concurrency: 8

# After (Ollama)
provider:
  type: ollama
  model: gemma4:e4b
  concurrency: 1
  timeout_seconds: 300
```

Also disable judge and logic_filter to keep runtimes reasonable:

```yaml
judge:
  enabled: false

logic_filter:
  enabled: false
```

---

## Project Structure

```
engine/
├── configs/                          # Ready-to-use YAML configs
│   ├── emotion_detection_bedrock.yaml
│   ├── hr_intent_bedrock.yaml
│   └── hr_intent.yaml
├── src/synthdata_engine/
│   ├── cli.py                        # CLI entry point (uv run synthdata)
│   ├── pipeline.py                   # Orchestrates all 6 stages
│   ├── config.py                     # YAML → Pydantic config models
│   ├── schema.py                     # Dataset schema validation
│   ├── debug.py                      # Debug log writer
│   ├── providers/
│   │   ├── base.py                   # LLMProvider protocol + LLMResponse
│   │   ├── bedrock.py                # AWS Bedrock (boto3)
│   │   └── ollama.py                 # Ollama (local)
│   └── stages/
│       ├── discover.py               # Stage 1 — axis discovery
│       ├── logic_filter.py           # Stage 1.5 — combination filter
│       ├── plan.py                   # Stage 2 — allocation planner
│       ├── compose.py                # Stage 3 — personas + prompt assembly
│       ├── generate.py               # Stage 4 — parallel generation
│       ├── judge.py                  # Stage 5 — CoT quality judge
│       └── dedup.py                  # Stage 6 — MinHash LSH dedup
├── docs/
│   ├── changelogs/v0.1.0.md
│   └── implementation/               # Per-stage implementation notes
├── tests/
├── pyproject.toml
└── README.md
```

---

## Running Tests

```bash
uv run pytest
```

---

## Performance Reference

| Provider | Model | target=10 | Estimated target=100 |
|---|---|---|---|
| AWS Bedrock | google.gemma-3-27b-it | ~50s | ~2–3 min |
| Ollama (M-series Mac) | gemma4:e4b | ~22 min | ~3–4 hours |

Bedrock parallelizes natively at `concurrency=8`. Ollama serializes all requests regardless of concurrency setting — always use `concurrency: 1`.
