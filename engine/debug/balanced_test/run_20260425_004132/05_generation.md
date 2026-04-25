# Stage 4 — Generation

## Stats
- Attempted: 44
- Succeeded: 44
- Schema failed: 0
- Refusals: 0
- Errors: 0
- Retries: 0

---

## Sample 1 — `emotional_intensity=mild, writing_style=concise, context=personal_chat, topic=purchase, speaker_type=venting_frustration, label=out_of_scope, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: mild
- writing_style: concise
- context: personal_chat
- topic: purchase
- speaker_type: venting_frustration
- label: out_of_scope
- source: synthetic
- Speaker persona: A musician sharing a joyful update about a successful gig, enthusiastic and energetic.
- Unique seed: 0220c65b

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "out_of_scope" — meaning: Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.7s)
```
```json
{
  "text": "Honestly, the new guitar arrived with a slightly warped neck. It plays, but it's...off. I'm just trying to figure out the return process now.",
  "label": "out_of_scope",
  "confidence": 0.78,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Honestly, the new guitar arrived with a slightly warped neck. It plays, but it's...off. I'm just trying to figure out the return process now.",
  "label": "out_of_scope",
  "confidence": 0.78,
  "source": "synthetic"
}
```


---

## Sample 2 — `emotional_intensity=mild, writing_style=concise, context=personal_chat, topic=purchase, speaker_type=venting_frustration, label=out_of_scope, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: mild
- writing_style: concise
- context: personal_chat
- topic: purchase
- speaker_type: venting_frustration
- label: out_of_scope
- source: synthetic
- Speaker persona: A person feeling lonely after moving to a new city, writing with quiet sadness and self-reflection.
- Unique seed: 16309d0d

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "out_of_scope" — meaning: Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.1s)
```
```json
{
  "text": "Honestly, the new coffee machine is just…there. It makes coffee, fine. It doesn't exactly spark joy, you know?",
  "label": "out_of_scope",
  "confidence": 0.83,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Honestly, the new coffee machine is just…there. It makes coffee, fine. It doesn't exactly spark joy, you know?",
  "label": "out_of_scope",
  "confidence": 0.83,
  "source": "synthetic"
}
```


---

## Sample 3 — `emotional_intensity=mild, writing_style=concise, context=personal_chat, topic=purchase, speaker_type=venting_frustration, label=out_of_scope, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: mild
- writing_style: concise
- context: personal_chat
- topic: purchase
- speaker_type: venting_frustration
- label: out_of_scope
- source: synthetic
- Speaker persona: A lawyer neutrally summarizing case details, precise and formal but not overly emotional.
- Unique seed: 375bcbf0

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "out_of_scope" — meaning: Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.1s)
```
```json
{
  "text": "Regarding the recent transaction, the delivered item does not correspond to the specifications outlined in purchase order 789-B. I have documented the discrepancies for review.",
  "label": "out_of_scope",
  "confidence": 0.82,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Regarding the recent transaction, the delivered item does not correspond to the specifications outlined in purchase order 789-B. I have documented the discrepancies for review.",
  "label": "out_of_scope",
  "confidence": 0.82,
  "source": "synthetic"
}
```


---

## Sample 4 — `emotional_intensity=mild, writing_style=concise, context=personal_chat, topic=purchase, speaker_type=venting_frustration, label=out_of_scope, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: mild
- writing_style: concise
- context: personal_chat
- topic: purchase
- speaker_type: venting_frustration
- label: out_of_scope
- source: synthetic
- Speaker persona: A person feeling frustrated with slow internet service, complaining with mild irritation.
- Unique seed: 6e2c1fd7

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "out_of_scope" — meaning: Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.2s)
```
```json
{
  "text": "Seriously, the loading wheel is my new screensaver. I just want to pay for this thing and move on with my life.",
  "label": "out_of_scope",
  "confidence": 0.78,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Seriously, the loading wheel is my new screensaver. I just want to pay for this thing and move on with my life.",
  "label": "out_of_scope",
  "confidence": 0.78,
  "source": "synthetic"
}
```


---

## Sample 5 — `emotional_intensity=moderate, writing_style=concise, context=product_review, topic=health, speaker_type=expressing_sadness, label=sad, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: concise
- context: product_review
- topic: health
- speaker_type: expressing_sadness
- label: sad
- source: synthetic
- Speaker persona: A patient describing symptoms to a doctor via text, factual and slightly anxious.
- Unique seed: d7a0e54e

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "sad" — meaning: Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.3s)
```
```json
{
  "text": "My appetite's been completely gone since the diagnosis. It's not even hunger, just… a hollow feeling. Everything tastes like ash, and I can't seem to force myself to eat anything, even my favorite things.",
  "label": "sad",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "My appetite's been completely gone since the diagnosis. It's not even hunger, just… a hollow feeling. Everything tastes like ash, and I can't seem to force myself to eat anything, even my favorite things.",
  "label": "sad",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 6 — `emotional_intensity=mild, writing_style=concise, context=personal_chat, topic=purchase, speaker_type=venting_frustration, label=out_of_scope, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: mild
- writing_style: concise
- context: personal_chat
- topic: purchase
- speaker_type: venting_frustration
- label: out_of_scope
- source: synthetic
- Speaker persona: A person sharing a funny anecdote from their day, lighthearted and conversational.
- Unique seed: f1b18ac2

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "out_of_scope" — meaning: Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.4s)
```
```json
{
  "text": "They sent the wrong color, again. It’s…a whole thing with this online store and pastels. Honestly, it's more amusing than infuriating at this point.",
  "label": "out_of_scope",
  "confidence": 0.78,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "They sent the wrong color, again. It’s…a whole thing with this online store and pastels. Honestly, it's more amusing than infuriating at this point.",
  "label": "out_of_scope",
  "confidence": 0.78,
  "source": "synthetic"
}
```


---

## Sample 7 — `emotional_intensity=mild, writing_style=concise, context=personal_chat, topic=purchase, speaker_type=venting_frustration, label=out_of_scope, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: mild
- writing_style: concise
- context: personal_chat
- topic: purchase
- speaker_type: venting_frustration
- label: out_of_scope
- source: synthetic
- Speaker persona: A person expressing disappointment with a restaurant meal, specific and constructive criticism.
- Unique seed: 4d9f4f4e

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "out_of_scope" — meaning: Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.4s)
```
```json
{
  "text": "The scallop risotto was… interesting. Honestly, it tasted overwhelmingly of lemon zest, and not in a good way. It completely overpowered the seafood. Not what I expected for thirty dollars.",
  "label": "out_of_scope",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "The scallop risotto was… interesting. Honestly, it tasted overwhelmingly of lemon zest, and not in a good way. It completely overpowered the seafood. Not what I expected for thirty dollars.",
  "label": "out_of_scope",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 8 — `emotional_intensity=moderate, writing_style=concise, context=product_review, topic=health, speaker_type=expressing_sadness, label=sad, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: concise
- context: product_review
- topic: health
- speaker_type: expressing_sadness
- label: sad
- source: synthetic
- Speaker persona: A person sharing a funny anecdote from their day, lighthearted and conversational.
- Unique seed: 68fcadb0

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "sad" — meaning: Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.5s)
```
```json
{
  "text": "My grandma used to make this specific kind of apple pie every fall, and I tried to recreate it this year. It just…wasn't the same. It tasted fine, but it didn't *feel* like fall, you know?",
  "label": "sad",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "My grandma used to make this specific kind of apple pie every fall, and I tried to recreate it this year. It just…wasn't the same. It tasted fine, but it didn't *feel* like fall, you know?",
  "label": "sad",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 9 — `emotional_intensity=moderate, writing_style=concise, context=product_review, topic=health, speaker_type=expressing_sadness, label=sad, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: concise
- context: product_review
- topic: health
- speaker_type: expressing_sadness
- label: sad
- source: synthetic
- Speaker persona: A lawyer neutrally summarizing case details, precise and formal but not overly emotional.
- Unique seed: 5df21c4b

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "sad" — meaning: Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.5s)
```
```json
{
  "text": "The specialist said the results are inconclusive, but honestly, it feels like another door closing. I'd built up so much hope for a clear path forward.",
  "label": "sad",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "The specialist said the results are inconclusive, but honestly, it feels like another door closing. I'd built up so much hope for a clear path forward.",
  "label": "sad",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 10 — `emotional_intensity=moderate, writing_style=concise, context=product_review, topic=health, speaker_type=expressing_sadness, label=sad, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: concise
- context: product_review
- topic: health
- speaker_type: expressing_sadness
- label: sad
- source: synthetic
- Speaker persona: An artist sharing their latest creation on Instagram, proud and hopeful for feedback.
- Unique seed: b2188c90

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "sad" — meaning: Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.8s)
```
```json
{
  "text": "I tried to repot the orchid my grandmother gave me, and the roots just crumbled. It feels silly to be upset over a plant, but it was… a piece of her, you know? Now it's just dirt and broken stems.",
  "label": "sad",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "I tried to repot the orchid my grandmother gave me, and the roots just crumbled. It feels silly to be upset over a plant, but it was… a piece of her, you know? Now it's just dirt and broken stems.",
  "label": "sad",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 11 — `emotional_intensity=moderate, writing_style=concise, context=product_review, topic=health, speaker_type=expressing_sadness, label=sad, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: concise
- context: product_review
- topic: health
- speaker_type: expressing_sadness
- label: sad
- source: synthetic
- Speaker persona: A person feeling frustrated with slow internet service, complaining with mild irritation.
- Unique seed: 218fd369

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "sad" — meaning: Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.7s)
```
```json
{
  "text": "I was really hoping this new vitamin would help with my energy levels, but honestly, I just feel… flatter than before. It's not even physical tiredness, just a sort of grayness that settles in. Makes it hard to even enjoy my usual hobbies.",
  "label": "sad",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "I was really hoping this new vitamin would help with my energy levels, but honestly, I just feel… flatter than before. It's not even physical tiredness, just a sort of grayness that settles in. Makes it hard to even enjoy my usual hobbies.",
  "label": "sad",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 12 — `emotional_intensity=moderate, writing_style=slightly_formal, context=social_media, topic=daily_life, speaker_type=venting_frustration, label=happy, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: slightly_formal
- context: social_media
- topic: daily_life
- speaker_type: venting_frustration
- label: happy
- source: synthetic
- Speaker persona: A parent venting on a parenting forum about toddler tantrums, using exasperated but relatable language.
- Unique seed: 3a64f971

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "happy" — meaning: Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.5s)
```
```json
{
  "text": "Honestly, the sheer relief when the last tiny human was finally asleep was… substantial. I think I managed a full, uninterrupted sip of lukewarm coffee. It's the little victories, you know?",
  "label": "happy",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Honestly, the sheer relief when the last tiny human was finally asleep was… substantial. I think I managed a full, uninterrupted sip of lukewarm coffee. It's the little victories, you know?",
  "label": "happy",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 13 — `emotional_intensity=moderate, writing_style=slightly_formal, context=social_media, topic=daily_life, speaker_type=venting_frustration, label=happy, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: slightly_formal
- context: social_media
- topic: daily_life
- speaker_type: venting_frustration
- label: happy
- source: synthetic
- Speaker persona: A college student casually texting friends about a frustrating group project, using slang and sarcasm.
- Unique seed: ceb8a421

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "happy" — meaning: Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.4s)
```
{"text": "Okay, so my group finally submitted the project, and honestly, it's not a total disaster. I was expecting a complete train wreck, but it's...presentable? I'm just relieved it's over, tbh.", "label": "happy", "confidence": 0.78, "source": "synthetic"}
```
### Parsed Output
```json
{
  "text": "Okay, so my group finally submitted the project, and honestly, it's not a total disaster. I was expecting a complete train wreck, but it's...presentable? I'm just relieved it's over, tbh.",
  "label": "happy",
  "confidence": 0.78,
  "source": "synthetic"
}
```


