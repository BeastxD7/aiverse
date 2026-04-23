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
  brief: |                   # What the dataset is for and what variety we want
    Training data for an intent classifier...
  target_count: 100          # How many samples to generate (1–100,000)
  diversity: high            # standard | high | edge_cases (not yet wired into prompts)
  persona_pool_size: 40      # How many distinct speaker personas to generate (5–200)
```

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
```

Bedrock credentials come from environment variables:
```
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_REGION=us-east-1
AWS_MODEL_ID=google.gemma-3-27b-it-qat-q8-0:2:2
```

Place a `.env` file at the repo root — it's auto-loaded via `python-dotenv`.

---

## `dedup`

```yaml
dedup:
  threshold: 0.85   # Jaccard similarity threshold (0.1–1.0); lower = more aggressive removal
  num_perm: 128     # MinHash permutations; higher = more accurate but slower
```

---

## `judge`

```yaml
judge:
  enabled: true          # false = skip judge stage entirely
  min_correctness: 7     # 0–10; samples below this score are removed
  min_realism: 7
  min_distinctiveness: 7
```

---

## `logic_filter`

```yaml
logic_filter:
  enabled: true       # false = skip combination filter (recommended for Ollama)
  batch_size: 25      # combinations per LLM call (5–100)
```
