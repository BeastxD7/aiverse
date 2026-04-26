# Provider: Ollama (Local / Offline)

Use Ollama when you need to run fully offline with no cloud provider or API key. All inference happens on your machine.

**Trade-off:** ~26× slower than Bedrock. Full pipeline at `target=10` takes ~22 minutes on an Apple M-series Mac.

---

## Setup

```bash
# Install Ollama
brew install ollama       # macOS
# or download from https://ollama.ai

# Pull a model
ollama pull gemma4:e4b

# Start the server
ollama serve
```

Ollama runs at `http://localhost:11434` by default.

---

## Sample Config

```yaml
project:
  name: Support Ticket Classifier
  domain_brief: >
    Customer support tickets submitted via a fintech mobile app.
    Users report payment issues, account problems, and general product questions.

dataset:
  brief: Training data for a 3-class support ticket classifier.
  target_count: 30
  require_balanced: true

schema:
  fields:
    - name: text
      type: string
      description: The support ticket text written by the customer.
    - name: label
      type: enum
      description: Support category for this ticket.
      values:
        - name: billing_inquiry
          description: Questions about charges, invoices, or payment amounts.
        - name: account_security
          description: Locked accounts, suspicious activity, password issues.
        - name: general_support
          description: General how-to questions or product usage help.

seeds:
  - text: "Why was I charged twice for my subscription this month?"
    label: billing_inquiry
  - text: "I can't log in — it says my account is locked."
    label: account_security

provider:
  type: ollama
  model: gemma4:e4b
  concurrency: 1          # must be 1 — Ollama serialises requests
  timeout_seconds: 300
  host: http://localhost:11434   # change if Ollama runs on a different port

judge:
  enabled: false          # disable to keep runtimes reasonable on local models

logic_filter:
  enabled: false          # disable to keep runtimes reasonable on local models
```

---

## Key Rules for Ollama

| Setting | Value | Why |
|---|---|---|
| `concurrency` | `1` | Ollama defaults to `NUM_PARALLEL=1` — concurrent requests queue and time out |
| `judge.enabled` | `false` | Each judge call is another ~60–90s model call — adds up fast |
| `logic_filter.enabled` | `false` | Same reason — adds LLM calls before generation even starts |
| `timeout_seconds` | `300` | Local models can take 60–90s per call; default 120s is too tight |

---

## Run

```bash
uv run synthdata configs/your_ollama_config.yaml
```

---

## Performance Reference

| Model | Target | Estimated time |
|---|---|---|
| `gemma4:e4b` (Apple M-series) | 10 | ~22 minutes |
| `gemma4:e4b` (Apple M-series) | 50 | ~90 minutes |

For faster local inference, consider a smaller quantised model or increase your machine's RAM allocation to Ollama.
