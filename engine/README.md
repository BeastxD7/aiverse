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
- [Dry-Run Mode](#dry-run-mode)
- [Checkpoint & Resume](#checkpoint--resume)
- [Debug Mode](#debug-mode)
- [Config Reference](#config-reference)
- [Balanced Class Coverage](#balanced-class-coverage)
- [Diversity Modes](#diversity-modes)
- [Quality Report](#quality-report)
- [Included Configs](#included-configs)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Performance Reference](#performance-reference)

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

**Important:** Always use `concurrency: 1` for Ollama. Ollama defaults to `NUM_PARALLEL=1` — multiple concurrent requests queue up and time out. Also disable `judge` and `logic_filter` to keep runtimes reasonable.

```yaml
provider:
  type: ollama
  model: gemma4:e4b
  concurrency: 1
  timeout_seconds: 300

judge:
  enabled: false

logic_filter:
  enabled: false
```

---

## Running a Job

```bash
uv run synthdata configs/emotion_detection_bedrock.yaml
```

**With options:**

```bash
# Override target count
uv run synthdata configs/emotion_detection_bedrock.yaml --target 100

# Change output file and format
uv run synthdata configs/emotion_detection_bedrock.yaml \
  --output datasets/emotion_100.jsonl \
  --format jsonl

# Export as CSV
uv run synthdata configs/emotion_detection_bedrock.yaml \
  --output datasets/emotion.csv \
  --format csv

# Export as a single JSON array
uv run synthdata configs/emotion_detection_bedrock.yaml \
  --output datasets/emotion.json \
  --format json

# Enable debug logs (writes per-stage markdown files)
uv run synthdata configs/emotion_detection_bedrock.yaml \
  --debug-dir debug/run1

# Preview the plan without generating anything
uv run synthdata configs/emotion_detection_bedrock.yaml \
  --dry-run

# Resume an interrupted run from a checkpoint folder
uv run synthdata configs/emotion_detection_bedrock.yaml \
  --target 500 \
  --checkpoint-dir checkpoints/

# All options combined
uv run synthdata configs/emotion_detection_bedrock.yaml \
  --target 50 \
  --output out/emotion_50.jsonl \
  --debug-dir debug/run1 \
  --checkpoint-dir checkpoints/
```

---

## CLI Reference

```
uv run synthdata <config.yaml> [OPTIONS]

Arguments:
  config.yaml              Path to the YAML config file (required)

Options:
  -o, --output PATH        Output file path (default: out_<timestamp>.jsonl)
  -f, --format TEXT        Output format: jsonl | json | csv (default: jsonl)
  --target INT             Override dataset.target_count from config
  -d, --debug-dir PATH     Write per-stage debug logs to this folder
  -c, --checkpoint-dir PATH  Resume interrupted runs from this folder
  --dry-run                Plan only: show axes, combinations, estimated calls — no generation
  --help                   Show this message and exit
```

---

## Dry-Run Mode

Pass `--dry-run` to preview the generation plan without making any LLM generation calls. Useful for estimating cost and validating your axes before committing to a full run.

```bash
uv run synthdata configs/emotion_detection_bedrock.yaml --target 100 --dry-run
```

Output:

```
┌──────────────────────────────────────────────────────┐
│ Combinations total            2880                   │
│ Combinations kept (filter)    119                    │
│ Plan rows                     8                      │
│ Planned samples               44                     │
│ Estimated LLM calls           ~52                    │
│ Estimated tokens (~800/call)  ~41,600                │
└──────────────────────────────────────────────────────┘
Axes:
  emotional_intensity: mild, moderate, strong
  writing_style: casual, slightly_formal, concise
  ...
```

Dry-run runs Stages 1 and 2 only (axis discovery + logic filter + allocation plan). No generation, judge, or dedup calls are made.

---

## Checkpoint & Resume

Long runs can be interrupted and resumed without losing progress.

```bash
# Start a run with checkpointing
uv run synthdata configs/emotion_detection_bedrock.yaml \
  --target 500 \
  --checkpoint-dir checkpoints/

# If interrupted, re-run the same command to resume
uv run synthdata configs/emotion_detection_bedrock.yaml \
  --target 500 \
  --checkpoint-dir checkpoints/
```

On resume, the engine loads samples from the checkpoint file, reduces the remaining target by the count already generated, and continues from where it left off.

**Checkpoint identity** is based on a content hash of your project/dataset brief, schema, seeds, and provider — not on `target_count` or `concurrency`. You can safely change `--target` or `concurrency` between runs without invalidating the checkpoint.

---

## Debug Mode

Pass `--debug-dir <folder>` to write detailed per-stage logs after every run. Each run creates a timestamped subfolder.

```bash
uv run synthdata configs/emotion_detection_bedrock.yaml \
  --target 20 \
  --debug-dir debug/run1
```

Inside `debug/run1/run_<timestamp>/` you'll find:

| File | What it shows |
|---|---|
| `01_axes_discovery.md` | Exact prompt sent to LLM + raw response + parsed axes |
| `02_logic_filter.md` | Per-batch: prompt, response, which combinations were kept vs removed |
| `03_allocation_plan.md` | Table of combination → target sample count |
| `04_personas.md` | Persona generation prompt + full list of generated personas |
| `05_generation.md` | Every sample attempt: combination, prompt, raw LLM response, parse result |
| `06_judge.md` | Every sample scored: LLM reasoning + correctness / realism / distinctiveness scores |
| `07_dedup.md` | Which samples were removed as near-duplicates |

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

provider:
  type: bedrock
  concurrency: 8
```

### Key fields

**`project.domain_brief`** — The most important field. Describe WHO the speakers are, WHAT they're trying to do, and in WHAT context. This grounds every stage of the pipeline.

**`dataset.target_count`** — How many samples to generate. The engine overshoots by ~10% and trims via judge + dedup. A backfill round runs automatically if you end up short.

**`dataset.require_balanced`** — Set `true` for multi-class classifiers. Prevents any label class from getting zero samples. See [Balanced Class Coverage](#balanced-class-coverage).

**`dataset.diversity`** — Controls variety in generated text. See [Diversity Modes](#diversity-modes).

**`dataset.axes`** — Pin axes manually to skip LLM-based axis discovery. Useful for reproducibility.

```yaml
dataset:
  axes:
    tone: [formal, casual, frustrated]
    channel: [chat, email, voice_transcript]
```

**`dataset.min_text_chars` / `dataset.max_text_chars`** — Quality gate applied after dedup. Samples outside this range are dropped (default: 10–2000 chars). For nested schemas, all string leaf values are concatenated before checking length.

**Supported field types:** `string`, `integer`, `float`, `boolean`, `enum`, `array`, `object`. Arrays and objects can be nested to any depth:

```yaml
schema:
  fields:
    - name: text
      type: string
    - name: spans
      type: array
      description: Named entity spans
      items:
        type: object
        fields:
          - name: start
            type: integer
            min: 0
          - name: end
            type: integer
            min: 0
          - name: label
            type: enum
            values: [PER, ORG, LOC]
    - name: metadata
      type: object
      fields:
        - name: source
          type: enum
          values: [news, social_media, review]
        - name: confidence
          type: float
          min: 0.0
          max: 1.0
```

The full nested structure is serialised into the generation prompt so the LLM knows exactly what shape to produce. Validation — including per-enum values and min/max bounds — is applied recursively at every level.

**`schema.fields[].values[].description`** — Per-enum-value descriptions dramatically improve label accuracy. Always include them for label fields.

**`anti_seeds`** — Negative examples the LLM must never generate. Use for common failure modes in your domain.

**`judge.enabled`** — Runs a second LLM pass scoring each sample 1–10 on correctness, realism, and distinctiveness. Adds ~30% to runtime but significantly improves quality. Recommended for Bedrock; disable for Ollama.

**`judge.min_correctness` / `min_realism` / `min_distinctiveness`** — Score thresholds (1–10, default: 7). Samples below any threshold are dropped.

**`logic_filter.enabled`** — Filters out implausible axis combinations before generation. Recommended for Bedrock; disable for Ollama.

Full config documentation: [`docs/implementation/config-reference.md`](docs/implementation/config-reference.md)

---

## Balanced Class Coverage

For multi-class classifiers, set `require_balanced: true` to guarantee every label class appears in the output.

```yaml
dataset:
  brief: Training data for a 4-class emotion classifier.
  target_count: 100
  require_balanced: true
```

**How it works:** After axis discovery, the engine injects all enum label fields as axes. Every combination explicitly targets one class, and the generation prompt hard-pins the label for that slot — the model can't drift to its default.

**Without `require_balanced`:** The model assigns whatever label fits the text it writes, which tends to favour common or emotionally salient classes and leave abstract ones (e.g. `out_of_scope`, `neutral`) with zero samples.

**With `require_balanced`:** All classes are guaranteed coverage. Some imbalance is still possible if the judge disproportionately rejects one class, but a **CRITICAL** warning fires at 0 samples and a **WARNING** fires below 60% of expected share.

---

## Diversity Modes

Control how varied the generated text is via `dataset.diversity`:

```yaml
dataset:
  diversity: high   # standard | high | edge_cases
```

| Mode | Effect |
|---|---|
| `standard` (default) | Natural variation — representative, mainstream examples |
| `high` | Unusual phrasing, rare contexts, demographic diversity, non-obvious word choices |
| `edge_cases` | Subtle and borderline examples — ambiguous labels, indirect expression, mixed signals |

**Note on `edge_cases`:** Without `require_balanced: true`, this mode tends to collapse toward a single dominant class. Use them together for per-class ambiguous examples.

---

## Quality Report

After every run, the engine prints a quality report in the summary table:

```
│ text (chars)    │ min=110  avg=197  max=334                          │
│ label           │ happy: 10  sad: 11  angry: 10  out_of_scope: 9    │
│ confidence      │ min=0.910  avg=0.952  max=1.000                    │
│ WARNING         │ field 'label' value 'happy' has only 5 samples ... │
```

- **String fields** show character length distribution (min/avg/max).
- **Enum fields** show per-value sample counts.
- **Float/integer fields** show actual value distribution.
- **WARNING** fires when any class falls below 60% of its expected even share.
- **CRITICAL** fires when any class has 0 samples.

---

## Included Configs

| Config | Provider | Labels | Balanced | Judge | Logic Filter |
|---|---|---|---|---|---|
| `configs/emotion_detection_bedrock.yaml` | Bedrock | happy, sad, angry, out_of_scope | ✓ | ✓ | ✓ |
| `configs/hr_intent_bedrock.yaml` | Bedrock | create_jd, refine_jd, delete_jd, hide_jd | — | ✓ | ✓ |
| `configs/hr_intent.yaml` | Ollama | create_jd, refine_jd, delete_jd, hide_jd | — | ✗ | ✗ |

**To switch from Bedrock to Ollama**, change the provider block and disable the heavy stages:

```yaml
provider:
  type: ollama
  model: gemma4:e4b
  concurrency: 1
  timeout_seconds: 300

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
│   ├── quality.py                    # Quality gate + distribution report
│   ├── debug.py                      # Debug log writer
│   ├── providers/
│   │   ├── base.py                   # LLMProvider protocol + LLMResponse
│   │   ├── bedrock.py                # AWS Bedrock (boto3, throttle backoff)
│   │   └── ollama.py                 # Ollama (local)
│   └── stages/
│       ├── discover.py               # Stage 1 — axis discovery
│       ├── logic_filter.py           # Stage 1.5 — combination filter
│       ├── plan.py                   # Stage 2 — allocation planner
│       ├── compose.py                # Stage 3 — personas + prompt assembly
│       ├── generate.py               # Stage 4 — parallel generation
│       ├── judge.py                  # Stage 5 — CoT quality judge
│       └── dedup.py                  # Stage 6 — MinHash LSH dedup
├── tests/
│   ├── test_compose.py
│   ├── test_dedup.py
│   ├── test_discover.py
│   ├── test_judge.py
│   ├── test_logic_filter.py
│   ├── test_plan.py
│   ├── test_quality.py
│   ├── test_schema.py
│   └── test_ollama_repair.py
├── docs/
│   ├── changelogs/
│   └── implementation/               # Per-stage implementation notes
├── pyproject.toml
└── README.md
```

---

## Running Tests

```bash
uv run pytest
```

70 tests cover every pipeline stage, quality module, schema validation, and dedup logic.

---

## Performance Reference

| Provider | Model | target=10 | target=40 | Notes |
|---|---|---|---|---|
| AWS Bedrock | google.gemma-3-27b-it | ~50s | ~52s | Parallelizes at concurrency=8 |
| Ollama (M-series Mac) | gemma4:e4b | ~22 min | ~90 min | Always use concurrency=1 |

Bedrock parallelizes natively. For large runs, `ThrottlingException` is handled automatically with exponential backoff (up to 120s + jitter) — no manual intervention needed.
