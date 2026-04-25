# Stage 1.5 — Logic Filter

## Input
- Total combinations: 120
- Batch size: 25
- Batches: 5


## Batch 1 (combos 0–24)

### User Prompt
```
I have a list of axis-combinations below. For each one,
judge whether a realistic example could naturally exist with that combination.

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


Mark a combination as IMPLAUSIBLE only if it's contradictory, absurd, or
socially/emotionally incoherent (e.g. "report_harassment intent with cheerful tone").
When in doubt, keep it — we prefer variety over aggressive filtering.

Combinations (numbered):
0. {"emotional_intensity": "strong", "writing_style": "concise", "context": "social_media", "topic": "daily_life", "speaker_type": "expressing_sadness", "label": "out_of_scope", "source": "synthetic"}
1. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "personal_chat", "topic": "daily_life", "speaker_type": "expressing_sadness", "label": "happy", "source": "synthetic"}
2. {"emotional_intensity": "mild", "writing_style": "casual", "context": "personal_chat", "topic": "work", "speaker_type": "sharing_joy", "label": "angry", "source": "synthetic"}
3. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "customer_service", "topic": "relationship", "speaker_type": "sharing_joy", "label": "angry", "source": "synthetic"}
4. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "social_media", "topic": "health", "speaker_type": "expressing_sadness", "label": "out_of_scope", "source": "synthetic"}
5. {"emotional_intensity": "mild", "writing_style": "concise", "context": "product_review", "topic": "health", "speaker_type": "venting_frustration", "label": "angry", "source": "synthetic"}
6. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "product_review", "topic": "relationship", "speaker_type": "expressing_sadness", "label": "out_of_scope", "source": "synthetic"}
7. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "personal_chat", "topic": "work", "speaker_type": "venting_frustration", "label": "out_of_scope", "source": "synthetic"}
8. {"emotional_intensity": "strong", "writing_style": "concise", "context": "customer_service", "topic": "daily_life", "speaker_type": "venting_frustration", "label": "out_of_scope", "source": "synthetic"}
9. {"emotional_intensity": "strong", "writing_style": "casual", "context": "product_review", "topic": "purchase", "speaker_type": "expressing_sadness", "label": "sad", "source": "synthetic"}
10. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "social_media", "topic": "health", "speaker_type": "sharing_joy", "label": "happy", "source": "synthetic"}
11. {"emotional_intensity": "strong", "writing_style": "slightly_formal", "context": "customer_service", "topic": "work", "speaker_type": "venting_frustration", "label": "angry", "source": "synthetic"}
12. {"emotional_intensity": "moderate", "writing_style": "concise", "context": "personal_chat", "topic": "daily_life", "speaker_type": "venting_frustration", "label": "happy", "source": "synthetic"}
13. {"emotional_intensity": "mild", "writing_style": "casual", "context": "personal_chat", "topic": "daily_life", "speaker_type": "venting_frustration", "label": "angry", "source": "synthetic"}
14. {"emotional_intensity": "mild", "writing_style": "casual", "context": "personal_chat", "topic": "health", "speaker_type": "expressing_sadness", "label": "angry", "source": "synthetic"}
15. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "social_media", "topic": "daily_life", "speaker_type": "neutral_message", "label": "out_of_scope", "source": "synthetic"}
16. {"emotional_intensity": "mild", "writing_style": "concise", "context": "product_review", "topic": "relationship", "speaker_type": "neutral_message", "label": "out_of_scope", "source": "synthetic"}
17. {"emotional_intensity": "mild", "writing_style": "concise", "context": "product_review", "topic": "purchase", "speaker_type": "expressing_sadness", "label": "happy", "source": "synthetic"}
18. {"emotional_intensity": "strong", "writing_style": "casual", "context": "personal_chat", "topic": "purchase", "speaker_type": "sharing_joy", "label": "sad", "source": "synthetic"}
19. {"emotional_intensity": "strong", "writing_style": "slightly_formal", "context": "customer_service", "topic": "purchase", "speaker_type": "venting_frustration", "label": "sad", "source": "synthetic"}
20. {"emotional_intensity": "mild", "writing_style": "casual", "context": "personal_chat", "topic": "work", "speaker_type": "neutral_message", "label": "happy", "source": "synthetic"}
21. {"emotional_intensity": "strong", "writing_style": "slightly_formal", "context": "social_media", "topic": "daily_life", "speaker_type": "expressing_sadness", "label": "angry", "source": "synthetic"}
22. {"emotional_intensity": "mild", "writing_style": "concise", "context": "customer_service", "topic": "relationship", "speaker_type": "neutral_message", "label": "angry", "source": "synthetic"}
23. {"emotional_intensity": "strong", "writing_style": "concise", "context": "personal_chat", "topic": "work", "speaker_type": "sharing_joy", "label": "sad", "source": "synthetic"}
24. {"emotional_intensity": "strong", "writing_style": "concise", "context": "product_review", "topic": "purchase", "speaker_type": "expressing_sadness", "label": "happy", "source": "synthetic"}

Return JSON of the form:
{
  "keep": [<list of indices to KEEP>]
}

JSON only.
```

