# Stage 3+4 — Persona Pool & Prompt Composition

## Stage 3: Persona Pool

Generates a pool of diverse speaker personas before generation starts. Personas are used to vary the voice and perspective of generated examples.

**Input:** `cfg.dataset.persona_pool_size` (default 40), `cfg.project.speakers`, domain brief  
**Output:** `list[str]` — e.g. `["Sarah, HR manager at a 500-person fintech, tends to use formal language..."]`

Speakers constraint is injected: only in-scope speaker types appear. Out-of-scope types are explicitly forbidden in the prompt.

**File:** `engine/src/synthdata_engine/stages/compose.py` → `build_persona_pool()`

## Stage 4: Prompt Composition

`compose_prompt()` assembles the full generation prompt for a single combination. Called once per sample (or batch) at generation time.

### Inputs to the prompt

| Block | Source | Purpose |
|---|---|---|
| Domain brief | `cfg.project.domain_brief` | Grounds the LLM in the product context |
| Dataset brief | `cfg.dataset.brief` | Explains what kind of data we want |
| Schema | `cfg.dataset_schema` | Field names, types, enum values with descriptions |
| Rules | derived from combination | Pins the axes for this specific sample |
| Speaker block | `cfg.project.speakers` | In/out-of-scope constraint repeated per sample |
| Persona | random pick from pool | Varies author voice |
| Seeds | `cfg.seeds` | Positive examples showing correct format and style |
| Anti-seeds | `cfg.anti_seeds` | Negative examples the LLM must never replicate |

### Rules block

For each axis in the current combination, a rule line is injected:
- Enum field: `The field "label" MUST be exactly "create_jd". This means: HR wants to draft a BRAND NEW job description from scratch.`
- Non-enum field: `The value of "tone" MUST be "casual".`

This is where per-enum-value descriptions pay off — the LLM gets the semantic rationale, not just a string to copy.

### Anti-seeds block

```
ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "Hi, I'd like to apply for the senior engineer role..." → Candidate voice — candidates never use this product.
```

### File

`engine/src/synthdata_engine/stages/compose.py`
