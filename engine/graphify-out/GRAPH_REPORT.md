# Graph Report - /Users/shashank/Desktop/shashank/codes/aiverse/engine  (2026-04-23)

## Corpus Check
- Corpus is ~9,928 words - fits in a single context window. You may not need a graph.

## Summary
- 243 nodes · 592 edges · 12 communities detected
- Extraction: 73% EXTRACTED · 27% INFERRED · 0% AMBIGUOUS · INFERRED: 160 edges (avg confidence: 0.66)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Provider Implementations|Provider Implementations]]
- [[_COMMUNITY_Core Pipeline Concepts & Docs|Core Pipeline Concepts & Docs]]
- [[_COMMUNITY_LLMProvider Interface & Axes Discovery|LLMProvider Interface & Axes Discovery]]
- [[_COMMUNITY_Prompt Composition & Persona Pool|Prompt Composition & Persona Pool]]
- [[_COMMUNITY_Dataset Schema & Validation|Dataset Schema & Validation]]
- [[_COMMUNITY_MinHash LSH Deduplication|MinHash LSH Deduplication]]
- [[_COMMUNITY_Prompt Assembly & Tests|Prompt Assembly & Tests]]
- [[_COMMUNITY_CLI Entry Point|CLI Entry Point]]
- [[_COMMUNITY_Allocation Planner & Tests|Allocation Planner & Tests]]
- [[_COMMUNITY_Module Init Files|Module Init Files]]
- [[_COMMUNITY_Project README|Project README]]
- [[_COMMUNITY_Providers Reference Docs|Providers Reference Docs]]

## God Nodes (most connected - your core abstractions)
1. `DatasetSchema` - 28 edges
2. `run_job()` - 18 edges
3. `LLMProvider` - 18 edges
4. `JobConfig` - 17 edges
5. `LLMResponse` - 17 edges
6. `compose_prompt()` - 12 edges
7. `OllamaProvider` - 11 edges
8. `_repair_json()` - 11 edges
9. `BedrockProvider` - 11 edges
10. `_kwargs()` - 10 edges

## Surprising Connections (you probably didn't know these)
- `_schema()` --calls--> `DatasetSchema`  [INFERRED]
  /Users/shashank/Desktop/shashank/codes/aiverse/engine/tests/test_compose.py → /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/schema.py
- `_schema()` --calls--> `SchemaField`  [INFERRED]
  /Users/shashank/Desktop/shashank/codes/aiverse/engine/tests/test_compose.py → /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/schema.py
- `_schema()` --calls--> `EnumValue`  [INFERRED]
  /Users/shashank/Desktop/shashank/codes/aiverse/engine/tests/test_compose.py → /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/schema.py
- `test_compose_includes_anti_seeds()` --calls--> `AntiSeed`  [INFERRED]
  /Users/shashank/Desktop/shashank/codes/aiverse/engine/tests/test_compose.py → /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/config.py
- `If label isn't in the combination, the generator should see all allowed values +` --uses--> `AntiSeed`  [INFERRED]
  /Users/shashank/Desktop/shashank/codes/aiverse/engine/tests/test_compose.py → /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/config.py

## Hyperedges (group relationships)
- **SynthData 6-Stage Generation Pipeline Flow** — stage1_axes_discovery, stage15_logic_filter, stage2_allocation_plan, stage34_prompt_composition, stage4_generation, stage5_judge, stage6_dedup [EXTRACTED 1.00]
- **Prompt Grounding Inputs (Domain Brief, Schema, Speaker Constraints, Seeds)** — concept_domain_brief, concept_enum_value_descriptions, concept_speaker_constraint, concept_anti_seeds, concept_seeds, concept_persona_pool [EXTRACTED 0.95]
- **Ollama Performance Constraints Disabling Advanced Stages** — provider_ollama, rationale_ollama_concurrency1, rationale_logic_filter_disabled_ollama, rationale_judge_disabled_ollama [EXTRACTED 0.95]

## Communities

### Community 0 - "Provider Implementations"
Cohesion: 0.1
Nodes (27): LLMResponse, Provider contract shared across Ollama / OpenAI / Anthropic / etc., _backoff(), BedrockCredentials, BedrockProvider, AWS Bedrock provider via the Converse API.  Uses `bedrock-runtime.converse` for, Run a single converse call in a thread (boto3 is sync)., Async wrapper around bedrock-runtime.converse with JSON repair + retries. (+19 more)

### Community 1 - "Core Pipeline Concepts & Docs"
Cohesion: 0.07
Nodes (44): 6-Stage Synthetic Data Generation Pipeline, Anti-Seeds (Negative Examples), Variation Axes (Categorical Dimensions), Axis Combination, Chain-of-Thought Quality Judge, Domain Brief, Per-Enum-Value Descriptions, JSON Repair Loop (+36 more)

