# User Story — How SynthData Engine Works

> No code. No jargon. Just what actually happens, step by step, from your perspective.

---

## The Problem You're Solving

You want to build an AI that reads a piece of text and puts it into a category.

For example:
- Read a customer support ticket → decide if it's a **billing issue**, **security issue**, or **general question**
- Read a product review → decide if it's **positive**, **negative**, or **neutral**
- Read a job request → decide if the user wants to **create**, **edit**, or **delete** a job listing

To train that AI, you need **hundreds or thousands of example texts** — each one already labelled with the correct category.

Collecting those examples by hand takes weeks. Paying humans to write them is expensive. This engine does it for you in minutes.

---

## What You Do

Your job is simple: **write a config file** that describes what you need.

You tell the engine three things:

1. **What your product is** — who uses it, what they do, what context they're in
2. **What your data should look like** — what fields each example should have, and what the label categories are
3. **A few example rows** — just 1–3 real examples so the engine knows what quality looks like

That's it. Then you run one command and wait.

---

## What the Engine Does (In Plain English)

Once you run the command, the engine goes through six steps on your behalf. Here's exactly what's happening:

---

### Step 1 — It figures out the variety

**What you see:** A log line saying "axes discovered"

**What's actually happening:**

The engine reads your product description and asks the AI: *"What are all the different dimensions of variety in this domain?"*

For a support ticket tool, it might discover:
- How urgent the message sounds (urgent, mild, calm)
- How much detail the user gave (vague, detailed, minimal)
- What kind of user they are (business owner, regular customer, first-time user)
- What part of the product they're talking about (mobile app, web dashboard, billing)

These dimensions are called **axes**. The engine uses them to make sure your dataset isn't all the same type of message. You get variety.

---

### Step 2 — It removes nonsense combinations

**What you see:** A log line saying "logic filter done"

**What's actually happening:**

Some combinations of those dimensions don't make sense in real life. For example: *"a calm, patient user who is also using urgent language"* — that's contradictory.

The engine asks the AI to go through all possible combinations and remove the ones that would never realistically happen. This keeps generated examples grounded in reality.

---

### Step 3 — It makes a plan

**What you see:** A log line saying "stage2_plan"

**What's actually happening:**

The engine now knows all the realistic combinations of variety dimensions. It calculates how many examples to generate per combination so the final dataset hits your target number.

If you asked for 100 examples and there are 20 valid combinations, it plans to generate ~5 examples per combination. This ensures your dataset covers all the variety — not just the most obvious cases.

If you turned on `require_balanced: true`, it also guarantees every label category (billing, security, general support, etc.) gets represented. No category ends up with zero examples.

---

### Step 4 — It creates characters

**What you see:** A log line saying "stage3_compose" or "personas"

**What's actually happening:**

Before writing examples, the engine generates a pool of realistic "characters" — different types of people who might send these messages.

For a fintech app, these might be:
- *Maria, 34, small business owner who uses the app for payroll — tends to be direct and businesslike*
- *James, 22, first-time user who just downloaded the app — writes casually and gets confused easily*
- *Priya, 45, long-time customer who has had account issues before — detailed and slightly frustrated*

These personas make the generated text feel like it came from real, different people — not all from the same voice.

---

### Step 5 — It writes the examples

**What you see:** Progress ticks like `✓ 10 samples ok`, `✓ 20 samples ok`...

**What's actually happening:**

This is the main generation step. For each combination in the plan, the engine sends the AI a detailed brief:

- Here's what the product is
- Here's the type of user writing this message (the persona)
- Here's the combination of dimensions for this example (e.g. urgent tone + vague details + business owner + mobile app)
- Here's the label this example must have (e.g. `billing_inquiry`)
- Here are some real examples of what good looks like (your seeds)
- **Write one realistic example**

The AI writes the text. The engine checks that it came back in the right format with the right fields. If not, it tries again automatically.

This step runs in parallel — up to 8 examples being generated at the same time (for Bedrock), which is why it's fast.

---

### Step 6 — It checks the quality

**What you see:** A log line saying "judge passed / failed"

**What's actually happening:**

After generating each example, a second AI pass reads it and scores it on three things:

- **Correctness** — does the label actually match the text? (1–10)
- **Realism** — does this sound like something a real person would write? (1–10)
- **Distinctiveness** — is this example meaningfully different from the others? (1–10)

Any example scoring below 7 in any category gets thrown out. This is your quality gate.

---

### Step 7 — It removes near-duplicates

**What you see:** A log line saying "duplicates removed: X"

**What's actually happening:**

Sometimes the AI writes two examples that are basically the same sentence with a couple of words swapped. Those are useless for training.

The engine runs a similarity check across all examples and removes any that are too close to each other. It keeps the best version and discards the rest.

---

### The End — You Get Your Dataset

**What you see:** A summary table and an output file

```
│ Samples written         │ 100                              │
│ label                   │ billing: 22  security: 19  ...  │
│ text (chars)            │ min=89  avg=203  max=412         │
│ Judge passed / failed   │ 94 / 6                           │
│ Duplicates removed      │ 8                                │
│ Elapsed                 │ 63.2s                            │
│ Output                  │ out_20260426_125541.jsonl         │
```

You now have a `.jsonl` file (or `.csv` or `.json`) ready to feed into a model training pipeline.

---

## The Full Journey in One Picture

```
You write a config file
         ↓
Engine reads your domain description
         ↓
Step 1: Discovers variety dimensions (axes)
         ↓
Step 2: Removes impossible combinations
         ↓
Step 3: Plans how many examples per combination
         ↓
Step 4: Creates realistic personas (characters)
         ↓
Step 5: Writes the examples (in parallel, fast)
         ↓
Step 6: Quality judge scores each example → rejects low quality
         ↓
Step 7: Removes near-duplicates
         ↓
You get a clean, labelled dataset file
```

---

## What Makes a Good Config

The single most important thing you write is the **domain brief** — the paragraph that describes your product and users.

**Bad:**
```yaml
domain_brief: A customer support tool.
```

**Good:**
```yaml
domain_brief: >
  A mobile-first fintech app used by small business owners and individual
  consumers in Southeast Asia to manage payments, digital wallets, and
  business banking. Users contact support when they have payment disputes,
  account access problems, or questions about app features.
```

The more specific you are, the more realistic and useful your generated data will be. Everything else in the pipeline — the variety dimensions, the personas, the text style — flows from this description.

---

## Common Questions

**Do I need to write hundreds of examples myself?**
No. You need just 1–3 seed examples to show the engine what quality looks like. It generates the rest.

**What if a category ends up with no examples?**
Turn on `require_balanced: true` in your config. The engine guarantees every label category appears in the output.

**How do I know the quality is good?**
Turn on `judge: enabled: true`. A second AI pass reviews every example and rejects anything that isn't realistic or correctly labelled.

**Can I see what the engine is deciding at each step?**
Yes — run with `--debug-dir debug/run1`. It writes a detailed log file for every step showing exactly what was generated and why.

**What if my run gets interrupted?**
Use `--checkpoint-dir checkpoints/`. The engine saves progress as it goes and picks up exactly where it left off.