### Raw LLM Response
```
```json
{
  "keep": [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
}
```
```

### Result
- Outcome: success (1.9s)
- Kept: 24/25
- Removed:
  - {
  "emotional_intensity": "mild",
  "writing_style": "slightly_formal",
  "context": "personal_chat",
  "topic": "daily_life",
  "speaker_type": "expressing_sadness",
  "label": "happy",
  "source": "synthetic"
}


## Batch 2 (combos 25–49)

### User Prompt
```
I have a list of axis-combinations below. For each one,
judge whether a realistic example could naturally exist with that combination.

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


Mark a combination as IMPLAUSIBLE only if it's contradictory, absurd, or
socially/emotionally incoherent (e.g. "report_harassment intent with cheerful tone").
When in doubt, keep it — we prefer variety over aggressive filtering.

Combinations (numbered):
0. {"emotional_intensity": "strong", "writing_style": "casual", "context": "product_review", "topic": "purchase", "speaker_type": "expressing_sadness", "label": "happy", "source": "synthetic"}
1. {"emotional_intensity": "moderate", "writing_style": "concise", "context": "personal_chat", "topic": "health", "speaker_type": "sharing_joy", "label": "angry", "source": "synthetic"}
2. {"emotional_intensity": "mild", "writing_style": "concise", "context": "product_review", "topic": "work", "speaker_type": "sharing_joy", "label": "angry", "source": "synthetic"}
3. {"emotional_intensity": "moderate", "writing_style": "concise", "context": "customer_service", "topic": "purchase", "speaker_type": "neutral_message", "label": "out_of_scope", "source": "synthetic"}
4. {"emotional_intensity": "strong", "writing_style": "slightly_formal", "context": "customer_service", "topic": "relationship", "speaker_type": "neutral_message", "label": "sad", "source": "synthetic"}
5. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "customer_service", "topic": "work", "speaker_type": "venting_frustration", "label": "out_of_scope", "source": "synthetic"}
6. {"emotional_intensity": "mild", "writing_style": "casual", "context": "social_media", "topic": "work", "speaker_type": "expressing_sadness", "label": "angry", "source": "synthetic"}
7. {"emotional_intensity": "mild", "writing_style": "concise", "context": "social_media", "topic": "relationship", "speaker_type": "neutral_message", "label": "sad", "source": "synthetic"}
8. {"emotional_intensity": "strong", "writing_style": "concise", "context": "product_review", "topic": "daily_life", "speaker_type": "expressing_sadness", "label": "out_of_scope", "source": "synthetic"}
9. {"emotional_intensity": "moderate", "writing_style": "concise", "context": "personal_chat", "topic": "daily_life", "speaker_type": "venting_frustration", "label": "out_of_scope", "source": "synthetic"}
10. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "personal_chat", "topic": "health", "speaker_type": "venting_frustration", "label": "sad", "source": "synthetic"}
11. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "customer_service", "topic": "work", "speaker_type": "venting_frustration", "label": "angry", "source": "synthetic"}
12. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "product_review", "topic": "purchase", "speaker_type": "neutral_message", "label": "happy", "source": "synthetic"}
13. {"emotional_intensity": "mild", "writing_style": "concise", "context": "product_review", "topic": "relationship", "speaker_type": "venting_frustration", "label": "sad", "source": "synthetic"}
14. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "personal_chat", "topic": "work", "speaker_type": "venting_frustration", "label": "angry", "source": "synthetic"}
15. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "personal_chat", "topic": "work", "speaker_type": "venting_frustration", "label": "angry", "source": "synthetic"}
16. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "social_media", "topic": "daily_life", "speaker_type": "expressing_sadness", "label": "out_of_scope", "source": "synthetic"}
17. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "product_review", "topic": "health", "speaker_type": "sharing_joy", "label": "happy", "source": "synthetic"}
18. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "social_media", "topic": "purchase", "speaker_type": "neutral_message", "label": "happy", "source": "synthetic"}
19. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "customer_service", "topic": "work", "speaker_type": "neutral_message", "label": "angry", "source": "synthetic"}
20. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "personal_chat", "topic": "daily_life", "speaker_type": "venting_frustration", "label": "happy", "source": "synthetic"}
21. {"emotional_intensity": "strong", "writing_style": "slightly_formal", "context": "customer_service", "topic": "purchase", "speaker_type": "expressing_sadness", "label": "happy", "source": "synthetic"}
22. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "personal_chat", "topic": "health", "speaker_type": "expressing_sadness", "label": "out_of_scope", "source": "synthetic"}
23. {"emotional_intensity": "mild", "writing_style": "casual", "context": "customer_service", "topic": "work", "speaker_type": "venting_frustration", "label": "sad", "source": "synthetic"}
24. {"emotional_intensity": "moderate", "writing_style": "concise", "context": "product_review", "topic": "health", "speaker_type": "expressing_sadness", "label": "sad", "source": "synthetic"}

Return JSON of the form:
{
  "keep": [<list of indices to KEEP>]
}

JSON only.
```

### Raw LLM Response
```
```json
{
  "keep": [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24
  ]
}
```
```

### Result
- Outcome: success (3.0s)
- Kept: 25/25
- Removed:
  _(none)_


## Batch 3 (combos 50–74)

### User Prompt
```
I have a list of axis-combinations below. For each one,
judge whether a realistic example could naturally exist with that combination.

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


Mark a combination as IMPLAUSIBLE only if it's contradictory, absurd, or
socially/emotionally incoherent (e.g. "report_harassment intent with cheerful tone").
When in doubt, keep it — we prefer variety over aggressive filtering.

Combinations (numbered):
0. {"emotional_intensity": "strong", "writing_style": "casual", "context": "product_review", "topic": "health", "speaker_type": "sharing_joy", "label": "happy", "source": "synthetic"}
1. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "customer_service", "topic": "work", "speaker_type": "neutral_message", "label": "out_of_scope", "source": "synthetic"}
2. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "product_review", "topic": "work", "speaker_type": "neutral_message", "label": "angry", "source": "synthetic"}
3. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "social_media", "topic": "relationship", "speaker_type": "venting_frustration", "label": "angry", "source": "synthetic"}
4. {"emotional_intensity": "strong", "writing_style": "slightly_formal", "context": "social_media", "topic": "work", "speaker_type": "sharing_joy", "label": "sad", "source": "synthetic"}
5. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "product_review", "topic": "relationship", "speaker_type": "venting_frustration", "label": "happy", "source": "synthetic"}
6. {"emotional_intensity": "strong", "writing_style": "concise", "context": "social_media", "topic": "relationship", "speaker_type": "neutral_message", "label": "angry", "source": "synthetic"}
7. {"emotional_intensity": "strong", "writing_style": "slightly_formal", "context": "product_review", "topic": "daily_life", "speaker_type": "sharing_joy", "label": "sad", "source": "synthetic"}
8. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "customer_service", "topic": "health", "speaker_type": "expressing_sadness", "label": "sad", "source": "synthetic"}
9. {"emotional_intensity": "strong", "writing_style": "slightly_formal", "context": "personal_chat", "topic": "health", "speaker_type": "neutral_message", "label": "happy", "source": "synthetic"}
10. {"emotional_intensity": "mild", "writing_style": "concise", "context": "personal_chat", "topic": "purchase", "speaker_type": "venting_frustration", "label": "out_of_scope", "source": "synthetic"}
11. {"emotional_intensity": "mild", "writing_style": "casual", "context": "product_review", "topic": "health", "speaker_type": "neutral_message", "label": "happy", "source": "synthetic"}
12. {"emotional_intensity": "mild", "writing_style": "casual", "context": "customer_service", "topic": "work", "speaker_type": "expressing_sadness", "label": "out_of_scope", "source": "synthetic"}
13. {"emotional_intensity": "strong", "writing_style": "concise", "context": "personal_chat", "topic": "purchase", "speaker_type": "sharing_joy", "label": "happy", "source": "synthetic"}
14. {"emotional_intensity": "mild", "writing_style": "concise", "context": "product_review", "topic": "daily_life", "speaker_type": "sharing_joy", "label": "sad", "source": "synthetic"}
15. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "customer_service", "topic": "purchase", "speaker_type": "venting_frustration", "label": "sad", "source": "synthetic"}
16. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "social_media", "topic": "relationship", "speaker_type": "sharing_joy", "label": "angry", "source": "synthetic"}
17. {"emotional_intensity": "mild", "writing_style": "concise", "context": "product_review", "topic": "purchase", "speaker_type": "expressing_sadness", "label": "sad", "source": "synthetic"}
18. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "personal_chat", "topic": "relationship", "speaker_type": "neutral_message", "label": "sad", "source": "synthetic"}
19. {"emotional_intensity": "moderate", "writing_style": "concise", "context": "product_review", "topic": "work", "speaker_type": "venting_frustration", "label": "sad", "source": "synthetic"}
20. {"emotional_intensity": "strong", "writing_style": "concise", "context": "social_media", "topic": "health", "speaker_type": "expressing_sadness", "label": "out_of_scope", "source": "synthetic"}
21. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "customer_service", "topic": "daily_life", "speaker_type": "sharing_joy", "label": "angry", "source": "synthetic"}
22. {"emotional_intensity": "mild", "writing_style": "concise", "context": "social_media", "topic": "work", "speaker_type": "expressing_sadness", "label": "angry", "source": "synthetic"}
23. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "customer_service", "topic": "purchase", "speaker_type": "neutral_message", "label": "happy", "source": "synthetic"}
24. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "customer_service", "topic": "relationship", "speaker_type": "neutral_message", "label": "out_of_scope", "source": "synthetic"}

Return JSON of the form:
{
  "keep": [<list of indices to KEEP>]
}

JSON only.
```

### Raw LLM Response
```
```json
{
  "keep": [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24
  ]
}
```
```

### Result
- Outcome: success (2.3s)
- Kept: 25/25
- Removed:
  _(none)_


## Batch 4 (combos 75–99)

### User Prompt
```
I have a list of axis-combinations below. For each one,
judge whether a realistic example could naturally exist with that combination.

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


Mark a combination as IMPLAUSIBLE only if it's contradictory, absurd, or
socially/emotionally incoherent (e.g. "report_harassment intent with cheerful tone").
When in doubt, keep it — we prefer variety over aggressive filtering.

Combinations (numbered):
0. {"emotional_intensity": "mild", "writing_style": "concise", "context": "customer_service", "topic": "daily_life", "speaker_type": "expressing_sadness", "label": "angry", "source": "synthetic"}
1. {"emotional_intensity": "strong", "writing_style": "concise", "context": "customer_service", "topic": "work", "speaker_type": "expressing_sadness", "label": "sad", "source": "synthetic"}
2. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "personal_chat", "topic": "daily_life", "speaker_type": "sharing_joy", "label": "sad", "source": "synthetic"}
3. {"emotional_intensity": "strong", "writing_style": "concise", "context": "product_review", "topic": "purchase", "speaker_type": "expressing_sadness", "label": "angry", "source": "synthetic"}
4. {"emotional_intensity": "strong", "writing_style": "concise", "context": "customer_service", "topic": "purchase", "speaker_type": "neutral_message", "label": "out_of_scope", "source": "synthetic"}
5. {"emotional_intensity": "strong", "writing_style": "concise", "context": "personal_chat", "topic": "relationship", "speaker_type": "neutral_message", "label": "angry", "source": "synthetic"}
6. {"emotional_intensity": "mild", "writing_style": "casual", "context": "product_review", "topic": "daily_life", "speaker_type": "sharing_joy", "label": "happy", "source": "synthetic"}
7. {"emotional_intensity": "strong", "writing_style": "slightly_formal", "context": "product_review", "topic": "relationship", "speaker_type": "neutral_message", "label": "out_of_scope", "source": "synthetic"}
8. {"emotional_intensity": "strong", "writing_style": "concise", "context": "social_media", "topic": "health", "speaker_type": "expressing_sadness", "label": "happy", "source": "synthetic"}
9. {"emotional_intensity": "mild", "writing_style": "concise", "context": "social_media", "topic": "daily_life", "speaker_type": "neutral_message", "label": "happy", "source": "synthetic"}
10. {"emotional_intensity": "strong", "writing_style": "casual", "context": "product_review", "topic": "work", "speaker_type": "expressing_sadness", "label": "out_of_scope", "source": "synthetic"}
11. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "social_media", "topic": "health", "speaker_type": "expressing_sadness", "label": "angry", "source": "synthetic"}
12. {"emotional_intensity": "mild", "writing_style": "concise", "context": "social_media", "topic": "work", "speaker_type": "neutral_message", "label": "sad", "source": "synthetic"}
13. {"emotional_intensity": "moderate", "writing_style": "concise", "context": "product_review", "topic": "daily_life", "speaker_type": "sharing_joy", "label": "sad", "source": "synthetic"}
14. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "product_review", "topic": "health", "speaker_type": "venting_frustration", "label": "angry", "source": "synthetic"}
15. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "personal_chat", "topic": "purchase", "speaker_type": "venting_frustration", "label": "sad", "source": "synthetic"}
16. {"emotional_intensity": "strong", "writing_style": "concise", "context": "social_media", "topic": "daily_life", "speaker_type": "neutral_message", "label": "sad", "source": "synthetic"}
17. {"emotional_intensity": "strong", "writing_style": "concise", "context": "product_review", "topic": "work", "speaker_type": "venting_frustration", "label": "angry", "source": "synthetic"}
18. {"emotional_intensity": "strong", "writing_style": "slightly_formal", "context": "social_media", "topic": "health", "speaker_type": "expressing_sadness", "label": "sad", "source": "synthetic"}
19. {"emotional_intensity": "mild", "writing_style": "concise", "context": "product_review", "topic": "work", "speaker_type": "venting_frustration", "label": "out_of_scope", "source": "synthetic"}
20. {"emotional_intensity": "strong", "writing_style": "concise", "context": "product_review", "topic": "relationship", "speaker_type": "sharing_joy", "label": "happy", "source": "synthetic"}
21. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "social_media", "topic": "daily_life", "speaker_type": "venting_frustration", "label": "happy", "source": "synthetic"}
22. {"emotional_intensity": "mild", "writing_style": "casual", "context": "customer_service", "topic": "purchase", "speaker_type": "sharing_joy", "label": "sad", "source": "synthetic"}
23. {"emotional_intensity": "mild", "writing_style": "concise", "context": "product_review", "topic": "daily_life", "speaker_type": "expressing_sadness", "label": "angry", "source": "synthetic"}
24. {"emotional_intensity": "mild", "writing_style": "casual", "context": "personal_chat", "topic": "daily_life", "speaker_type": "venting_frustration", "label": "out_of_scope", "source": "synthetic"}

Return JSON of the form:
{
  "keep": [<list of indices to KEEP>]
}

JSON only.
```

### Raw LLM Response
```
```json
{
  "keep": [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24
  ]
}
```
```

### Result
- Outcome: success (2.3s)
- Kept: 25/25
- Removed:
  _(none)_


## Batch 5 (combos 100–119)

### User Prompt
```
I have a list of axis-combinations below. For each one,
judge whether a realistic example could naturally exist with that combination.

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


Mark a combination as IMPLAUSIBLE only if it's contradictory, absurd, or
socially/emotionally incoherent (e.g. "report_harassment intent with cheerful tone").
When in doubt, keep it — we prefer variety over aggressive filtering.

Combinations (numbered):
0. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "social_media", "topic": "relationship", "speaker_type": "neutral_message", "label": "happy", "source": "synthetic"}
1. {"emotional_intensity": "moderate", "writing_style": "concise", "context": "social_media", "topic": "health", "speaker_type": "expressing_sadness", "label": "out_of_scope", "source": "synthetic"}
2. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "personal_chat", "topic": "daily_life", "speaker_type": "expressing_sadness", "label": "happy", "source": "synthetic"}
3. {"emotional_intensity": "mild", "writing_style": "casual", "context": "product_review", "topic": "work", "speaker_type": "neutral_message", "label": "out_of_scope", "source": "synthetic"}
4. {"emotional_intensity": "mild", "writing_style": "concise", "context": "customer_service", "topic": "purchase", "speaker_type": "venting_frustration", "label": "happy", "source": "synthetic"}
5. {"emotional_intensity": "strong", "writing_style": "slightly_formal", "context": "personal_chat", "topic": "relationship", "speaker_type": "venting_frustration", "label": "out_of_scope", "source": "synthetic"}
6. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "social_media", "topic": "relationship", "speaker_type": "expressing_sadness", "label": "happy", "source": "synthetic"}
7. {"emotional_intensity": "mild", "writing_style": "concise", "context": "customer_service", "topic": "purchase", "speaker_type": "sharing_joy", "label": "angry", "source": "synthetic"}
8. {"emotional_intensity": "strong", "writing_style": "concise", "context": "personal_chat", "topic": "health", "speaker_type": "neutral_message", "label": "happy", "source": "synthetic"}
9. {"emotional_intensity": "strong", "writing_style": "casual", "context": "personal_chat", "topic": "health", "speaker_type": "neutral_message", "label": "happy", "source": "synthetic"}
10. {"emotional_intensity": "moderate", "writing_style": "concise", "context": "social_media", "topic": "work", "speaker_type": "sharing_joy", "label": "happy", "source": "synthetic"}
11. {"emotional_intensity": "strong", "writing_style": "concise", "context": "social_media", "topic": "purchase", "speaker_type": "expressing_sadness", "label": "sad", "source": "synthetic"}
12. {"emotional_intensity": "moderate", "writing_style": "concise", "context": "product_review", "topic": "health", "speaker_type": "sharing_joy", "label": "out_of_scope", "source": "synthetic"}
13. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "product_review", "topic": "work", "speaker_type": "expressing_sadness", "label": "sad", "source": "synthetic"}
14. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "personal_chat", "topic": "health", "speaker_type": "neutral_message", "label": "happy", "source": "synthetic"}
15. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "social_media", "topic": "daily_life", "speaker_type": "venting_frustration", "label": "angry", "source": "synthetic"}
16. {"emotional_intensity": "strong", "writing_style": "slightly_formal", "context": "social_media", "topic": "daily_life", "speaker_type": "expressing_sadness", "label": "out_of_scope", "source": "synthetic"}
17. {"emotional_intensity": "strong", "writing_style": "casual", "context": "product_review", "topic": "health", "speaker_type": "neutral_message", "label": "out_of_scope", "source": "synthetic"}
18. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "personal_chat", "topic": "health", "speaker_type": "sharing_joy", "label": "happy", "source": "synthetic"}
19. {"emotional_intensity": "strong", "writing_style": "slightly_formal", "context": "personal_chat", "topic": "purchase", "speaker_type": "expressing_sadness", "label": "angry", "source": "synthetic"}

Return JSON of the form:
{
  "keep": [<list of indices to KEEP>]
}

JSON only.
```

### Raw LLM Response
```
```json
{
  "keep": [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19
  ]
}
```
```

### Result
- Outcome: success (2.0s)
- Kept: 20/20
- Removed:
  _(none)_


## Summary
- Input: 120 combinations
- Kept: 119 combinations
- Removed: 1 combinations