---

## Sample 14 — `emotional_intensity=moderate, writing_style=slightly_formal, context=social_media, topic=daily_life, speaker_type=venting_frustration, label=happy, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: slightly_formal
- context: social_media
- topic: daily_life
- speaker_type: venting_frustration
- label: happy
- source: synthetic
- Speaker persona: A lawyer neutrally summarizing case details, precise and formal but not overly emotional.
- Unique seed: c077a9a8

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "happy" — meaning: Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.6s)
```
```json
{
  "text": "The preliminary injunction was granted this morning, which, frankly, is a relief. It’s not a final victory, of course, but it buys us the necessary time to present a more comprehensive case and avoids immediate disruption to our clients’ operations.",
  "label": "happy",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "The preliminary injunction was granted this morning, which, frankly, is a relief. It’s not a final victory, of course, but it buys us the necessary time to present a more comprehensive case and avoids immediate disruption to our clients’ operations.",
  "label": "happy",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 15 — `emotional_intensity=moderate, writing_style=concise, context=product_review, topic=health, speaker_type=expressing_sadness, label=sad, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: concise
- context: product_review
- topic: health
- speaker_type: expressing_sadness
- label: sad
- source: synthetic
- Speaker persona: A person politely requesting a refund for a defective product, assertive but respectful.
- Unique seed: e15d3e52

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "sad" — meaning: Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.8s)
```
```json
{
  "text": "I tried the sleep aid, hoping for just one night of real rest after weeks of this. It didn't do anything, and now I've just wasted a month's worth of my money. It feels silly to be upset about this, but I'm just… completely drained.",
  "label": "sad",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "I tried the sleep aid, hoping for just one night of real rest after weeks of this. It didn't do anything, and now I've just wasted a month's worth of my money. It feels silly to be upset about this, but I'm just… completely drained.",
  "label": "sad",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 16 — `emotional_intensity=moderate, writing_style=slightly_formal, context=social_media, topic=daily_life, speaker_type=venting_frustration, label=happy, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: slightly_formal
- context: social_media
- topic: daily_life
- speaker_type: venting_frustration
- label: happy
- source: synthetic
- Speaker persona: A dog owner sharing a heartwarming video of their pet, enthusiastic and filled with joy.
- Unique seed: a0fe7460

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "happy" — meaning: Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.7s)
```
```json
{
  "text": "Honestly, I wasn't expecting the peonies to bloom like this after the late frost. It's such a small thing, but seeing that burst of color feels like a little victory, a quiet reassurance that things can still be beautiful even when you least expect it.",
  "label": "happy",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Honestly, I wasn't expecting the peonies to bloom like this after the late frost. It's such a small thing, but seeing that burst of color feels like a little victory, a quiet reassurance that things can still be beautiful even when you least expect it.",
  "label": "happy",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 17 — `emotional_intensity=moderate, writing_style=slightly_formal, context=social_media, topic=daily_life, speaker_type=venting_frustration, label=happy, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: slightly_formal
- context: social_media
- topic: daily_life
- speaker_type: venting_frustration
- label: happy
- source: synthetic
- Speaker persona: A fan reacting to a sports team's victory, ecstatic and exuberant.
- Unique seed: bf67b368

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "happy" — meaning: Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.9s)
```
```json
{
  "text": "Honestly, I'm still buzzing from the game. It wasn't just the win, it was *how* they won – that last-minute penalty kick was absolutely audacious, and I think I temporarily lost my voice celebrating with everyone at the pub. A truly cathartic evening.",
  "label": "happy",
  "confidence": 0.91,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Honestly, I'm still buzzing from the game. It wasn't just the win, it was *how* they won – that last-minute penalty kick was absolutely audacious, and I think I temporarily lost my voice celebrating with everyone at the pub. A truly cathartic evening.",
  "label": "happy",
  "confidence": 0.91,
  "source": "synthetic"
}
```


---

## Sample 18 — `emotional_intensity=moderate, writing_style=casual, context=personal_chat, topic=daily_life, speaker_type=sharing_joy, label=sad, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: casual
- context: personal_chat
- topic: daily_life
- speaker_type: sharing_joy
- label: sad
- source: synthetic
- Speaker persona: A chef reviewing a new kitchen appliance, practical and focused on functionality.
- Unique seed: dd1105c5

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "sad" — meaning: Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.8s)
```
```json
{
  "text": "I tried making my grandmother's pierogi recipe today. It just...didn't taste like hers. It's silly, I know, it's just dough and potatoes, but a little bit of something feels lost now.",
  "label": "sad",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "I tried making my grandmother's pierogi recipe today. It just...didn't taste like hers. It's silly, I know, it's just dough and potatoes, but a little bit of something feels lost now.",
  "label": "sad",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 19 — `emotional_intensity=moderate, writing_style=casual, context=personal_chat, topic=daily_life, speaker_type=sharing_joy, label=sad, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: casual
- context: personal_chat
- topic: daily_life
- speaker_type: sharing_joy
- label: sad
- source: synthetic
- Speaker persona: A chef reviewing a new kitchen appliance, practical and focused on functionality.
- Unique seed: 38e6e0c6

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "sad" — meaning: Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.1s)
```
```json
{
  "text": "My grandmother used to make challah every Friday, and the smell would fill the whole house. I tried to follow her recipe today, but it just...didn't rise right. It feels silly to be so upset over bread, but it just reminded me she's not here to help anymore.",
  "label": "sad",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "My grandmother used to make challah every Friday, and the smell would fill the whole house. I tried to follow her recipe today, but it just...didn't rise right. It feels silly to be so upset over bread, but it just reminded me she's not here to help anymore.",
  "label": "sad",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 20 — `emotional_intensity=moderate, writing_style=casual, context=personal_chat, topic=daily_life, speaker_type=sharing_joy, label=sad, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: casual
- context: personal_chat
- topic: daily_life
- speaker_type: sharing_joy
- label: sad
- source: synthetic
- Speaker persona: An online gamer expressing rage after losing a match, using some strong language but not excessive.
- Unique seed: 63b95987

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "sad" — meaning: Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.2s)
```
```json
{
  "text": "My grandma always used to make these little knitted birds for everyone in the family, and I found the one she made me while cleaning out the attic. It's… just not the same without her to give me a new one every year, you know? Feels like a piece of her is gone all over again.",
  "label": "sad",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "My grandma always used to make these little knitted birds for everyone in the family, and I found the one she made me while cleaning out the attic. It's… just not the same without her to give me a new one every year, you know? Feels like a piece of her is gone all over again.",
  "label": "sad",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 21 — `emotional_intensity=moderate, writing_style=casual, context=personal_chat, topic=daily_life, speaker_type=sharing_joy, label=sad, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: casual
- context: personal_chat
- topic: daily_life
- speaker_type: sharing_joy
- label: sad
- source: synthetic
- Speaker persona: An employee expressing frustration with a company policy, cautiously worded and slightly passive-aggressive.
- Unique seed: 0a6165cd

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "sad" — meaning: Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.1s)
```
```json
{
  "text": "I spent the afternoon reorganizing my grandmother's old photos. It's silly, but looking at all those faces… it just made me realize how much time has passed and how many people aren't around anymore to share a memory with. It's a quiet kind of ache, I guess.",
  "label": "sad",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "I spent the afternoon reorganizing my grandmother's old photos. It's silly, but looking at all those faces… it just made me realize how much time has passed and how many people aren't around anymore to share a memory with. It's a quiet kind of ache, I guess.",
  "label": "sad",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 22 — `emotional_intensity=moderate, writing_style=slightly_formal, context=social_media, topic=daily_life, speaker_type=venting_frustration, label=happy, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: slightly_formal
- context: social_media
- topic: daily_life
- speaker_type: venting_frustration
- label: happy
- source: synthetic
- Speaker persona: A teenager expressing disappointment over a cancelled concert, using dramatic but typical teen language.
- Unique seed: 1fa6d702

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "happy" — meaning: Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.3s)
```
```json
{
  "text": "Okay, so my grandma finally figured out how to video call. It was a little glitchy, and she kept waving her phone at the ceiling, but honestly seeing her face just…brightened the whole day. It's the small wins, you know?",
  "label": "happy",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Okay, so my grandma finally figured out how to video call. It was a little glitchy, and she kept waving her phone at the ceiling, but honestly seeing her face just…brightened the whole day. It's the small wins, you know?",
  "label": "happy",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 23 — `emotional_intensity=moderate, writing_style=casual, context=personal_chat, topic=daily_life, speaker_type=sharing_joy, label=sad, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: casual
- context: personal_chat
- topic: daily_life
- speaker_type: sharing_joy
- label: sad
- source: synthetic
- Speaker persona: A dog owner sharing a heartwarming video of their pet, enthusiastic and filled with joy.
- Unique seed: 9707892b

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "sad" — meaning: Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.2s)
```
```json
{
  "text": "I spent the afternoon going through old photos of my grandmother, and it just hit me all over again that she’s really gone. It wasn't a sudden thing, she lived a long life, but it's the little everyday things I miss… her terrible jokes, the way she always smelled like cinnamon. It’s a quiet sadness, not overwhelming, but it’s there.",
  "label": "sad",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "I spent the afternoon going through old photos of my grandmother, and it just hit me all over again that she’s really gone. It wasn't a sudden thing, she lived a long life, but it's the little everyday things I miss… her terrible jokes, the way she always smelled like cinnamon. It’s a quiet sadness, not overwhelming, but it’s there.",
  "label": "sad",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 24 — `emotional_intensity=moderate, writing_style=casual, context=personal_chat, topic=daily_life, speaker_type=sharing_joy, label=sad, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: casual
- context: personal_chat
- topic: daily_life
- speaker_type: sharing_joy
- label: sad
- source: synthetic
- Speaker persona: A software engineer reporting a bug in a professional chat, concise and focused on technical details.
- Unique seed: 46082e9e

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "sad" — meaning: Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.5s)
```
```json
{
  "text": "I tried to recreate my grandmother's recipe for her plum cake, the one she always made for birthdays. It just…isn't the same. It tastes fine, I guess, but it doesn’t smell like her kitchen, you know? Feels pointless to even bother anymore.",
  "label": "sad",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "I tried to recreate my grandmother's recipe for her plum cake, the one she always made for birthdays. It just…isn't the same. It tastes fine, I guess, but it doesn’t smell like her kitchen, you know? Feels pointless to even bother anymore.",
  "label": "sad",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 25 — `emotional_intensity=mild, writing_style=slightly_formal, context=social_media, topic=daily_life, speaker_type=expressing_sadness, label=out_of_scope, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: mild
- writing_style: slightly_formal
- context: social_media
- topic: daily_life
- speaker_type: expressing_sadness
- label: out_of_scope
- source: synthetic
- Speaker persona: A software engineer reporting a bug in a professional chat, concise and focused on technical details.
- Unique seed: 8dd0bff9

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "out_of_scope" — meaning: Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.6s)
```
```json
{
  "text": "The integration tests are consistently failing on the staging server, specifically with the payment gateway. I've verified the API keys and the request parameters seem correct. Could someone with access double-check the server configuration?",
  "label": "out_of_scope",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "The integration tests are consistently failing on the staging server, specifically with the payment gateway. I've verified the API keys and the request parameters seem correct. Could someone with access double-check the server configuration?",
  "label": "out_of_scope",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 26 — `emotional_intensity=mild, writing_style=slightly_formal, context=social_media, topic=daily_life, speaker_type=expressing_sadness, label=out_of_scope, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: mild
- writing_style: slightly_formal
- context: social_media
- topic: daily_life
- speaker_type: expressing_sadness
- label: out_of_scope
- source: synthetic
- Speaker persona: A chef reviewing a new kitchen appliance, practical and focused on functionality.
- Unique seed: 7c2ad68a

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "out_of_scope" — meaning: Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.5s)
```
```json
{
  "text": "The new convection oven maintains temperature remarkably consistently, though the digital interface is less intuitive than I’d hoped. It seems well-built, but I’m still evaluating whether the added features justify the cost.",
  "label": "out_of_scope",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "The new convection oven maintains temperature remarkably consistently, though the digital interface is less intuitive than I’d hoped. It seems well-built, but I’m still evaluating whether the added features justify the cost.",
  "label": "out_of_scope",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 27 — `emotional_intensity=mild, writing_style=slightly_formal, context=social_media, topic=daily_life, speaker_type=expressing_sadness, label=out_of_scope, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: mild
- writing_style: slightly_formal
- context: social_media
- topic: daily_life
- speaker_type: expressing_sadness
- label: out_of_scope
- source: synthetic
- Speaker persona: A parent venting on a parenting forum about toddler tantrums, using exasperated but relatable language.
- Unique seed: a87bbd09

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "out_of_scope" — meaning: Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.6s)
```
```json
{
  "text": "Honestly, the sheer volume of tiny socks that end up behind the dryer is a physics problem I haven't the bandwidth to solve right now. It’s just… a lot.",
  "label": "out_of_scope",
  "confidence": 0.78,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Honestly, the sheer volume of tiny socks that end up behind the dryer is a physics problem I haven't the bandwidth to solve right now. It’s just… a lot.",
  "label": "out_of_scope",
  "confidence": 0.78,
  "source": "synthetic"
}
```


---

## Sample 28 — `emotional_intensity=mild, writing_style=slightly_formal, context=social_media, topic=daily_life, speaker_type=expressing_sadness, label=out_of_scope, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: mild
- writing_style: slightly_formal
- context: social_media
- topic: daily_life
- speaker_type: expressing_sadness
- label: out_of_scope
- source: synthetic
- Speaker persona: A chef reviewing a new kitchen appliance, practical and focused on functionality.
- Unique seed: 1a281067

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "out_of_scope" — meaning: Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.6s)
```
```json
{
  "text": "The new immersion blender arrived today. It handles pureeing root vegetables adequately, though the motor seems a bit strained with anything beyond soft fruits. I’ll need to assess its longevity with more frequent use.",
  "label": "out_of_scope",
  "confidence": 0.82,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "The new immersion blender arrived today. It handles pureeing root vegetables adequately, though the motor seems a bit strained with anything beyond soft fruits. I’ll need to assess its longevity with more frequent use.",
  "label": "out_of_scope",
  "confidence": 0.82,
  "source": "synthetic"
}
```


---

## Sample 29 — `emotional_intensity=strong, writing_style=concise, context=social_media, topic=relationship, speaker_type=neutral_message, label=angry, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: strong
- writing_style: concise
- context: social_media
- topic: relationship
- speaker_type: neutral_message
- label: angry
- source: synthetic
- Speaker persona: A grieving widow privately journaling her feelings, writing in fragmented sentences and raw emotion.
- Unique seed: 1a440adb

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "angry" — meaning: Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.5s)
```
```json
{
  "text": "He said he 'needed space.' Space? After everything? Like I'm some orbiting debris he can just discard when I become inconvenient. I burned years on that man.",
  "label": "angry",
  "confidence": 0.87,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "He said he 'needed space.' Space? After everything? Like I'm some orbiting debris he can just discard when I become inconvenient. I burned years on that man.",
  "label": "angry",
  "confidence": 0.87,
  "source": "synthetic"
}
```


---

## Sample 30 — `emotional_intensity=strong, writing_style=concise, context=social_media, topic=relationship, speaker_type=neutral_message, label=angry, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: strong
- writing_style: concise
- context: social_media
- topic: relationship
- speaker_type: neutral_message
- label: angry
- source: synthetic
- Speaker persona: A person politely requesting a refund for a defective product, assertive but respectful.
- Unique seed: ef7c15f5

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "angry" — meaning: Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.6s)
```
```json
{
  "text": "Honestly, I'm beyond irritated. They claimed the 'artisan' bread was baked fresh daily, but it tasted like it was a week old. A week! For that price, I expect better, and I expect truth in advertising.",
  "label": "angry",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Honestly, I'm beyond irritated. They claimed the 'artisan' bread was baked fresh daily, but it tasted like it was a week old. A week! For that price, I expect better, and I expect truth in advertising.",
  "label": "angry",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 31 — `emotional_intensity=mild, writing_style=slightly_formal, context=social_media, topic=daily_life, speaker_type=expressing_sadness, label=out_of_scope, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: mild
- writing_style: slightly_formal
- context: social_media
- topic: daily_life
- speaker_type: expressing_sadness
- label: out_of_scope
- source: synthetic
- Speaker persona: A volunteer expressing gratitude for donations to a cause, sincere and appreciative.
- Unique seed: 308dc8a8

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "out_of_scope" — meaning: Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.8s)
```
```json
{
  "text": "We are so grateful for the generous contributions received this week; it allows us to continue providing essential services, though the need unfortunately continues to grow with the changing economic climate.",
  "label": "out_of_scope",
  "confidence": 0.78,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "We are so grateful for the generous contributions received this week; it allows us to continue providing essential services, though the need unfortunately continues to grow with the changing economic climate.",
  "label": "out_of_scope",
  "confidence": 0.78,
  "source": "synthetic"
}
```


---

## Sample 32 — `emotional_intensity=strong, writing_style=concise, context=social_media, topic=relationship, speaker_type=neutral_message, label=angry, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: strong
- writing_style: concise
- context: social_media
- topic: relationship
- speaker_type: neutral_message
- label: angry
- source: synthetic
- Speaker persona: An employee expressing frustration with a company policy, cautiously worded and slightly passive-aggressive.
- Unique seed: 2c245ed1

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "angry" — meaning: Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.6s)
```
```json
{
  "text": "Honestly, the new ‘flexible’ work arrangements feel less about employee wellbeing and more like a cost-cutting measure thinly veiled in corporate speak. It’s…disappointing, to say the least.",
  "label": "angry",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Honestly, the new ‘flexible’ work arrangements feel less about employee wellbeing and more like a cost-cutting measure thinly veiled in corporate speak. It’s…disappointing, to say the least.",
  "label": "angry",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 33 — `emotional_intensity=strong, writing_style=concise, context=social_media, topic=relationship, speaker_type=neutral_message, label=angry, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: strong
- writing_style: concise
- context: social_media
- topic: relationship
- speaker_type: neutral_message
- label: angry
- source: synthetic
- Speaker persona: A book reviewer giving a neutral summary of a plot, analytical and objective.
- Unique seed: 5dbc0d0d

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "angry" — meaning: Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.5s)
```
```json
{
  "text": "He promised to handle the finances, and now I'm dealing with late notices and a ruined credit score. I'm beyond disappointed; it feels intentionally malicious.",
  "label": "angry",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "He promised to handle the finances, and now I'm dealing with late notices and a ruined credit score. I'm beyond disappointed; it feels intentionally malicious.",
  "label": "angry",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 34 — `emotional_intensity=strong, writing_style=concise, context=social_media, topic=relationship, speaker_type=neutral_message, label=angry, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: strong
- writing_style: concise
- context: social_media
- topic: relationship
- speaker_type: neutral_message
- label: angry
- source: synthetic
- Speaker persona: A volunteer expressing gratitude for donations to a cause, sincere and appreciative.
- Unique seed: a1f7440d

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "angry" — meaning: Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.6s)
```
```json
{
  "text": "I spent all weekend building that stupid shelf, following the instructions *exactly*, and it's still wobbly. It's like they actively try to make things impossible. Seriously considering just throwing the whole thing out the window.",
  "label": "angry",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "I spent all weekend building that stupid shelf, following the instructions *exactly*, and it's still wobbly. It's like they actively try to make things impossible. Seriously considering just throwing the whole thing out the window.",
  "label": "angry",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 35 — `emotional_intensity=mild, writing_style=concise, context=product_review, topic=daily_life, speaker_type=expressing_sadness, label=angry, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: mild
- writing_style: concise
- context: product_review
- topic: daily_life
- speaker_type: expressing_sadness
- label: angry
- source: synthetic
- Speaker persona: A person feeling frustrated with slow internet service, complaining with mild irritation.
- Unique seed: cff1289e

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "angry" — meaning: Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.6s)
```
```json
{
  "text": "Seriously, another buffering wheel? I'm paying for 'high speed' but I think my dial-up was faster. It's ridiculous how often this happens when I'm trying to actually *use* the internet.",
  "label": "angry",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Seriously, another buffering wheel? I'm paying for 'high speed' but I think my dial-up was faster. It's ridiculous how often this happens when I'm trying to actually *use* the internet.",
  "label": "angry",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 36 — `emotional_intensity=mild, writing_style=concise, context=product_review, topic=daily_life, speaker_type=expressing_sadness, label=angry, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: mild
- writing_style: concise
- context: product_review
- topic: daily_life
- speaker_type: expressing_sadness
- label: angry
- source: synthetic
- Speaker persona: A chef reviewing a new kitchen appliance, practical and focused on functionality.
- Unique seed: 96beb8bd

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "angry" — meaning: Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.5s)
```
```json
{
  "text": "Honestly, this immersion blender is a joke. It couldn't puree a ripe tomato without sputtering and leaving chunks. I've wasted perfectly good basil trying to salvage a pesto. Absolute garbage.",
  "label": "angry",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Honestly, this immersion blender is a joke. It couldn't puree a ripe tomato without sputtering and leaving chunks. I've wasted perfectly good basil trying to salvage a pesto. Absolute garbage.",
  "label": "angry",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 37 — `emotional_intensity=mild, writing_style=concise, context=product_review, topic=daily_life, speaker_type=expressing_sadness, label=angry, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: mild
- writing_style: concise
- context: product_review
- topic: daily_life
- speaker_type: expressing_sadness
- label: angry
- source: synthetic
- Speaker persona: A college student casually texting friends about a frustrating group project, using slang and sarcasm.
- Unique seed: 8767d194

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "angry" — meaning: Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.6s)
```
```json
{
  "text": "Seriously?! My group partner just sent *another* email at 3 AM asking for my section. Like, dude, get a grip. I'm starting to think they're doing this on purpose just to be chaotic.",
  "label": "angry",
  "confidence": 0.87,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Seriously?! My group partner just sent *another* email at 3 AM asking for my section. Like, dude, get a grip. I'm starting to think they're doing this on purpose just to be chaotic.",
  "label": "angry",
  "confidence": 0.87,
  "source": "synthetic"
}
```


---

## Sample 38 — `emotional_intensity=moderate, writing_style=concise, context=personal_chat, topic=daily_life, speaker_type=venting_frustration, label=out_of_scope, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: concise
- context: personal_chat
- topic: daily_life
- speaker_type: venting_frustration
- label: out_of_scope
- source: synthetic
- Speaker persona: An artist sharing their latest creation on Instagram, proud and hopeful for feedback.
- Unique seed: 4dd86914

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}
{"text": "They promised to fix the billing error weeks ago and it's STILL showing up on my account. Completely unacceptable.", "label": "angry", "confidence": 0.93, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "out_of_scope" — meaning: Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.3s)
```
```json
{
  "text": "Just finished uploading the new digital painting. Took ages to render, hope the colors translate okay on different screens.",
  "label": "out_of_scope",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Just finished uploading the new digital painting. Took ages to render, hope the colors translate okay on different screens.",
  "label": "out_of_scope",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 39 — `emotional_intensity=mild, writing_style=concise, context=product_review, topic=daily_life, speaker_type=expressing_sadness, label=angry, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: mild
- writing_style: concise
- context: product_review
- topic: daily_life
- speaker_type: expressing_sadness
- label: angry
- source: synthetic
- Speaker persona: A person expressing disappointment with a restaurant meal, specific and constructive criticism.
- Unique seed: b0025303

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "angry" — meaning: Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.7s)
```
```json
{
  "text": "They said the halibut was 'fresh catch of the day,' but it tasted like it had been swimming around in the freezer for a month. Seriously, my grandmother's cooking is more inventive and she's been gone twenty years.",
  "label": "angry",
  "confidence": 0.87,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "They said the halibut was 'fresh catch of the day,' but it tasted like it had been swimming around in the freezer for a month. Seriously, my grandmother's cooking is more inventive and she's been gone twenty years.",
  "label": "angry",
  "confidence": 0.87,
  "source": "synthetic"
}
```


---

## Sample 40 — `emotional_intensity=moderate, writing_style=concise, context=personal_chat, topic=daily_life, speaker_type=venting_frustration, label=out_of_scope, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: concise
- context: personal_chat
- topic: daily_life
- speaker_type: venting_frustration
- label: out_of_scope
- source: synthetic
- Speaker persona: A commuter complaining about a delayed train, using sarcastic humor and resignation.
- Unique seed: 028947b7

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "out_of_scope" — meaning: Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.4s)
```
```json
{
  "text": "Oh fantastic, another fifteen minute delay. Apparently a 'signal malfunction.'  I swear, this train has a personal vendetta against my punctuality.",
  "label": "out_of_scope",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Oh fantastic, another fifteen minute delay. Apparently a 'signal malfunction.'  I swear, this train has a personal vendetta against my punctuality.",
  "label": "out_of_scope",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 41 — `emotional_intensity=moderate, writing_style=concise, context=personal_chat, topic=daily_life, speaker_type=venting_frustration, label=out_of_scope, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: concise
- context: personal_chat
- topic: daily_life
- speaker_type: venting_frustration
- label: out_of_scope
- source: synthetic
- Speaker persona: A person feeling lonely after moving to a new city, writing with quiet sadness and self-reflection.
- Unique seed: 20dfd5af

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "out_of_scope" — meaning: Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.3s)
```
{"text": "Honestly, I spent the afternoon rearranging my bookshelf. It felt…productive, I guess. Still haven't met anyone here, and it's starting to feel normal.", "label": "out_of_scope", "confidence": 0.78, "source": "synthetic"}
```
### Parsed Output
```json
{
  "text": "Honestly, I spent the afternoon rearranging my bookshelf. It felt…productive, I guess. Still haven't met anyone here, and it's starting to feel normal.",
  "label": "out_of_scope",
  "confidence": 0.78,
  "source": "synthetic"
}
```


---

## Sample 42 — `emotional_intensity=moderate, writing_style=concise, context=personal_chat, topic=daily_life, speaker_type=venting_frustration, label=out_of_scope, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: concise
- context: personal_chat
- topic: daily_life
- speaker_type: venting_frustration
- label: out_of_scope
- source: synthetic
- Speaker persona: A teacher acknowledging a student’s improvement, encouraging and positive.
- Unique seed: e3ed9211

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "out_of_scope" — meaning: Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.6s)
```
```json
{
  "text": "Mark's really turning things around in math. He used to struggle so much, now he's actually participating. It's nice to see, but still a lot of work ahead for both of us.",
  "label": "out_of_scope",
  "confidence": 0.78,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Mark's really turning things around in math. He used to struggle so much, now he's actually participating. It's nice to see, but still a lot of work ahead for both of us.",
  "label": "out_of_scope",
  "confidence": 0.78,
  "source": "synthetic"
}
```


---

## Sample 43 — `emotional_intensity=moderate, writing_style=concise, context=personal_chat, topic=daily_life, speaker_type=venting_frustration, label=out_of_scope, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: moderate
- writing_style: concise
- context: personal_chat
- topic: daily_life
- speaker_type: venting_frustration
- label: out_of_scope
- source: synthetic
- Speaker persona: A chef reviewing a new kitchen appliance, practical and focused on functionality.
- Unique seed: b9f447d3

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "Anyone know if the downtown branch is open on Sundays?", "label": "out_of_scope", "confidence": 0.91, "source": "synthetic"}
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "out_of_scope" — meaning: Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.6s)
```
```json
{
  "text": "This immersion circulator is… fine. It holds temperature, which is the point, but the interface is needlessly complicated for basic sous vide. I expected more for the price.",
  "label": "out_of_scope",
  "confidence": 0.82,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "This immersion circulator is… fine. It holds temperature, which is the point, but the interface is needlessly complicated for basic sous vide. I expected more for the price.",
  "label": "out_of_scope",
  "confidence": 0.82,
  "source": "synthetic"
}
```


---

## Sample 44 — `emotional_intensity=mild, writing_style=concise, context=product_review, topic=daily_life, speaker_type=expressing_sadness, label=angry, source=synthetic` — **PASS**

### User Prompt
```
Generate ONE example matching this schema:

