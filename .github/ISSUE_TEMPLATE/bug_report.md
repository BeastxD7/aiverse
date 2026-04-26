---
name: Bug report
about: Something broke during a generation run, config loading, or output validation
title: '[bug] '
labels: bug
assignees: ''

---

## What happened

A clear description of the bug. What did you expect, and what did you get instead?

## Config

Paste the relevant parts of your YAML config (remove any secrets):

```yaml
provider:
  type:        # ollama | bedrock
  model:
  concurrency:

dataset:
  target_count:
  require_balanced:

schema:
  fields:
    # ...
```

## Command

```bash
uv run synthdata configs/your_config.yaml --target 50
```

## Error output

Paste the full terminal output or error message:

```
# paste here
```

## Which stage failed?

- [ ] Stage 1 — axis discovery
- [ ] Stage 1.5 — logic filter
- [ ] Stage 2 — allocation plan
- [ ] Stage 3 — persona generation
- [ ] Stage 4 — generation
- [ ] Stage 5 — judge
- [ ] Stage 6 — dedup
- [ ] Quality report / output
- [ ] Config loading / validation
- [ ] Not sure

## Debug logs

If you ran with `--debug-dir`, paste or attach the relevant stage file (e.g. `05_generation.md`).

## Environment

- OS:
- Python version (`python --version`):
- Engine version / commit:
- Provider: `ollama` / `bedrock`
- Model:
