# Graph Report - /Users/shashank/Desktop/shashank/codes/aiverse  (2026-04-25)

## Corpus Check
- 29 files · ~125,273 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 318 nodes · 1007 edges · 13 communities detected
- Extraction: 47% EXTRACTED · 53% INFERRED · 0% AMBIGUOUS · INFERRED: 537 edges (avg confidence: 0.63)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]

## God Nodes (most connected - your core abstractions)
1. `LLMResponse` - 67 edges
2. `DebugWriter` - 55 edges
3. `DatasetSchema` - 55 edges
4. `JobConfig` - 37 edges
5. `run()` - 31 edges
6. `SchemaField` - 31 edges
7. `DatasetConfig` - 30 edges
8. `EnumValue` - 28 edges
9. `run_job()` - 26 edges
10. `ProviderConfig` - 24 edges

## Surprising Connections (you probably didn't know these)
- `test_enum_requires_values()` --calls--> `SchemaField`  [INFERRED]
  /Users/shashank/Desktop/shashank/codes/aiverse/engine/tests/test_schema.py → /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/schema.py
- `A negative example — text that must NEVER be generated, with the reason.` --uses--> `DatasetSchema`  [INFERRED]
  /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/config.py → /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/schema.py
- `Split the target across combinations.      Overshoot by ~10% up front so judge/d` --uses--> `DebugWriter`  [INFERRED]
  /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/stages/plan.py → /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/debug.py
- `Stage 6 — MinHash LSH deduplication.  Catches near-duplicates (case / punctuatio` --uses--> `DebugWriter`  [INFERRED]
  /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/stages/dedup.py → /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/debug.py
- `Concatenate the primary text fields for signature computation.` --uses--> `DebugWriter`  [INFERRED]
  /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/stages/dedup.py → /Users/shashank/Desktop/shashank/codes/aiverse/engine/src/synthdata_engine/debug.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.06
Nodes (51): LLMProvider, _backoff(), BedrockProvider, _classify_error(), from_env(), Run a single converse call in a thread (boto3 is sync)., Return (error_message, is_throttle). Inspects botocore ClientError codes., Longer backoff with jitter for rate-limit errors — gives AWS time to recover. (+43 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (25): LLMResponse, Provider contract shared across Ollama / OpenAI / Anthropic / etc., BedrockCredentials, AWS Bedrock provider via the Converse API.  Uses `bedrock-runtime.converse` for, _backoff(), _looks_like_refusal(), OllamaProvider, Ollama provider — async calls with JSON repair, refusal detection, and retries. (+17 more)

### Community 2 - "Community 2"
Cohesion: 0.18
Nodes (47): BaseModel, DatasetConfig, DedupConfig, JobConfig, JudgeConfig, LogicFilterConfig, ProjectConfig, ProviderConfig (+39 more)

### Community 3 - "Community 3"
Cohesion: 0.14
Nodes (22): _default_output(), _print_summary(), CLI: `uv run synthdata config.yaml`., Run a generation job from a YAML config., run(), _write_output(), cartesian(), filter_combinations() (+14 more)

### Community 4 - "Community 4"
Cohesion: 0.22
Nodes (21): apply_quality_gate(), compute_report(), FieldDistribution, QualityReport, _dataset_cfg(), _samples(), _schema(), test_gate_empty_input() (+13 more)

### Community 5 - "Community 5"
Cohesion: 0.14
Nodes (14): load_config(), _check_type(), _normalize_values(), User-defined dataset schema.  The user declares the shape of their dataset (fiel, Just the allowed value strings, preserving order., Return (is_valid, list_of_errors)., Shape hint embedded in prompts — type descriptors, not real values., _hr_schema() (+6 more)

### Community 6 - "Community 6"
Cohesion: 0.16
Nodes (17): build_plan(), Split the target across combinations.      Overshoot by ~10% up front so judge/d, With few combos and a large target, per-combo rises above SWEET_MAX to hit the t, 30 combos at 100K target: total must reach 100K, each combo handles ~3333., 500 combos at 100K target: total must reach 100K, each combo handles ~200., Even at extreme scale, no combo exceeds MAX_PER_COMBO., Total planned = floor(target * overshoot), not just target., When n * SWEET_MAX >= target, per-combo stays at or below SWEET_MAX. (+9 more)

### Community 7 - "Community 7"
Cohesion: 0.29
Nodes (14): compose_prompt(), Return (system, user) for a single generation call., AntiSeed, A negative example — text that must NEVER be generated, with the reason., _kwargs(), If label isn't in the combination, the generator should see all allowed values +, _schema(), test_compose_includes_anti_seeds() (+6 more)

### Community 8 - "Community 8"
Cohesion: 0.38
Nodes (12): judge_samples(), _cfg(), _PassAllProvider, _samples(), test_judge_disabled_returns_all_samples_unchanged(), test_judge_empty_input(), test_judge_fail_open_on_unparseable_response(), test_judge_passes_all_high_quality_samples() (+4 more)

### Community 9 - "Community 9"
Cohesion: 0.2
Nodes (12): dedupe(), pick_text_fields(), _primary_text(), Stage 6 — MinHash LSH deduplication.  Catches near-duplicates (case / punctuatio, Concatenate the primary text fields for signature computation., Return (unique_samples, duplicates_removed_count)., Use string fields for dedup; fall back to all fields if none.      Skips enum fi, _tokens() (+4 more)

### Community 10 - "Community 10"
Cohesion: 1.0
Nodes (0): 

### Community 11 - "Community 11"
Cohesion: 1.0
Nodes (1): Accept list[str] or list[{name, description}] — normalize to EnumValue.

### Community 12 - "Community 12"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **19 isolated node(s):** `With few combos and a large target, per-combo rises above SWEET_MAX to hit the t`, `30 combos at 100K target: total must reach 100K, each combo handles ~3333.`, `500 combos at 100K target: total must reach 100K, each combo handles ~200.`, `Even at extreme scale, no combo exceeds MAX_PER_COMBO.`, `Total planned = floor(target * overshoot), not just target.` (+14 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 10`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 11`** (1 nodes): `Accept list[str] or list[{name, description}] — normalize to EnumValue.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 12`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `LLMResponse` connect `Community 1` to `Community 8`, `Community 0`, `Community 2`, `Community 3`?**
  _High betweenness centrality (0.208) - this node is a cross-community bridge._
- **Why does `DebugWriter` connect `Community 0` to `Community 1`, `Community 2`, `Community 3`, `Community 6`, `Community 7`, `Community 8`, `Community 9`?**
  _High betweenness centrality (0.172) - this node is a cross-community bridge._
- **Why does `run_job()` connect `Community 0` to `Community 2`, `Community 3`, `Community 4`, `Community 5`, `Community 6`, `Community 8`, `Community 9`?**
  _High betweenness centrality (0.145) - this node is a cross-community bridge._
- **Are the 66 inferred relationships involving `LLMResponse` (e.g. with `_GoodProvider` and `_FailProvider`) actually correct?**
  _`LLMResponse` has 66 INFERRED edges - model-reasoned connections that need verification._
- **Are the 51 inferred relationships involving `DebugWriter` (e.g. with `_GoodProvider` and `_FailProvider`) actually correct?**
  _`DebugWriter` has 51 INFERRED edges - model-reasoned connections that need verification._
- **Are the 50 inferred relationships involving `DatasetSchema` (e.g. with `_GoodProvider` and `_FailProvider`) actually correct?**
  _`DatasetSchema` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Are the 35 inferred relationships involving `JobConfig` (e.g. with `_GoodProvider` and `_FailProvider`) actually correct?**
  _`JobConfig` has 35 INFERRED edges - model-reasoned connections that need verification._