# Graph Report - /Users/shashank/Desktop/shashank/codes/aiverse/engine  (2026-04-25)

## Corpus Check
- 71 files · ~121,101 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 526 nodes · 1510 edges · 17 communities detected
- Extraction: 60% EXTRACTED · 40% INFERRED · 0% AMBIGUOUS · INFERRED: 598 edges (avg confidence: 0.64)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Pipeline Features & Changelog|Pipeline Features & Changelog]]
- [[_COMMUNITY_Provider Protocol & Contracts|Provider Protocol & Contracts]]
- [[_COMMUNITY_Prompt Composition & Personas|Prompt Composition & Personas]]
- [[_COMMUNITY_Bedrock Provider Implementation|Bedrock Provider Implementation]]
- [[_COMMUNITY_Logic Filter & Response Models|Logic Filter & Response Models]]
- [[_COMMUNITY_Pipeline Architecture & Concepts|Pipeline Architecture & Concepts]]
- [[_COMMUNITY_Emotion Detection Axes|Emotion Detection Axes]]
- [[_COMMUNITY_Allocation Planner|Allocation Planner]]
- [[_COMMUNITY_Quality Gate & Reporting|Quality Gate & Reporting]]
- [[_COMMUNITY_CLI Interface|CLI Interface]]
- [[_COMMUNITY_Deduplication Stage|Deduplication Stage]]
- [[_COMMUNITY_Compose Tests|Compose Tests]]
- [[_COMMUNITY_Schema Validation Tests|Schema Validation Tests]]
- [[_COMMUNITY_Schema Model|Schema Model]]
- [[_COMMUNITY_Prior Graph Snapshot|Prior Graph Snapshot]]
- [[_COMMUNITY_Enum Normalization|Enum Normalization]]
- [[_COMMUNITY_Providers Documentation|Providers Documentation]]

## God Nodes (most connected - your core abstractions)
1. `LLMResponse` - 72 edges
2. `DatasetSchema` - 60 edges
3. `DebugWriter` - 56 edges
4. `JobConfig` - 42 edges
5. `run()` - 33 edges
6. `SchemaField` - 32 edges
7. `DatasetConfig` - 31 edges
8. `EnumValue` - 29 edges
9. `run_job()` - 27 edges
10. `ProviderConfig` - 26 edges

## Surprising Connections (you probably didn't know these)
- `JudgeStats` --describes--> `Stage 5 — CoT Judge: correctness/realism/distinctiveness scoring`  [EXTRACTED]
  /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/stages/judge.py → docs/implementation/06-judge.md
- `undershoot_risk()` --describes--> `Stage 2 — Allocation Plan`  [EXTRACTED]
  /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/stages/plan.py → docs/implementation/03-allocation-plan.md
- `6-Stage Synthetic NLP Dataset Generation Pipeline` --references--> `Debug balanced_test: Stage 1.5 Logic Filter — 120 input combinations`  [INFERRED]
  README.md → debug/balanced_test/run_20260425_004132/02_logic_filter.md
- `Async Ollama wrapper with JSON-mode generation, repair, and backoff.` --uses--> `LLMResponse`  [INFERRED]
  /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/providers/ollama.py → /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/providers/base.py
- `Load the model into memory so the first real call isn't a cold start.` --uses--> `LLMResponse`  [INFERRED]
  /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/providers/ollama.py → /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/providers/base.py

## Hyperedges (group relationships)
- **SynthData 6-Stage Generation Pipeline Flow** — stage1_axes_discovery, stage15_logic_filter, stage2_allocation_plan, stage34_prompt_composition, stage4_generation, stage5_judge, stage6_dedup [EXTRACTED 1.00]
- **Prompt Grounding Inputs (Domain Brief, Schema, Speaker Constraints, Seeds)** — concept_domain_brief, concept_enum_value_descriptions, concept_speaker_constraint, concept_anti_seeds, concept_seeds, concept_persona_pool [EXTRACTED 0.95]

## Communities