{
  "text": "string (A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.\n)",
  "label": "one of ['happy', 'sad', 'angry', 'out_of_scope']",
  "confidence": "float between 0.7 and 1.0",
  "source": "one of ['synthetic']"
}

CONTEXT FOR THIS SPECIFIC EXAMPLE:
- emotional_intensity: mild
- writing_style: concise
- context: product_review
- topic: daily_life
- speaker_type: expressing_sadness
- label: angry
- source: synthetic
- Speaker persona: A traveler sharing excitement about an upcoming vacation, using exclamation points and descriptive language.
- Unique seed: 9ed128ff

SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

REFERENCE EXAMPLES (for tone and shape only — DO NOT COPY):
{"text": "My dog passed away last night. The house feels so empty without him.", "label": "sad", "confidence": 0.97, "source": "synthetic"}
{"text": "Just got the promotion I've been working toward for two years. Still in shock honestly.", "label": "happy", "confidence": 0.95, "source": "synthetic"}

ANTI-EXAMPLES (DO NOT generate anything resembling these):
- "I feel happy and sad at the same time about leaving." — reason: Explicitly mixed emotions — no single dominant label, cannot be reliably classified.
- "The product ships in 3-5 business days." — reason: Automated / system message with no human emotional content.
- "Her eyes glistened with unshed tears as she watched him walk away." — reason: Fictional narrative prose, not a real personal expression from a human speaker.

DIVERSITY DIRECTIVE: Generate an UNUSUAL, VARIED example. Avoid the most obvious or generic expression. Vary sentence length, vocabulary, cultural context, or phrasing. Make this example as distinct as possible from a typical training sample.

HARD RULES:
- "label" must equal "angry" — meaning: Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

- "confidence" must be between 0.7 and 1.0
- "source" must equal "synthetic" — meaning: LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (9.9s)
```
```json
{
  "text": "Seriously? Another delayed flight. I specifically paid extra for a direct route and now I'm stuck with a connection in…Trenton? This isn't just inconvenient, it's a complete disregard for my time and money.",
  "label": "angry",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Seriously? Another delayed flight. I specifically paid extra for a direct route and now I'm stuck with a connection in…Trenton? This isn't just inconvenient, it's a complete disregard for my time and money.",
  "label": "angry",
  "confidence": 0.88,
  "source": "synthetic"
}
```
