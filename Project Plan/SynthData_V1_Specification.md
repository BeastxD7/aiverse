# SynthData V1 — Complete Specification

> **Version:** 1.0 Final
> **Date:** April 2026
> **Status:** Ready for implementation
> **Audience:** Engineers, architects, and anyone building or reviewing this

---

## What this document is

This is the **complete definition of SynthData V1** — what it does, what it doesn't, how every part works, what breaks and how we handle it.

Written in plain English. No unexplained jargon. If you read this end-to-end, you will fully understand what we're building.

---

## Table of contents

1. [What is V1 in one sentence](#1-what-is-v1-in-one-sentence)
2. [What V1 can do](#2-what-v1-can-do)
3. [What V1 cannot do](#3-what-v1-cannot-do)
4. [Who V1 is for](#4-who-v1-is-for)
5. [The capacity — what you can generate](#5-the-capacity--what-you-can-generate)
6. [The user journey — from signup to dataset](#6-the-user-journey--from-signup-to-dataset)
7. [The pipeline — how data is actually made](#7-the-pipeline--how-data-is-actually-made)
8. [Error handling — what happens when things break](#8-error-handling--what-happens-when-things-break)
9. [Quality — how we know the data is good](#9-quality--how-we-know-the-data-is-good)
10. [The tech stack](#10-the-tech-stack)
11. [What we cut and why](#11-what-we-cut-and-why)
12. [Success criteria](#12-success-criteria)

---

## 1. What is V1 in one sentence

**SynthData V1 is a web platform where ML engineers generate up to 100,000 training examples for NLP tasks by describing their domain in plain English — using their own AI provider API key.**

That's it. No more, no less.

---

## 2. What V1 can do

### Core capabilities

- **Generate NLP datasets** — text classification, intent detection, NER, Q&A, sentiment, or any custom text schema the user defines
- **Up to 100,000 samples per job** — comfortable ceiling, fits the sweet spot for fine-tuning small language models
- **Five AI providers supported** — OpenAI, Anthropic, Groq, AWS Bedrock, Ollama (for local runs)
- **Bring Your Own Key (BYOK)** — users pay their provider directly; SynthData never proxies calls
- **Schema-enforced output** — every row matches a JSON structure the user defines upfront
- **Three standard output formats** — JSONL (fine-tune ready), JSON (inspectable), CSV (analyst friendly)

### What users actually experience

- Sign up with email and password, no credit card
- Create a project (like "HR intent classifier")
- Define their dataset — domain, schema, 2-3 seed examples
- Pick their LLM provider, paste their API key (encrypted and stored locally)
- Click Generate
- Watch a live dashboard showing progress, current batch, success rate
- Download the finished dataset when done

### Quality features baked into V1

- **Automatic prompt engineering** — the system designs prompts for the user, they never write one
- **Near-duplicate detection** — MinHash catches trivial variants that slip through
- **Schema validation** — every sample is checked before admission
- **Auto-retry on failure** — failed generations retry up to 3 times
- **Crash-safe jobs** — if the system restarts mid-job, it resumes from where it stopped
- **Live progress** — users see what's happening in real time, not a black box

---

## 3. What V1 cannot do

Being honest about limits upfront prevents scope creep and user disappointment.

### Not supported (explicitly out of scope)

- **Datasets larger than 100,000 samples** — needs augmentation tricks that hurt quality; deferred to V2
- **Tabular / structured data** — different problem, different tool (Gretel, SDV)
- **Image or audio data** — wrong product entirely
- **Non-English output** — meta-prompt is tuned for English only
- **Multi-turn dialogue** — single-row generation only in V1
- **Real-time streaming generation** — batch jobs only
- **Dataset versioning** — export creates a snapshot, no history tracking
- **Team collaboration features** — single user per account
- **Comparing multiple generation runs side-by-side** — simple export only
- **Fine-tuning benchmarks** — we generate data, we don't train models

### Limitations users should know about

- **Users need their own API key** — no free LLM calls from us
- **Jobs can take hours** — 100K samples ≈ 2-3 hours depending on provider speed
- **User's rate limits apply** — if their OpenAI tier is limited, generation is throttled
- **Quality depends on provider quality** — Ollama local llama-3-8b produces worse output than GPT-4o

---

## 4. Who V1 is for

### Primary user — the ML engineer

**Who they are:**
- Mid-level to senior ML engineer at a 50-5000 person company
- Comfortable with Python, JSONL, HuggingFace, API keys
- Has a specific fine-tuning goal — a production model they need to ship
- Already knows what schema they need
- Willing to pay $5-$50 in LLM costs for a dataset

**What they want:**
- Go from "I need data" to "I have data" in under a day
- Not write a single prompt themselves
- Know the data is clean and fine-tune ready
- Own the data, own the costs, no vendor lock-in

**What they don't want:**
- A 2-week project to set up a generation pipeline
- To hire annotators
- To explain to legal why they're using production data
- Vendor lock-in from hosted services

### Who V1 is NOT for

- **Product managers** who want to click a button and get a model — wrong audience
- **Researchers doing foundation model pretraining** — wrong scale
- **Teams with no API budget** — BYOK means users pay for compute
- **Non-technical users** — this assumes comfort with schemas, JSON, API keys

---

## 5. The capacity — what you can generate

### Tier structure

| Tier | Max samples per job | Features | Pricing |
|---|---|---|---|
| **Free** | 1,000 | Basic pipeline, no judge | $0 (user pays LLM costs) |
| **Pro** | 25,000 | Full pipeline with judge | ~$29/month |
| **Team** | 100,000 | Full pipeline, priority queue | ~$99/month |

### Real numbers — what to expect

| Samples | Time | LLM calls | User's LLM cost (Groq llama-3) |
|---|---|---|---|
| 500 | 2 min | ~60 | $0.30 |
| 1,000 | 3 min | ~120 | $0.60 |
| 10,000 | 30 min | ~1,200 | $6 |
| 25,000 | 1 hour | ~2,500 | $12 |
| 100,000 | 2-3 hours | ~10,000 | $45 |

Costs roughly 10x higher on GPT-4o or Claude Sonnet, 5x higher on gpt-4o-mini. SynthData shows the estimate before generation.

### Why 100K is the hard ceiling

- At 100K, pure LLM generation still produces high quality (90%+ unique after dedup)
- Past 100K, you need augmentation tricks that reduce quality
- Enterprise users who need millions of samples should wait for V2
- 100K is more than enough for 95% of fine-tuning tasks

---

## 6. The user journey — from signup to dataset

### Step 1 — Sign up

User lands on SynthData homepage, clicks "Start free", creates account with email + password. No credit card required.

**What happens under the hood:**
- Account created in Postgres
- Default project limits set based on tier (Free: 1000 samples/job)
- JWT access token issued, 15-minute expiry, 7-day refresh

### Step 2 — Create a project

User clicks "New project", names it (e.g. "HR Intent Classifier"), writes a brief description of what they're building.

**What the system captures:**
- Project name
- Detailed brief (plain English description — this primes every generation)
- Optional template selection (Intent classification, NER, Q&A, etc.) — pre-fills a starter schema

### Step 3 — Configure the dataset

Multi-step wizard:

**Step 3a — AI provider**
- Pick provider (OpenAI, Anthropic, Groq, Bedrock, Ollama)
- Enter API key (encrypted at rest with AES-256)
- Click "Test key" — system verifies the key works before proceeding

**Step 3b — Context**
- What is this specific dataset for? (plain English, e.g. "Adversarial phrasings to stress-test the classifier")

**Step 3c — Schema**
- Define each field — name, type, description of what it's for
- User can paste a JSON example if they prefer
- System enforces: at least one string field, maximum 10 fields in V1

**Step 3d — Seed examples**
- User provides 2-3 "perfect" example rows
- These ground the generation — every batch gets them as anchors

**Step 3e — Volume & settings**
- Target sample count (slider: 100, 500, 1000, 5000, 10000, 25000, 100000)
- Diversity mode (Standard, High, Edge cases)
- Dedup threshold (Default: MinHash 0.85, adjustable)

### Step 4 — Review and estimate

Before generation starts, system shows:
- Total LLM calls estimated
- Time estimate
- Cost estimate (on user's provider)
- Credit check — does user have enough platform credits?

### Step 5 — Generation runs

User clicks "Generate", redirected to the Job Engine screen:
- Large percentage counter (0% → 100%)
- Per-batch progress
- Live log (INFO / OK / WARN events)
- Throughput chart (rows per minute)
- Validity / dup rate / retry rate cards

### Step 6 — Download

When job hits 100%:
- Stats summary appears (rows, validity, duplicates, tokens, duration, cost)
- Intent/label distribution visualization
- Preview of 8-10 sample rows
- Three download buttons: **JSONL**, **JSON**, **CSV**
- Optional: "Push to HuggingFace" button

### Step 7 — Mobile monitoring (nice-to-have)

Long jobs can be monitored from the mobile app:
- Shows running jobs with live percentage
- Shows completed jobs with download button
- Push notifications when job finishes

---

## 7. The pipeline — how data is actually made

This is the heart of the platform. Six stages. Each has one job.

### Stage 1 — Discover the axes

**What it does:** Figures out the different "dimensions" that vary in this specific domain.

**Plain English analogy:** If you're describing pizzas, the axes are cheese, topping, crust. If you're describing weather, the axes are location, season, severity. Every domain has different axes.

**How it works:**
- System sends one prompt to the user's LLM: *"What are the 3-6 dimensions that naturally vary in this domain?"*
- LLM returns a JSON object with axes and values
- Result is cached per project — we don't re-discover axes every job

**Example output for HR domain:**
```
intent:  [create_jd, refine_jd, delete_jd, hide_jd]  (4 values)
tone:    [formal, casual, urgent]                    (3 values)
persona: [HR manager, founder, recruiter, CHRO,
          HR assistant]                              (5 values)
context: [startup, enterprise, agency]               (3 values)
```

**Why it's domain-agnostic:**
The LLM already knows every domain. We let it tell us what varies, instead of hardcoding axes that only work for one domain.

### Stage 1.5 — Logic filter (new in V1 based on reviewer feedback)

**What it does:** Removes impossible or illogical combinations before we waste LLM calls on them.

**Plain English analogy:** It doesn't make sense to generate "a report_harassment intent in a cheerful tone." A human would never write that. So we remove it.

**How it works:**
- System takes all combinations from Stage 1 (e.g. 4×3×5×3 = 180)
- Sends them to a small, fast LLM (Llama-3-8b or Haiku) in batches of 50
- Asks: *"Which of these combinations make logical sense?"*
- Drops the combinations that don't

**Expected outcome:**
- Start with ~180 combinations
- Drop ~10-15% as illogical
- End with ~150 valid combinations

### Stage 2 — Plan the allocation

**What it does:** Given the valid combinations and target count, figures out exactly how many samples to generate per combination.

**The core math:**
```
examples_per_combination = target_count ÷ valid_combinations
```

**The sweet spot rule:**
- Aim for 5-20 examples per combination
- Below 5 → too random
- Above 20 → starts repeating within a combination

**Three cases the allocator handles:**

| If combinations are | What the allocator does |
|---|---|
| In sweet spot (50-200 for 1000 target) | Proceed directly, split evenly |
| Too few (fewer than 50) | Ask Stage 1 to expand values, or generate more per combo |
| Too many (more than 200) | Randomly sample from combination pool |

**What gets written to the database:**

The plan is saved as individual rows in Postgres:
```
job_id | combination_id | combo_values              | status  | retries
abc123 | 001            | {intent:create_jd, ...}   | pending | 0
abc123 | 002            | {intent:refine_jd, ...}   | pending | 0
...
abc123 | 150            | {intent:hide_jd, ...}     | pending | 0
```

This is the checkpointing mechanism — if the system crashes, it picks up from where `status = pending`.

### Stage 3 — Compose the prompts

**What it does:** Builds one unique prompt per combination. Injects a random persona for extra variety.

**The persona pool:**
- At project creation, we generate 100-200 personas specific to the domain
- Cached per project
- User can click "Regenerate personas" in the UI if they want fresh variety

**A composed prompt looks like:**
```
System: You are generating one training example for HR intent classification.

Respond ONLY with valid JSON matching this schema:
{text: string, label: string, confidence: float, source: string}

Rules:
- label must be exactly "create_jd"
- source must be "synthetic"
- confidence must be between 0.7 and 1.0

Context for THIS specific example:
- Intent: create_jd
- Tone: casual
- Scenario: startup
- Speaker: A startup founder hiring their first engineer, writes short direct messages
- Seed: 3f9a-b7c2-[unique ID per call]

Generate the example now.
```

### Stage 4 — Generate in parallel

**What it does:** Fires the prompts at the LLM provider. Manages concurrency, retries, and validates every response.

**How parallelism works:**
- Default concurrency: 10 calls at once
- Each call has 30-second timeout
- Structured output mode enabled when the provider supports it (OpenAI, Anthropic, Bedrock) — this guarantees valid JSON at 99%+ rates

**What happens to each response:**
1. Response comes back from LLM
2. Parsed as JSON
3. Validated against the user's schema:
   - All required fields present?
   - Field types correct?
   - Enum values allowed?
4. If valid → marked as success, saved to DB
5. If invalid → retry up to 3 times with exponential backoff
6. If still invalid after 3 retries → logged as schema failure

**Handling safety refusals (new in V1 based on reviewer feedback):**

Sometimes the LLM refuses to generate because it thinks the prompt is unsafe (e.g. HR data mentioning "workplace violence"). When this happens:
- Refusal detected via heuristics (short response, apology keywords, no JSON)
- Marked as `safety_refusal` in logs
- Combination is skipped, not retried
- User sees a note in the final report: "5 combinations skipped due to provider safety filters"

### Stage 5 — Judge the quality

**What it does:** A second, cheaper LLM scores every generated sample to catch bad outputs.

**Plain English analogy:** Like a QA reviewer checking each row before it goes into the final dataset. If it's bad, it gets thrown out.

**The judge scores each sample on three axes:**

| Axis | What it checks |
|---|---|
| **Correctness** (1-10) | Does the text actually match the label? |
| **Realism** (1-10) | Would a real user say this naturally? |
| **Distinctiveness** (1-10) | Is it meaningfully different from typical examples? |

**The judge uses Chain-of-Thought:**
Instead of just returning a score, the judge writes a one-sentence justification first. This dramatically improves grading accuracy for small models.

Example judge output:
```
Reasoning: "The text clearly expresses intent to create a JD,
tone matches 'casual startup' context, and the phrasing
feels natural. Not a common example."
Correctness: 9
Realism: 8
Distinctiveness: 8
Verdict: KEEP
```

**Thresholds:**
- All scores must be ≥ 7 to keep the sample
- Free tier: judge is **OFF** by default (cost saving)
- Pro and Team: judge is **ON** by default

**If the judge itself fails (new in V1 based on reviewer feedback):**
- Can't parse judge response → default to PASS (give benefit of doubt)
- Judge times out → default to PASS
- Judge hits rate limit → pause job, resume when available

### Stage 6 — Deduplicate with MinHash LSH (new in V1)

**What it does:** Removes trivial duplicates that exact-match misses.

**Why MinHash and not exact match:**
Exact match misses things like:
- `"Create a JD"` vs `"create a jd"` (case)
- `"Create a JD."` vs `"Create a JD!"` (punctuation)
- `"Create a JD"` vs `"Create  a  JD"` (whitespace)

MinHash catches all of these in near-linear time, without needing expensive embeddings.

**Why not aggressive semantic dedup:**
We don't want to kill valuable paraphrases:
- `"I want to create a JD"` and `"I need to make a new job post"` — **both kept**
- These teach the model variety, they're not duplicates

**The MinHash approach:**
- Each sample's text is tokenized
- A MinHash signature (128 hashes) is computed
- LSH (Locality-Sensitive Hashing) groups similar signatures
- Threshold: 0.85 Jaccard similarity
- Duplicates are dropped, unique samples kept

**Backfill mechanism:**
If dedup brings total below target:
- System tracks the gap (e.g. target 1000, have 940)
- Queues more generation calls from underrepresented combinations
- Continues until target is hit
- Typical overshoot buffer: 5-10% extra to reduce backfill rounds

---

## 8. Error handling — what happens when things break

This is where most pipelines fail in production. V1 has explicit handling for every failure mode.

### Error category 1 — Transient LLM errors

**What can go wrong:**
- Network timeout
- Provider temporarily down (503)
- Response truncated mid-generation
- Rate limit hit (429)

**How we handle it:**
- **Retry with exponential backoff**: 1s, 2s, 4s, 8s
- **Max 3 retries per sample**
- **If rate-limited**: pause the job, alert user, resume when window clears
- **If rate-limit persists > 15 minutes**: suspend job, require manual resume

### Error category 2 — Invalid LLM output

**What can go wrong:**
- LLM returns non-JSON
- LLM returns valid JSON but wrong schema
- Enum value outside allowed set
- Type mismatch (number where string expected)

**How we handle it:**
- **First attempt**: coerce obvious types (string "0.9" → float 0.9)
- **If still invalid**: retry with a corrective prompt ("Your previous response failed validation because X")
- **If still invalid after retry**: mark as schema failure, move on
- **If > 10% of batch fails schema**: pause job, alert user about possible provider issue

### Error category 3 — Safety refusals

**What can go wrong:**
- Provider flags prompt as unsafe
- Returns error instead of JSON
- Returns apology text instead of generation

**How we handle it:**
- **Detect via heuristics**: short response, apology keywords ("I cannot", "I apologize"), no JSON structure
- **Don't retry** — it'll refuse again
- **Log as `safety_refusal`** for that combination
- **Skip to next combination**
- **User sees summary**: "N combinations skipped due to safety filters"

### Error category 4 — System crashes mid-job

**What can go wrong:**
- Server restarts
- Worker node fails
- Database connection drops
- User cancels and resumes later

**How we handle it:**
- **Database checkpointing**: every combination's status (pending/running/complete/failed) is in Postgres
- **On restart**: workers spin up, query `status = pending` or `status = running`, resume from there
- **Deduplication on resume**: if a combination finished generating but DB didn't persist, dedup catches the duplicate
- **User sees no disruption**: progress bar continues from where it stopped

### Error category 5 — User errors

**What can go wrong:**
- Invalid API key
- Bad schema definition
- Contradictory seed examples
- Target count too high for tier

**How we handle it:**
- **Validate before job starts**: test API key, schema, seed examples
- **Show clear error message**: "Your seed example has 'Apply for Job' label but your intents don't include that"
- **Don't start the job** until issues are resolved
- **Save as draft** so user can fix and resume

### Error category 6 — Judge failures

**What can go wrong:**
- Judge LLM can't parse the score format
- Judge hallucinates and returns reasoning without score
- Judge times out

**How we handle it:**
- **If score can't be parsed**: default to PASS (lean generous)
- **If judge times out**: skip judging for that sample, mark as `unjudged`, include in dataset
- **If judge fails on > 20% of samples**: pause job, alert user, suggest switching judge model

### What the user sees

The generation dashboard has three error surfaces:

1. **Live log** — color-coded events (INFO green, WARN orange, ERROR red)
2. **Retry rate card** — percentage shows how often we're retrying; high rate = something wrong
3. **Error banner** — top of screen if a job is paused, cancelled, or critically failing

---

## 9. Quality — how we know the data is good

### Metrics we track per job

Every finished job produces a quality report with:

| Metric | What it means | Target |
|---|---|---|
| **Schema validity** | % of samples that matched the schema | ≥ 99% |
| **Judge pass rate** | % of samples the judge approved | ≥ 85% |
| **Dedup removal rate** | % of duplicates caught | 2-10% is normal |
| **Label distribution** | Count per label, flagged if imbalanced | Within 20% of target |
| **Avg text length** | Mean word count per sample | Depends on domain |
| **Unique word ratio** | Lexical diversity proxy | ≥ 0.3 |

### Mode collapse detection

If any of these trigger, we alert the user:
- 30%+ of samples share the same first 5 words
- Duplicate rate exceeds 20%
- Judge rejection exceeds 30%
- One label dominates by > 70%

### Preview before committing

Before firing the full job, user sees 20 sample rows generated as a preview. This catches:
- Schema misconfigurations
- Wrong tone
- Label confusion in seed examples

User can either "Generate full dataset" or "Go back and adjust."

---

## 10. The tech stack

### Backend
- **Python 3.11+** — main language
- **FastAPI** — REST API framework
- **Celery** — task queue for long-running jobs
- **Redis** — broker + cache
- **PostgreSQL 16** — projects, users, jobs, combination checkpoints
- **S3-compatible storage** — dataset files, exports

### AI / pipeline
- **LLM SDKs** — openai, anthropic, groq, boto3 (Bedrock), ollama-python
- **Pydantic v2** — schema validation
- **datasketch** — MinHash LSH deduplication
- **asyncio** — parallel LLM calls

### Frontend
- **Next.js 14** — App Router
- **React + TypeScript** — UI
- **Tailwind CSS** + **shadcn/ui** — styling
- **Recharts** — metrics dashboards
- **WebSocket** — live job progress

### Auth
- **Custom JWT** — no third-party auth service
- **AES-256 encryption** — API keys at rest
- **bcrypt** — password hashing

### Infra
- **Docker Compose** — local dev
- **Kubernetes** — production
- **OpenTelemetry + Grafana** — monitoring
- **Loki** — structured log aggregation

### Explicitly avoided
- **LiteLLM** — March 2026 PyPI compromise, don't trust the supply chain yet
- **Supabase** — custom auth for security control
- **Langchain in production** — used for experiments only; production engine uses direct SDK calls

---

## 11. What we cut and why

Reviewers suggested many features. Here's what we're intentionally **not** building in V1.

| Feature suggested | Why we're cutting from V1 |
|---|---|
| Multi-judge voting | Single judge with CoT is 95% as good at half the cost |
| Dynamic persona regeneration | Cached per project is fine; add "regenerate" button later |
| Stage 7 augmentation | Not needed at 100K ceiling |
| Embedding-based semantic dedup | MinHash covers 90% of the need at 10% of the cost |
| Downstream fine-tuning benchmarks | Huge scope, separate product |
| Dataset versioning | Snapshots only in V1; versioning in V2 |
| Axis correlation detection | Logic filter handles the worst cases; full MI analysis in V2 |
| Perplexity filters for augmentation | No augmentation in V1, so not needed |
| Multi-turn dialogue generation | Single-row only in V1 |
| Real-time generation API | Batch jobs only in V1 |

Each of these is a good idea, but none of them are needed to ship something valuable.

---

## 12. Success criteria

V1 is successful if:

### Functional success
- A user can go from signup to dataset download in under 30 minutes (for 1,000 sample job)
- Schema validity stays above 99% across all providers
- Dedup removal rate stays below 10% under normal conditions
- Jobs up to 100K samples complete reliably
- Crashes don't lose progress

### Product success
- 100 signups in the first month
- 50% of signups complete at least one generation job
- 20% of Free users upgrade to Pro within 30 days
- Mean time to first dataset < 20 minutes

### Technical success
- API response times under 200ms (non-generation calls)
- Job throughput: 50-100 samples/minute per worker
- Zero data loss on crash recovery
- Zero API key leaks (ever)

---

## Final summary

**V1 is scoped to do one thing exceptionally well:** generate up to 100,000 high-quality NLP training examples for any text domain, using the user's own AI provider, with a 6-stage pipeline that handles variety, validation, quality, and deduplication.

Everything else is deferred. The ceiling is clear. The failures have defined handlers. The quality is measurable.

This is what we're building.

---

*SynthData V1 Specification — April 2026*
*For engineers, reviewers, and anyone evaluating feasibility.*
