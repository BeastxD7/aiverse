# Stage 4 — Generation

## Stats
- Attempted: 22
- Succeeded: 22
- Schema failed: 0
- Refusals: 0
- Errors: 0
- Retries: 0

---

## Sample 1 — `emotional_intensity=mild, writing_style=abbreviated, context=product_review, topic=work, speaker_type=sharing_joy` — **PASS**

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
- writing_style: abbreviated
- context: product_review
- topic: work
- speaker_type: sharing_joy
- Speaker persona: A recently engaged person enthusiastically sharing the news with family, filled with excitement.
- Unique seed: c817dda1

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.4s)
```
```json
{
  "text": "OMG I'm engaged!! He proposed last night and I'm still floating. So excited to marry my best friend.",
  "label": "happy",
  "confidence": 0.98,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "OMG I'm engaged!! He proposed last night and I'm still floating. So excited to marry my best friend.",
  "label": "happy",
  "confidence": 0.98,
  "source": "synthetic"
}
```


---

## Sample 2 — `emotional_intensity=mild, writing_style=abbreviated, context=product_review, topic=work, speaker_type=sharing_joy` — **PASS**

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
- writing_style: abbreviated
- context: product_review
- topic: work
- speaker_type: sharing_joy
- Speaker persona: A software developer frustrated with a bug, briefly describing the problem in a team chat.
- Unique seed: e8b5f871

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.9s)
```
```json
{
  "text": "Finally squashed that bug! Been fighting it all day, but it's done. Huge relief.",
  "label": "happy",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Finally squashed that bug! Been fighting it all day, but it's done. Huge relief.",
  "label": "happy",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 3 — `emotional_intensity=mild, writing_style=abbreviated, context=product_review, topic=work, speaker_type=sharing_joy` — **PASS**

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
- writing_style: abbreviated
- context: product_review
- topic: work
- speaker_type: sharing_joy
- Speaker persona: A receptionist confirming an appointment, polite and factual without any emotional content.
- Unique seed: b6c78315

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.9s)
```
```json
{
  "text": "Finally finished that huge project. So relieved it's over!",
  "label": "happy",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Finally finished that huge project. So relieved it's over!",
  "label": "happy",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 4 — `emotional_intensity=mild, writing_style=abbreviated, context=product_review, topic=work, speaker_type=sharing_joy` — **PASS**

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
- writing_style: abbreviated
- context: product_review
- topic: work
- speaker_type: sharing_joy
- Speaker persona: A retail worker expressing annoyance about a rude customer on a personal chat, using passive-aggression.
- Unique seed: 7dffa697

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.0s)
```
```json
{
  "text": "Ugh, someone just asked if we had a discount for buying *one* pair of socks. Like, seriously? Some people…",
  "label": "angry",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Ugh, someone just asked if we had a discount for buying *one* pair of socks. Like, seriously? Some people…",
  "label": "angry",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 5 — `emotional_intensity=mild, writing_style=abbreviated, context=product_review, topic=work, speaker_type=sharing_joy` — **PASS**

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
- writing_style: abbreviated
- context: product_review
- topic: work
- speaker_type: sharing_joy
- Speaker persona: A young parent happily sharing a milestone their child achieved on social media, with emojis.
- Unique seed: 2105ba41

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.0s)
```
```json
{
  "text": "My little one said 'mama' for the first time today 😭 So proud! It was the best moment ever. 🥰",
  "label": "happy",
  "confidence": 0.97,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "My little one said 'mama' for the first time today 😭 So proud! It was the best moment ever. 🥰",
  "label": "happy",
  "confidence": 0.97,
  "source": "synthetic"
}
```


---

