# Provider: AWS Bedrock (Recommended)

AWS Bedrock is the recommended provider — ~26× faster than local Ollama, higher quality output, and supports concurrent generation. Full pipeline at `target=10` runs in ~50 seconds.

---

## Setup

**Step 1 — Enable model access**

1. Log into the [AWS Console](https://console.aws.amazon.com)
2. Go to **Amazon Bedrock → Model access**
3. Request access for your chosen model (e.g. `google.gemma-3-27b-it`)
4. Approval is instant for most models

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

Create a `.env` file at the repo root:

```env
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=us-east-1
AWS_MODEL_ID=google.gemma-3-27b-it-qat-q8-0:2:2
```

The engine auto-loads this file — you don't need to copy it per project.

---

## Sample Config

```yaml
project:
  name: Support Ticket Classifier
  domain_brief: >
    Customer support tickets submitted via a fintech mobile app.
    Users report payment issues, account problems, and general product questions.

dataset:
  brief: Training data for a 5-class support ticket classifier.
  target_count: 100
  require_balanced: true
  diversity: high

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
        - name: payment_dispute
          description: Disputed or unrecognised transactions.
        - name: product_bug
          description: App crashes, broken features, unexpected behaviour.
        - name: general_support
          description: General how-to questions or product usage help.

seeds:
  - text: "Why was I charged twice for my subscription this month?"
    label: billing_inquiry
  - text: "I can't log in — it says my account is locked."
    label: account_security

provider:
  type: bedrock
  model: google.gemma-3-27b-it-qat-q8-0:2:2   # overrides AWS_MODEL_ID if set
  concurrency: 8
  timeout_seconds: 60

judge:
  enabled: true
  min_correctness: 7
  min_realism: 7
  min_distinctiveness: 7
  concurrency: 8

logic_filter:
  enabled: true
```

---

## Recommended Models (us-east-1)

| Model ID | Speed | Quality | Notes |
|---|---|---|---|
| `google.gemma-3-27b-it-qat-q8-0:2:2` | Fast | High | Tested baseline |
| `us.amazon.nova-pro-v1:0` | Fast | High | Strong reasoning |
| `anthropic.claude-3-5-haiku-20241022-v1:0` | Very fast | Very high | Higher cost |

To switch models without editing the config, update `AWS_MODEL_ID` in `.env`.

---

## Judge Model Override

Use a stronger model just for the quality judge while keeping a cheaper model for generation:

```yaml
provider:
  type: bedrock
  model: google.gemma-3-27b-it-qat-q8-0:2:2          # generation (fast, cheap)
  judge_model: anthropic.claude-3-5-haiku-20241022-v1:0   # judge (higher quality)
```

---

## Run

```bash
uv run synthdata configs/your_bedrock_config.yaml
```

---

## Performance Reference

| Target | Estimated time | Notes |
|---|---|---|
| 10 | ~50s | All 6 stages, concurrency=8 |
| 50 | ~60–64s | 5-class balanced |
| 100 | ~2–3 min | |
| 1,000 | ~5–10 min | |
| 100,000 | ~45–90 min | Throttle backoff kicks in automatically |

Bedrock parallelises natively at `concurrency=8`. `ThrottlingException` is handled with exponential backoff — no manual intervention needed.
