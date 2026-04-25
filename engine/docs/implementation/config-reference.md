# Config Reference

Full annotated reference for the SynthData YAML config format.

## Top-level structure

```yaml
project:      # Who uses this product and what it does
dataset:      # What data to generate and how much
schema:       # Output row structure (fields, types, enum values)
seeds:        # Positive examples (must pass schema validation)
anti_seeds:   # Negative examples (LLM must never replicate)
provider:     # LLM provider settings
dedup:        # Near-duplicate removal settings
judge:        # Quality judge settings
logic_filter: # Combination validity filter settings
```

---

## `project`

```yaml
project:
  name: "HR Intent Classifier"          # Human-readable job name
  domain_brief: |                       # WHO uses the product, in what context
    An HR SaaS product where HR-side professionals...
  speakers:
    in_scope:                           # ONLY these user types generate messages
      - HR manager at a mid-size company
      - Startup founder hiring their first employees
    out_of_scope:                       # NEVER generate messages from these
      - Candidates or applicants
      - Job seekers
```

**`domain_brief`** is the single most important field. It determines axis discovery, persona generation, and the semantic grounding of every generation call. Be specific about who the speakers are and what they're trying to accomplish.

---

## `dataset`

```yaml
dataset:
  brief: |                        # What the dataset is for (required)
    Training data for an intent classifier...
  target_count: 100               # How many samples to generate (1–100,000)
  diversity: standard             # standard | high | edge_cases
  require_balanced: false         # Force equal class coverage across enum label fields
  persona_pool_size: 20           # How many distinct speaker personas to generate (5–200)
  min_text_chars: 10              # Minimum character length for text fields (quality gate)
  max_text_chars: 2000            # Maximum character length for text fields (quality gate)
  axes:                           # Optional: pin axes to skip LLM discovery (for reproducibility)
    tone: [formal, casual, blunt]
    channel: [email, chat, phone]
```

### `diversity`

Controls how varied the generated samples are.

| Value | Behaviour |
|---|---|
| `standard` | Normal generation. Suitable for most datasets. |
| `high` | Pushes for unusual phrasing, underrepresented demographics, rare contexts. Increases variety at the cost of some realism. |
| `edge_cases` | Targets borderline, ambiguous, or subtle examples. Best combined with `require_balanced: true`. |

### `require_balanced`

When `true`, injects every enum label field as a generation axis after axis discovery. This forces every combination to explicitly target one class, guaranteeing all classes appear in the output. Without it, emergent label assignment consistently starves minority or ambiguous classes (e.g. `out_of_scope`, `neutral`).

Always enable this for multi-class classification datasets. The quality report issues a `CRITICAL` warning for any class that reaches 0 samples.

### `axes` (pinned)

Skips Stage 1 (LLM axis discovery) entirely. Use when you already know the right variation dimensions or need fully reproducible runs. The checkpoint hash is stable across runs when axes are pinned.

### `min_text_chars` / `max_text_chars`

Applied as a post-dedup quality gate on all `string` type fields. Samples where the combined text length falls outside `[min, max]` are removed before the final output is written. Filtered count is shown in the run summary.

---

## `schema`

```yaml
schema:
  fields:
    - name: text
      type: string
      description: The raw user message as typed in the HR chat interface.

    - name: label
      type: enum
      description: The HR user's intent
      values:
        - name: create_jd
          description: HR wants to draft a BRAND NEW job description from scratch.
        - name: refine_jd
          description: HR wants to modify an EXISTING job description.

    - name: confidence
      type: float
      min: 0.7
      max: 1.0
      description: Self-reported labeling confidence

    - name: source
      type: enum
      description: Where this example came from
      values:
        - name: synthetic
          description: Always this value
```

**Supported types:** `string`, `int`, `float`, `bool`, `enum`

For `enum` fields, providing per-value `description` is strongly recommended — it significantly improves label accuracy by giving the LLM semantic context, not just a string to copy.

---

## `seeds`

Positive examples that must pass schema validation. Used to show the LLM the correct output format and style.

```yaml
seeds:
  - text: "Hey can you draft a JD for a senior backend engineer?"
    label: create_jd
    confidence: 0.95
    source: synthetic
```

Minimum 1, maximum 10 seeds. Include at least one example per enum label if possible.

---

## `anti_seeds`

Negative examples the LLM must never replicate. Used to prevent out-of-scope speaker voices and common label confusions.

```yaml
anti_seeds:
  - text: "Hi, I'd like to apply for the senior engineer role."
    reason: Candidate voice — candidates never use this product.
```

Maximum 10 anti-seeds. Focus on the most common failure modes for your domain.

---

## `provider`

### Ollama

```yaml
provider:
  type: ollama
  model: gemma4:e4b          # required for ollama
  concurrency: 1             # must be 1 — Ollama serializes requests
  timeout_seconds: 300
  host: http://localhost:11434
```

### Bedrock

```yaml
provider:
  type: bedrock
  # model: us.amazon.nova-pro-v1:0   # optional — overrides AWS_MODEL_ID env var
  concurrency: 8             # Bedrock parallelizes natively
  timeout_seconds: 120
  judge_model: anthropic.claude-3-5-haiku-20241022-v1:0  # optional: use a different model for judging
```

Bedrock credentials come from environment variables:
```
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_REGION=us-east-1
AWS_MODEL_ID=google.gemma-3-27b-it-qat-q8-0:2:2
```

Place a `.env` file at the repo root — it's auto-loaded via `python-dotenv`.

**Throttling:** The Bedrock provider automatically detects `ThrottlingException`, `TooManyRequestsException`, `RequestLimitExceeded`, `ServiceUnavailableException`, and `ModelNotReadyException`. Throttled calls back off with `min(30 × attempt, 120)s + jitter` before retrying. No config needed.

---

## `dedup`

```yaml
dedup:
  threshold: 0.85   # Jaccard similarity threshold (0.1–1.0); lower = more aggressive removal
  num_perm: 128     # MinHash permutations; higher = more accurate but slower
```

At 100K+ samples, `num_perm: 64` reduces memory usage (~50%) with minimal accuracy loss.

---

## `judge`

```yaml
judge:
  enabled: true           # false = skip judge stage entirely
  min_correctness: 7      # 0–10; samples below this score are removed
  min_realism: 7
  min_distinctiveness: 6
  concurrency: 8          # how many samples to judge in parallel
```

Lower thresholds (6–7) are recommended for creative/ambiguous domains. Higher (8–9) for strict factual classification. Very high thresholds (9–10) combined with a small combo set will trigger multiple backfill passes — this is handled automatically.

---

## `logic_filter`

```yaml
logic_filter:
  enabled: true       # false = skip combination filter (recommended for Ollama)
  batch_size: 25      # combinations per LLM call (5–100)
```