## Sample 6 — `emotional_intensity=mild, writing_style=abbreviated, context=product_review, topic=work, speaker_type=sharing_joy` — **PASS**

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
- writing_style: abbreviated
- context: product_review
- topic: work
- speaker_type: sharing_joy
- Speaker persona: A travel agent providing flight information, strictly focused on details and logistics.
- Unique seed: 7c74ed25

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.1s)
```
```json
{
  "text": "Just booked Mrs. Davison's honeymoon flights to Fiji! She was SO excited, it made my day.",
  "label": "happy",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Just booked Mrs. Davison's honeymoon flights to Fiji! She was SO excited, it made my day.",
  "label": "happy",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 7 — `emotional_intensity=mild, writing_style=formal, context=customer_service, topic=work, speaker_type=neutral_message` — **PASS**

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
- writing_style: formal
- context: customer_service
- topic: work
- speaker_type: neutral_message
- Speaker persona: A person feeling overwhelmed with work, hinting at stress without explicitly complaining.
- Unique seed: 884e6334

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.4s)
```
```json
{
  "text": "I seem to be constantly catching up on things lately. It's a little difficult to stay focused when there's always another task waiting, but I'm managing. I just wish I had a bit more breathing room.",
  "label": "sad",
  "confidence": 0.78,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "I seem to be constantly catching up on things lately. It's a little difficult to stay focused when there's always another task waiting, but I'm managing. I just wish I had a bit more breathing room.",
  "label": "sad",
  "confidence": 0.78,
  "source": "synthetic"
}
```


---

## Sample 8 — `emotional_intensity=mild, writing_style=formal, context=customer_service, topic=work, speaker_type=neutral_message` — **PASS**

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
- writing_style: formal
- context: customer_service
- topic: work
- speaker_type: neutral_message
- Speaker persona: A frustrated gamer complaining about lag in an online game, using internet slang and sarcasm.
- Unique seed: 3771c5aa

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (2.4s)
```
```json
{
  "text": "Seriously? Another lag spike? I'm trying to clutch here, and my character just freezes. This is beyond frustrating, honestly. Like, pay to win is one thing, but pay to *not* have your game crash is a whole other level of ridiculous.",
  "label": "angry",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Seriously? Another lag spike? I'm trying to clutch here, and my character just freezes. This is beyond frustrating, honestly. Like, pay to win is one thing, but pay to *not* have your game crash is a whole other level of ridiculous.",
  "label": "angry",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 9 — `emotional_intensity=mild, writing_style=formal, context=customer_service, topic=work, speaker_type=neutral_message` — **PASS**

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
- writing_style: formal
- context: customer_service
- topic: work
- speaker_type: neutral_message
- Speaker persona: A frustrated gamer complaining about lag in an online game, using internet slang and sarcasm.
- Unique seed: 4e986463

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.7s)
```
```json
{
  "text": "Seriously? Another 200ms ping? I'm paying for fiber and playing like I'm on dial-up. This is ridiculous, my K/D is taking a nosedive because of this lag.",
  "label": "angry",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Seriously? Another 200ms ping? I'm paying for fiber and playing like I'm on dial-up. This is ridiculous, my K/D is taking a nosedive because of this lag.",
  "label": "angry",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 10 — `emotional_intensity=mild, writing_style=formal, context=customer_service, topic=work, speaker_type=neutral_message` — **PASS**

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
- writing_style: formal
- context: customer_service
- topic: work
- speaker_type: neutral_message
- Speaker persona: A librarian responding to a factual inquiry, maintaining a professional and neutral tone.
- Unique seed: 4daa7cbb

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.5s)
```
```json
{
  "text": "I was really hoping to find a first edition of that book, but I understand it’s quite rare. Still, I appreciate you checking the archives for me.",
  "label": "sad",
  "confidence": 0.78,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "I was really hoping to find a first edition of that book, but I understand it’s quite rare. Still, I appreciate you checking the archives for me.",
  "label": "sad",
  "confidence": 0.78,
  "source": "synthetic"
}
```


---

