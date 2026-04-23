# Stage 1 — Axes Discovery

## System Prompt
```
You design synthetic-data generation plans for NLP fine-tuning.
Output strict JSON only.
```

## User Prompt
```
I'm generating a dataset for this domain:

PROJECT: Human Emotion Detector

DOMAIN BRIEF:
A text classification system that detects the primary emotion expressed in
short human-written messages. Messages come from everyday contexts: social
media posts, personal chat messages, customer service transcripts, product
reviews, and forum posts. The writer is always a human expressing or
describing their current emotional state or a recent experience.
Messages are typically 1-3 sentences, conversational in tone, and written
in the first person — though some are more indirect or restrained.


DATASET PURPOSE:
Training data for a 4-class emotion classifier. We need variety across
emotional intensity (mild to strong), writing style (casual to formal),
context (personal, professional, social media), and speaker demographics.
Include subtle and ambiguous cases — not every sad message says "I'm sad"
and not every angry message uses strong language. The out_of_scope class
captures messages that contain no clear sad/happy/angry signal: neutral
questions, informational statements, or mixed emotions that don't resolve
to one label.


SPEAKERS IN SCOPE (messages originate from these users):
- Person venting frustration or dissatisfaction about a situation or product
- Person sharing a joyful or positive experience (achievement, surprise, gratitude)
- Person expressing sadness, grief, disappointment, or loneliness
- Person writing a neutral or factual message with no clear emotional charge
SPEAKERS OUT OF SCOPE (NEVER generate a message from these):
- Automated bots or system-generated messages
- Formal business communications with no personal emotional content
- Song lyrics, poetry, or fictional narrative (not real personal expression)

SCHEMA FIELDS (with per-value semantics where declared):
- text (string) — A short human-written message (1-4 sentences) expressing or describing an emotion. First-person. Conversational. No quotes around the message.

- label (enum): The primary emotion expressed in the text
    * happy — Message expresses joy, excitement, relief, gratitude, pride, or contentment. The overall tone is clearly positive. Includes subtle cases like quiet satisfaction or pleasant surprise — not just exclamation-mark excitement.

    * sad — Message expresses sadness, grief, disappointment, loneliness, regret, or despair. Covers both direct ("I'm devastated") and indirect expressions ("I just don't see the point anymore"). Missing someone, losing something important, or feeling let down all count.

    * angry — Message expresses anger, frustration, irritation, resentment, or outrage. Ranges from mild annoyance ("this is so frustrating") to strong rage. Complaints about a specific injustice or betrayal also fall here when the dominant tone is anger rather than sadness.

    * out_of_scope — Message has no clear dominant emotion from the three above. Examples: neutral factual statements, questions with no emotional charge, mixed emotions that cancel out, ambiguous statements that could plausibly be any label. Use this when a human labeler would genuinely disagree on which of the three emotions applies.

- confidence (float in [0.7, 1.0]) — Labeling confidence. 1.0 = unmistakably clear label. 0.7 = genuine ambiguity — a reasonable person might pick a different label.

- source (enum): Origin of this training example
    * synthetic — LLM-generated example (always this value)

Identify the 3 to 6 independent DIMENSIONS (called "axes") that naturally vary in
this domain. For each axis, list 3 to 8 representative VALUES the axis can take.

HARD CONSTRAINTS:
- Good axes are orthogonal — changing one shouldn't force changing another.
- If you use a persona/user/speaker axis, draw ONLY from the SPEAKERS IN SCOPE above.
  Never include any out-of-scope speaker as a value, and never invent speaker
  types beyond what is listed.
- Do NOT use the dataset's output label as an axis unless it's a genuinely
  controllable input dimension (when in doubt, skip it).

Return JSON of the form:
{
  "axes": {
    "<axis_name>": ["val1", "val2", ...],
    ...
  }
}

No prose, no explanation — JSON only.
```

## Raw LLM Response
```
```json
{
  "axes": {
    "emotional_intensity": ["mild", "moderate", "strong"],
    "writing_style": ["casual", "conversational", "slightly_formal"],
    "context": ["social_media", "personal_chat", "customer_service", "product_review"],
    "topic": ["relationship", "work", "health", "daily_life", "finances"],
    "speaker_type": ["venting_frustration", "sharing_joy", "expressing_sadness", "neutral_message"],
    "indirectness": ["direct", "indirect", "restrained"]
  }
}
```
```

## Parsed Axes
```json
{
  "emotional_intensity": [
    "mild",
    "moderate",
    "strong"
  ],
  "writing_style": [
    "casual",
    "conversational",
    "slightly_formal"
  ],
  "context": [
    "social_media",
    "personal_chat",
    "customer_service",
    "product_review"
  ],
  "topic": [
    "relationship",
    "work",
    "health",
    "daily_life",
    "finances"
  ],
  "speaker_type": [
    "venting_frustration",
    "sharing_joy",
    "expressing_sadness",
    "neutral_message"
  ],
  "indirectness": [
    "direct",
    "indirect",
    "restrained"
  ]
}
```

## Stats
- Outcome: success
- Attempts: 1
- Duration: 2.5s