### Community 0 - "Pipeline Features & Changelog"
Cohesion: 0.03
Nodes (77): Bedrock Throttle Detection + Exponential Backoff, v0.2.0 Breaking Changes (CLI syntax, output filename, thresholds), Checkpoint/Resume for Large Runs, Dynamic Allocation Planner (effective_max formula), Judge Model Override (provider.judge_model), Multi-Pass Backfill (up to 5 passes, escalating overshoot), quality.py: Quality Report Module, Per-Call Temperature Control (+69 more)

### Community 1 - "Provider Protocol & Contracts"
Cohesion: 0.08
Nodes (41): LLMProvider, Provider contract shared across Ollama / OpenAI / Anthropic / etc., from_env(), build_persona_pool(), _build_rules(), _fence(), _json(), make_run_dir() (+33 more)

### Community 2 - "Prompt Composition & Personas"
Cohesion: 0.14
Nodes (58): BaseModel, Stage 3 — Prompt composer + persona pool.  Persona pool: cached per project. Eac, Return (system, user) for a single generation call., Compose per-field rules, inlining enum-value semantics when pinned., Compose per-field rules, inlining enum-value semantics when pinned., Return (system, user) for a single generation call., AntiSeed, DatasetConfig (+50 more)

### Community 3 - "Bedrock Provider Implementation"
Cohesion: 0.07
Nodes (33): _backoff(), BedrockCredentials, BedrockProvider, _classify_error(), AWS Bedrock provider via the Converse API.  Uses `bedrock-runtime.converse` for, Run a single converse call in a thread (boto3 is sync)., Run a single converse call in a thread (boto3 is sync)., Return (error_message, is_throttle). Inspects botocore ClientError codes. (+25 more)

### Community 4 - "Logic Filter & Response Models"
Cohesion: 0.09
Nodes (19): LLMResponse, filter_combinations(), _BadJSONProvider, _combos(), _ErrorProvider, _KeepAllProvider, _KeepNoneProvider, Tests for Stage 1.5 — logic filter. (+11 more)

### Community 5 - "Pipeline Architecture & Concepts"
Cohesion: 0.07
Nodes (43): 6-Stage Synthetic Data Generation Pipeline, Anti-Seeds (Negative Examples), Variation Axes (Categorical Dimensions), Axis Combination, Chain-of-Thought Quality Judge, Domain Brief, Per-Enum-Value Descriptions, JSON Repair Loop (+35 more)

### Community 6 - "Emotion Detection Axes"
Cohesion: 0.09
Nodes (39): Axis: context (social_media/personal_chat/customer_service/product_review), Axis: emotional_intensity (mild/moderate/strong), Axis: indirectness (direct/indirect/restrained) — unique to test2, Axis: speaker_type (venting_frustration/sharing_joy/expressing_sadness/neutral_message), Axis: topic (work/relationships/health/hobbies/everyday_life), Axis: writing_style (casual/conversational/slightly_formal), Balanced Test — Axes Discovery (run_20260425_004132), Balanced Test — Persona Pool (run_20260425_004132) (+31 more)

### Community 7 - "Allocation Planner"
Cohesion: 0.14
Nodes (23): build_plan(), PlanRow, Stage 2 — Allocation planner.  Decide how many examples to generate per (valid), Split the target across combinations.      Overshoot by ~10% up front so dedup l, Split the target across combinations.      Overshoot by ~10% up front so judge/d, total_target(), undershoot_risk(), With few combos and a large target, per-combo rises above SWEET_MAX to hit the t (+15 more)