## Sample 11 — `emotional_intensity=moderate, writing_style=abbreviated, context=product_review, topic=purchase, speaker_type=expressing_sadness` — **PASS**

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
- writing_style: abbreviated
- context: product_review
- topic: purchase
- speaker_type: expressing_sadness
- Speaker persona: A young parent happily sharing a milestone their child achieved on social media, with emojis.
- Unique seed: ff784c73

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.4s)
```
```json
{
  "text": "Ugh, the stroller arrived damaged. Baby shower's tomorrow and now I'm scrambling. So frustrating!",
  "label": "angry",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Ugh, the stroller arrived damaged. Baby shower's tomorrow and now I'm scrambling. So frustrating!",
  "label": "angry",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 12 — `emotional_intensity=moderate, writing_style=abbreviated, context=product_review, topic=purchase, speaker_type=expressing_sadness` — **PASS**

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
- writing_style: abbreviated
- context: product_review
- topic: purchase
- speaker_type: expressing_sadness
- Speaker persona: A teenager expressing disappointment about a cancelled concert, using dramatic language.
- Unique seed: 5e5877cd

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.5s)
```
```json
{
  "text": "omg they cancelled the concert i was SO looking forward to. like, seriously? my whole summer was planned around that. i'm gonna be a wreck.",
  "label": "sad",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "omg they cancelled the concert i was SO looking forward to. like, seriously? my whole summer was planned around that. i'm gonna be a wreck.",
  "label": "sad",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 13 — `emotional_intensity=mild, writing_style=formal, context=customer_service, topic=work, speaker_type=neutral_message` — **PASS**

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
- writing_style: formal
- context: customer_service
- topic: work
- speaker_type: neutral_message
- Speaker persona: A software developer frustrated with a bug, briefly describing the problem in a team chat.
- Unique seed: e88bbdef

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.6s)
```
```json
{
  "text": "I've been staring at this error for the last three hours and I'm still no closer to figuring it out. It's incredibly frustrating when a seemingly simple change causes such a cascade of issues.",
  "label": "angry",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "I've been staring at this error for the last three hours and I'm still no closer to figuring it out. It's incredibly frustrating when a seemingly simple change causes such a cascade of issues.",
  "label": "angry",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 14 — `emotional_intensity=mild, writing_style=formal, context=customer_service, topic=work, speaker_type=neutral_message` — **PASS**

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
- writing_style: formal
- context: customer_service
- topic: work
- speaker_type: neutral_message
- Speaker persona: A data analyst reporting statistical findings, objective and devoid of emotional coloring.
- Unique seed: d5cd74b6

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.6s)
```
```json
{
  "text": "The latest data indicates a slight decrease in user engagement this quarter, which is a bit concerning given our projected growth targets. We'll need to investigate the underlying factors contributing to this trend.",
  "label": "out_of_scope",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "The latest data indicates a slight decrease in user engagement this quarter, which is a bit concerning given our projected growth targets. We'll need to investigate the underlying factors contributing to this trend.",
  "label": "out_of_scope",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 15 — `emotional_intensity=moderate, writing_style=abbreviated, context=product_review, topic=purchase, speaker_type=expressing_sadness` — **PASS**

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
- writing_style: abbreviated
- context: product_review
- topic: purchase
- speaker_type: expressing_sadness
- Speaker persona: A person feeling overwhelmed with work, hinting at stress without explicitly complaining.
- Unique seed: 2c3363bc

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.5s)
```
```json
{
  "text": "Just… a lot. Work's been crazy, and I ordered this hoping for a little treat, but now it's just another thing. Sigh.",
  "label": "sad",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Just… a lot. Work's been crazy, and I ordered this hoping for a little treat, but now it's just another thing. Sigh.",
  "label": "sad",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 16 — `emotional_intensity=moderate, writing_style=abbreviated, context=product_review, topic=purchase, speaker_type=expressing_sadness` — **PASS**

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
- writing_style: abbreviated
- context: product_review
- topic: purchase
- speaker_type: expressing_sadness
- Speaker persona: A receptionist confirming an appointment, polite and factual without any emotional content.
- Unique seed: b88e1f34

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.5s)
```
```json
{
  "text": "Ugh, the package arrived damaged. I was really looking forward to this and now I have to deal with returns. Just my luck.",
  "label": "sad",
  "confidence": 0.85,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Ugh, the package arrived damaged. I was really looking forward to this and now I have to deal with returns. Just my luck.",
  "label": "sad",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 17 — `emotional_intensity=moderate, writing_style=abbreviated, context=product_review, topic=purchase, speaker_type=expressing_sadness` — **PASS**

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
- writing_style: abbreviated
- context: product_review
- topic: purchase
- speaker_type: expressing_sadness
- Speaker persona: A person feeling anxious about an upcoming presentation, hinting at nervousness.
- Unique seed: 5b06bfcd

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.6s)
```
```json
{
  "text": "Ugh, I just ordered it and now I'm kinda panicking about the presentation next week. I hope it arrives in time and that I don't mess things up.",
  "label": "sad",
  "confidence": 0.78,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Ugh, I just ordered it and now I'm kinda panicking about the presentation next week. I hope it arrives in time and that I don't mess things up.",
  "label": "sad",
  "confidence": 0.78,
  "source": "synthetic"
}
```


---

## Sample 18 — `emotional_intensity=strong, writing_style=formal, context=personal_chat, topic=daily_life, speaker_type=expressing_sadness` — **PASS**

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
- writing_style: formal
- context: personal_chat
- topic: daily_life
- speaker_type: expressing_sadness
- Speaker persona: A person feeling down after a rejection, writing a melancholic message to a close friend.
- Unique seed: 15e51683

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.5s)
```
{"text": "I received the news today, and honestly, I'm just feeling incredibly disheartened. It was a long shot, I know, but I really had my hopes up for that position. I think I need some time to process this.", "label": "sad", "confidence": 0.85, "source": "synthetic"}
```
### Parsed Output
```json
{
  "text": "I received the news today, and honestly, I'm just feeling incredibly disheartened. It was a long shot, I know, but I really had my hopes up for that position. I think I need some time to process this.",
  "label": "sad",
  "confidence": 0.85,
  "source": "synthetic"
}
```


---

## Sample 19 — `emotional_intensity=strong, writing_style=formal, context=personal_chat, topic=daily_life, speaker_type=expressing_sadness` — **PASS**

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
- writing_style: formal
- context: personal_chat
- topic: daily_life
- speaker_type: expressing_sadness
- Speaker persona: A student relieved after finishing a project, expressing a sense of accomplishment.
- Unique seed: f3a990d6

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.5s)
```
```json
{
  "text": "I finally submitted the final project and honestly, a huge weight has been lifted. It feels incredible to be done, and I’m just so relieved to have that behind me now.",
  "label": "happy",
  "confidence": 0.92,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "I finally submitted the final project and honestly, a huge weight has been lifted. It feels incredible to be done, and I’m just so relieved to have that behind me now.",
  "label": "happy",
  "confidence": 0.92,
  "source": "synthetic"
}
```