### Community 2 - "LLMProvider Interface & Axes Discovery"
Cohesion: 0.12
Nodes (25): LLMProvider, from_env(), discover_axes(), Stage 1 — Axes discovery.  Given a domain brief + dataset purpose + schema + spe, Schema hint that includes enum value semantics when the user provided them., _rich_schema_hint(), flatten_samples(), generate_all() (+17 more)

### Community 3 - "Prompt Composition & Persona Pool"
Cohesion: 0.15
Nodes (27): BaseModel, build_persona_pool(), _build_rules(), Stage 3 — Prompt composer + persona pool.  Persona pool: cached per project. Eac, Compose per-field rules, inlining enum-value semantics when pinned., Return (system, user) for a single generation call., AntiSeed, DatasetConfig (+19 more)

### Community 4 - "Dataset Schema & Validation"
Cohesion: 0.17
Nodes (19): _at_least_one_string(), _check_type(), _enum_needs_values(), EnumValue, _normalize_values(), User-defined dataset schema.  The user declares the shape of their dataset (fiel, One allowed value for an enum field, with optional usage description., Just the allowed value strings, preserving order. (+11 more)

### Community 5 - "MinHash LSH Deduplication"
Cohesion: 0.23
Nodes (12): dedupe(), pick_text_fields(), _primary_text(), Stage 6 — MinHash LSH deduplication.  Catches near-duplicates (case / punctuatio, Concatenate the primary text fields for signature computation., Return (unique_samples, duplicates_removed_count)., Use string fields for dedup; fall back to all fields if none.      Skips enum fi, _tokens() (+4 more)

### Community 6 - "Prompt Assembly & Tests"
Cohesion: 0.38
Nodes (11): compose_prompt(), Shape hint embedded in prompts — type descriptors, not real values., _kwargs(), _schema(), test_compose_includes_anti_seeds(), test_compose_includes_persona(), test_compose_includes_speaker_block(), test_compose_injects_unique_seed() (+3 more)

### Community 7 - "CLI Entry Point"
Cohesion: 0.46
Nodes (6): main(), _print_summary(), CLI: `uv run synthdata run config.yaml`., Run a generation job from a YAML config., run(), _write_output()

### Community 8 - "Allocation Planner & Tests"
Cohesion: 0.46
Nodes (6): build_plan(), Split the target across combinations.      Overshoot by ~10% up front so dedup l, test_plan_hits_adjusted_target(), test_sampling_when_too_many_combinations(), test_sweet_spot_cap_when_few_combinations(), test_unique_combination_ids()

### Community 10 - "Module Init Files"
Cohesion: 1.0
Nodes (1): Accept list[str] or list[{name, description}] — normalize to EnumValue.

### Community 14 - "Project README"
Cohesion: 1.0
Nodes (1): SynthData Engine

### Community 15 - "Providers Reference Docs"
Cohesion: 1.0
Nodes (1): Providers Documentation

## Knowledge Gaps
- **32 isolated node(s):** `Run a generation job from a YAML config.`, `One allowed value for an enum field, with optional usage description.`, `Accept list[str] or list[{name, description}] — normalize to EnumValue.`, `Just the allowed value strings, preserving order.`, `Return (is_valid, list_of_errors).` (+27 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Module Init Files`** (1 nodes): `Accept list[str] or list[{name, description}] — normalize to EnumValue.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Project README`** (1 nodes): `SynthData Engine`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Providers Reference Docs`** (1 nodes): `Providers Documentation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `run_job()` connect `LLMProvider Interface & Axes Discovery` to `Provider Implementations`, `Prompt Composition & Persona Pool`, `MinHash LSH Deduplication`, `CLI Entry Point`, `Allocation Planner & Tests`?**
  _High betweenness centrality (0.110) - this node is a cross-community bridge._
- **Why does `DatasetSchema` connect `Prompt Composition & Persona Pool` to `LLMProvider Interface & Axes Discovery`, `Dataset Schema & Validation`, `Prompt Assembly & Tests`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Are the 22 inferred relationships involving `DatasetSchema` (e.g. with `If label isn't in the combination, the generator should see all allowed values +` and `Speakers`) actually correct?**
  _`DatasetSchema` has 22 INFERRED edges - model-reasoned connections that need verification._
- **Are the 12 inferred relationships involving `run_job()` (e.g. with `run()` and `.warmup()`) actually correct?**
  _`run_job()` has 12 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `LLMProvider` (e.g. with `JobResult` and `Orchestrates all 6 stages end-to-end.`) actually correct?**
  _`LLMProvider` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 14 inferred relationships involving `JobConfig` (e.g. with `DatasetSchema` and `SynthData engine — synthetic NLP dataset generation pipeline.`) actually correct?**
  _`JobConfig` has 14 INFERRED edges - model-reasoned connections that need verification._
- **Are the 15 inferred relationships involving `LLMResponse` (e.g. with `OllamaProvider` and `Ollama provider — async calls with JSON repair, refusal detection, and retries.`) actually correct?**
  _`LLMResponse` has 15 INFERRED edges - model-reasoned connections that need verification._