### Community 8 - "Quality Gate & Reporting"
Cohesion: 0.26
Nodes (22): apply_quality_gate(), compute_report(), FieldDistribution, Post-generation quality gates and distribution analytics.  Runs after Stage 6 (d, _dataset_cfg(), Tests for quality gate and distribution report., _samples(), _schema() (+14 more)

### Community 9 - "CLI Interface"
Cohesion: 0.25
Nodes (21): _default_output(), main(), _print_dry_run(), _print_summary(), CLI: `uv run synthdata config.yaml`., Run a generation job from a YAML config., Run a generation job from a YAML config., run() (+13 more)

### Community 10 - "Deduplication Stage"
Cohesion: 0.18
Nodes (15): dedupe(), pick_text_fields(), _primary_text(), Stage 6 — MinHash LSH deduplication.  Catches near-duplicates (case / punctuatio, Concatenate the primary text fields for signature computation., Concatenate the primary text fields for signature computation., Return (unique_samples, duplicates_removed_count)., Return (unique_samples, duplicates_removed_count). (+7 more)

### Community 11 - "Compose Tests"
Cohesion: 0.5
Nodes (10): compose_prompt(), _kwargs(), _schema(), test_compose_includes_anti_seeds(), test_compose_includes_persona(), test_compose_includes_speaker_block(), test_compose_injects_unique_seed(), test_compose_lists_enum_values_when_not_pinned() (+2 more)

### Community 12 - "Schema Validation Tests"
Cohesion: 0.41
Nodes (9): Return (is_valid, list_of_errors)., _hr_schema(), test_bad_enum(), test_duplicate_field_names_rejected(), test_enum_requires_values(), test_extra_fields_flagged(), test_missing_field(), test_out_of_range_float() (+1 more)

### Community 13 - "Schema Model"
Cohesion: 0.25
Nodes (7): _at_least_one_string(), _check_type(), _enum_needs_values(), _normalize_values(), User-defined dataset schema.  The user declares the shape of their dataset (fiel, Just the allowed value strings, preserving order., Shape hint embedded in prompts — type descriptors, not real values.

### Community 14 - "Prior Graph Snapshot"
Cohesion: 0.67
Nodes (3): 12 Graph Communities Detected, God Nodes: DatasetSchema(28), run_job(18), LLMProvider(18), GRAPH_REPORT: 243 nodes, 592 edges, 12 communities

### Community 16 - "Enum Normalization"
Cohesion: 1.0
Nodes (1): Accept list[str] or list[{name, description}] — normalize to EnumValue.

### Community 20 - "Providers Documentation"
Cohesion: 1.0
Nodes (1): Providers Documentation

## Knowledge Gaps
- **77 isolated node(s):** `Run a generation job from a YAML config.`, `One allowed value for an enum field, with optional usage description.`, `Accept list[str] or list[{name, description}] — normalize to EnumValue.`, `Just the allowed value strings, preserving order.`, `Return (is_valid, list_of_errors).` (+72 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Enum Normalization`** (1 nodes): `Accept list[str] or list[{name, description}] — normalize to EnumValue.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Providers Documentation`** (1 nodes): `Providers Documentation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Stage 5 — CoT Judge: correctness/realism/distinctiveness scoring` connect `Pipeline Features & Changelog` to `Provider Protocol & Contracts`?**
  _High betweenness centrality (0.302) - this node is a cross-community bridge._
- **Why does `JudgeStats` connect `Provider Protocol & Contracts` to `Pipeline Features & Changelog`, `CLI Interface`, `Prompt Composition & Personas`?**
  _High betweenness centrality (0.290) - this node is a cross-community bridge._
- **Are the 70 inferred relationships involving `LLMResponse` (e.g. with `OllamaProvider` and `.generate_json()`) actually correct?**
  _`LLMResponse` has 70 INFERRED edges - model-reasoned connections that need verification._
- **Are the 54 inferred relationships involving `DatasetSchema` (e.g. with `_schema()` and `If label isn't in the combination, the generator should see all allowed values +`) actually correct?**
  _`DatasetSchema` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Are the 51 inferred relationships involving `DebugWriter` (e.g. with `JobResult` and `run_job()`) actually correct?**
  _`DebugWriter` has 51 INFERRED edges - model-reasoned connections that need verification._
- **Are the 39 inferred relationships involving `JobConfig` (e.g. with `DatasetSchema` and `SynthData engine — synthetic NLP dataset generation pipeline.`) actually correct?**
  _`JobConfig` has 39 INFERRED edges - model-reasoned connections that need verification._
- **Are the 26 inferred relationships involving `run()` (e.g. with `load_config()` and `run_job()`) actually correct?**
  _`run()` has 26 INFERRED edges - model-reasoned connections that need verification._