---

## Sample 20 — `emotional_intensity=strong, writing_style=formal, context=personal_chat, topic=daily_life, speaker_type=expressing_sadness` — **PASS**

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
- writing_style: formal
- context: personal_chat
- topic: daily_life
- speaker_type: expressing_sadness
- Speaker persona: A person grieving a breakup, writing a short, raw message detailing their sadness.
- Unique seed: 3e432b64

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.7s)
```
```json
{
  "text": "I keep replaying everything in my head, wondering what I could have done differently. It feels like a part of me is just…gone now. I honestly don't know how I'm going to get through this.",
  "label": "sad",
  "confidence": 0.95,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "I keep replaying everything in my head, wondering what I could have done differently. It feels like a part of me is just…gone now. I honestly don't know how I'm going to get through this.",
  "label": "sad",
  "confidence": 0.95,
  "source": "synthetic"
}
```


---

## Sample 21 — `emotional_intensity=strong, writing_style=formal, context=personal_chat, topic=daily_life, speaker_type=expressing_sadness` — **PASS**

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
- writing_style: formal
- context: personal_chat
- topic: daily_life
- speaker_type: expressing_sadness
- Speaker persona: A college student venting to a friend about a difficult exam, using casual slang and exaggeration.
- Unique seed: e1c72fbc

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.7s)
```
```json
{
  "text": "Ugh, that exam just absolutely wrecked me. I seriously think I failed everything, and now my GPA is probably toast. I'm so bummed out, I just want to curl up in bed and disappear for a week.",
  "label": "sad",
  "confidence": 0.88,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "Ugh, that exam just absolutely wrecked me. I seriously think I failed everything, and now my GPA is probably toast. I'm so bummed out, I just want to curl up in bed and disappear for a week.",
  "label": "sad",
  "confidence": 0.88,
  "source": "synthetic"
}
```


---

## Sample 22 — `emotional_intensity=strong, writing_style=formal, context=personal_chat, topic=daily_life, speaker_type=expressing_sadness` — **PASS**

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
- writing_style: formal
- context: personal_chat
- topic: daily_life
- speaker_type: expressing_sadness
- Speaker persona: A musician overjoyed by positive feedback on their new song, sharing the comments.
- Unique seed: 6ecb7937

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

HARD RULES:
- "label" must be one of:
    * "happy" — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * "sad" — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * "angry" — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * "out_of_scope" — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- "confidence" must be between 0.7 and 1.0
- "source" must be one of:
    * "synthetic" — LLM-generated example (always this value)

Return JSON only — a single object matching the schema above.
```

### Raw LLM Response (1.7s)
```
```json
{
  "text": "I'm still reeling from the response to the new song. People are genuinely connecting with it, and I've received so many heartfelt messages about how it's helped them through difficult times. It's incredibly humbling and makes all the late nights worthwhile.",
  "label": "happy",
  "confidence": 0.95,
  "source": "synthetic"
}
```
```
### Parsed Output
```json
{
  "text": "I'm still reeling from the response to the new song. People are genuinely connecting with it, and I've received so many heartfelt messages about how it's helped them through difficult times. It's incredibly humbling and makes all the late nights worthwhile.",
  "label": "happy",
  "confidence": 0.95,
  "source": "synthetic"
}
```
