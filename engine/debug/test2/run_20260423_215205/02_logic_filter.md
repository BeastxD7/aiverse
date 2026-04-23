# Stage 1.5 — Logic Filter

## Input
- Total combinations: 100
- Batch size: 25
- Batches: 4


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
0. {"emotional_intensity": "mild", "writing_style": "conversational", "context": "product_review", "topic": "daily_life", "speaker_type": "venting_frustration", "indirectness": "direct"}
1. {"emotional_intensity": "mild", "writing_style": "casual", "context": "personal_chat", "topic": "daily_life", "speaker_type": "expressing_sadness", "indirectness": "direct"}
2. {"emotional_intensity": "moderate", "writing_style": "conversational", "context": "customer_service", "topic": "daily_life", "speaker_type": "neutral_message", "indirectness": "indirect"}
3. {"emotional_intensity": "moderate", "writing_style": "conversational", "context": "social_media", "topic": "daily_life", "speaker_type": "expressing_sadness", "indirectness": "indirect"}
4. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "product_review", "topic": "work", "speaker_type": "venting_frustration", "indirectness": "restrained"}
5. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "personal_chat", "topic": "health", "speaker_type": "expressing_sadness", "indirectness": "indirect"}
6. {"emotional_intensity": "mild", "writing_style": "conversational", "context": "customer_service", "topic": "finances", "speaker_type": "neutral_message", "indirectness": "restrained"}
7. {"emotional_intensity": "mild", "writing_style": "conversational", "context": "personal_chat", "topic": "finances", "speaker_type": "expressing_sadness", "indirectness": "restrained"}
8. {"emotional_intensity": "strong", "writing_style": "conversational", "context": "social_media", "topic": "finances", "speaker_type": "venting_frustration", "indirectness": "direct"}
9. {"emotional_intensity": "mild", "writing_style": "casual", "context": "customer_service", "topic": "relationship", "speaker_type": "neutral_message", "indirectness": "indirect"}
10. {"emotional_intensity": "mild", "writing_style": "casual", "context": "customer_service", "topic": "relationship", "speaker_type": "venting_frustration", "indirectness": "restrained"}
11. {"emotional_intensity": "mild", "writing_style": "conversational", "context": "customer_service", "topic": "work", "speaker_type": "neutral_message", "indirectness": "restrained"}
12. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "customer_service", "topic": "finances", "speaker_type": "expressing_sadness", "indirectness": "indirect"}
13. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "product_review", "topic": "finances", "speaker_type": "sharing_joy", "indirectness": "indirect"}
14. {"emotional_intensity": "strong", "writing_style": "slightly_formal", "context": "customer_service", "topic": "health", "speaker_type": "sharing_joy", "indirectness": "restrained"}
15. {"emotional_intensity": "mild", "writing_style": "casual", "context": "personal_chat", "topic": "finances", "speaker_type": "venting_frustration", "indirectness": "direct"}
16. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "personal_chat", "topic": "health", "speaker_type": "neutral_message", "indirectness": "indirect"}
17. {"emotional_intensity": "strong", "writing_style": "conversational", "context": "social_media", "topic": "daily_life", "speaker_type": "venting_frustration", "indirectness": "restrained"}
18. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "product_review", "topic": "relationship", "speaker_type": "venting_frustration", "indirectness": "restrained"}
19. {"emotional_intensity": "strong", "writing_style": "conversational", "context": "customer_service", "topic": "daily_life", "speaker_type": "sharing_joy", "indirectness": "direct"}
20. {"emotional_intensity": "moderate", "writing_style": "conversational", "context": "customer_service", "topic": "finances", "speaker_type": "neutral_message", "indirectness": "restrained"}
21. {"emotional_intensity": "mild", "writing_style": "casual", "context": "social_media", "topic": "health", "speaker_type": "venting_frustration", "indirectness": "restrained"}
22. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "customer_service", "topic": "finances", "speaker_type": "sharing_joy", "indirectness": "restrained"}
23. {"emotional_intensity": "strong", "writing_style": "conversational", "context": "social_media", "topic": "finances", "speaker_type": "sharing_joy", "indirectness": "direct"}
24. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "product_review", "topic": "work", "speaker_type": "venting_frustration", "indirectness": "indirect"}

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
- Outcome: success (2.5s)
- Kept: 25/25
- Removed:
  _(none)_


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
0. {"emotional_intensity": "moderate", "writing_style": "conversational", "context": "customer_service", "topic": "finances", "speaker_type": "neutral_message", "indirectness": "indirect"}
1. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "customer_service", "topic": "daily_life", "speaker_type": "venting_frustration", "indirectness": "direct"}
2. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "customer_service", "topic": "daily_life", "speaker_type": "sharing_joy", "indirectness": "restrained"}
3. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "customer_service", "topic": "finances", "speaker_type": "neutral_message", "indirectness": "indirect"}
4. {"emotional_intensity": "mild", "writing_style": "conversational", "context": "customer_service", "topic": "finances", "speaker_type": "neutral_message", "indirectness": "indirect"}
5. {"emotional_intensity": "mild", "writing_style": "conversational", "context": "customer_service", "topic": "work", "speaker_type": "expressing_sadness", "indirectness": "indirect"}
6. {"emotional_intensity": "strong", "writing_style": "casual", "context": "personal_chat", "topic": "finances", "speaker_type": "expressing_sadness", "indirectness": "restrained"}
7. {"emotional_intensity": "mild", "writing_style": "conversational", "context": "customer_service", "topic": "daily_life", "speaker_type": "venting_frustration", "indirectness": "direct"}
8. {"emotional_intensity": "strong", "writing_style": "casual", "context": "social_media", "topic": "health", "speaker_type": "expressing_sadness", "indirectness": "direct"}
9. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "product_review", "topic": "health", "speaker_type": "sharing_joy", "indirectness": "indirect"}
10. {"emotional_intensity": "moderate", "writing_style": "conversational", "context": "customer_service", "topic": "relationship", "speaker_type": "sharing_joy", "indirectness": "direct"}
11. {"emotional_intensity": "mild", "writing_style": "casual", "context": "customer_service", "topic": "finances", "speaker_type": "neutral_message", "indirectness": "direct"}
12. {"emotional_intensity": "strong", "writing_style": "conversational", "context": "product_review", "topic": "work", "speaker_type": "neutral_message", "indirectness": "direct"}
13. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "social_media", "topic": "health", "speaker_type": "expressing_sadness", "indirectness": "indirect"}
14. {"emotional_intensity": "strong", "writing_style": "casual", "context": "personal_chat", "topic": "finances", "speaker_type": "venting_frustration", "indirectness": "restrained"}
15. {"emotional_intensity": "mild", "writing_style": "conversational", "context": "personal_chat", "topic": "work", "speaker_type": "neutral_message", "indirectness": "indirect"}
16. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "social_media", "topic": "relationship", "speaker_type": "venting_frustration", "indirectness": "direct"}
17. {"emotional_intensity": "strong", "writing_style": "casual", "context": "social_media", "topic": "daily_life", "speaker_type": "sharing_joy", "indirectness": "restrained"}
18. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "personal_chat", "topic": "relationship", "speaker_type": "expressing_sadness", "indirectness": "indirect"}
19. {"emotional_intensity": "mild", "writing_style": "conversational", "context": "social_media", "topic": "daily_life", "speaker_type": "expressing_sadness", "indirectness": "restrained"}
20. {"emotional_intensity": "mild", "writing_style": "casual", "context": "product_review", "topic": "relationship", "speaker_type": "expressing_sadness", "indirectness": "indirect"}
21. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "product_review", "topic": "health", "speaker_type": "neutral_message", "indirectness": "direct"}
22. {"emotional_intensity": "moderate", "writing_style": "conversational", "context": "product_review", "topic": "daily_life", "speaker_type": "neutral_message", "indirectness": "direct"}
23. {"emotional_intensity": "mild", "writing_style": "conversational", "context": "personal_chat", "topic": "health", "speaker_type": "venting_frustration", "indirectness": "restrained"}
24. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "product_review", "topic": "finances", "speaker_type": "sharing_joy", "indirectness": "restrained"}

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
- Outcome: success (2.4s)
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
0. {"emotional_intensity": "mild", "writing_style": "conversational", "context": "customer_service", "topic": "finances", "speaker_type": "sharing_joy", "indirectness": "restrained"}
1. {"emotional_intensity": "strong", "writing_style": "conversational", "context": "customer_service", "topic": "finances", "speaker_type": "neutral_message", "indirectness": "direct"}
2. {"emotional_intensity": "strong", "writing_style": "casual", "context": "social_media", "topic": "finances", "speaker_type": "expressing_sadness", "indirectness": "direct"}
3. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "product_review", "topic": "relationship", "speaker_type": "expressing_sadness", "indirectness": "direct"}
4. {"emotional_intensity": "strong", "writing_style": "casual", "context": "personal_chat", "topic": "work", "speaker_type": "sharing_joy", "indirectness": "indirect"}
5. {"emotional_intensity": "strong", "writing_style": "casual", "context": "social_media", "topic": "work", "speaker_type": "sharing_joy", "indirectness": "direct"}
6. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "customer_service", "topic": "work", "speaker_type": "expressing_sadness", "indirectness": "direct"}
7. {"emotional_intensity": "moderate", "writing_style": "conversational", "context": "customer_service", "topic": "work", "speaker_type": "venting_frustration", "indirectness": "indirect"}
8. {"emotional_intensity": "mild", "writing_style": "conversational", "context": "social_media", "topic": "finances", "speaker_type": "sharing_joy", "indirectness": "indirect"}
9. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "product_review", "topic": "daily_life", "speaker_type": "sharing_joy", "indirectness": "indirect"}
10. {"emotional_intensity": "moderate", "writing_style": "conversational", "context": "social_media", "topic": "daily_life", "speaker_type": "expressing_sadness", "indirectness": "direct"}
11. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "product_review", "topic": "relationship", "speaker_type": "neutral_message", "indirectness": "direct"}
12. {"emotional_intensity": "strong", "writing_style": "conversational", "context": "product_review", "topic": "health", "speaker_type": "neutral_message", "indirectness": "direct"}
13. {"emotional_intensity": "strong", "writing_style": "casual", "context": "personal_chat", "topic": "finances", "speaker_type": "expressing_sadness", "indirectness": "direct"}
14. {"emotional_intensity": "moderate", "writing_style": "conversational", "context": "customer_service", "topic": "health", "speaker_type": "venting_frustration", "indirectness": "indirect"}
15. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "customer_service", "topic": "finances", "speaker_type": "neutral_message", "indirectness": "restrained"}
16. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "customer_service", "topic": "relationship", "speaker_type": "expressing_sadness", "indirectness": "restrained"}
17. {"emotional_intensity": "mild", "writing_style": "casual", "context": "product_review", "topic": "finances", "speaker_type": "venting_frustration", "indirectness": "indirect"}
18. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "product_review", "topic": "daily_life", "speaker_type": "venting_frustration", "indirectness": "restrained"}
19. {"emotional_intensity": "mild", "writing_style": "casual", "context": "customer_service", "topic": "relationship", "speaker_type": "neutral_message", "indirectness": "restrained"}
20. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "personal_chat", "topic": "health", "speaker_type": "expressing_sadness", "indirectness": "restrained"}
21. {"emotional_intensity": "strong", "writing_style": "casual", "context": "product_review", "topic": "work", "speaker_type": "neutral_message", "indirectness": "restrained"}
22. {"emotional_intensity": "moderate", "writing_style": "conversational", "context": "customer_service", "topic": "work", "speaker_type": "sharing_joy", "indirectness": "indirect"}
23. {"emotional_intensity": "mild", "writing_style": "conversational", "context": "social_media", "topic": "health", "speaker_type": "expressing_sadness", "indirectness": "indirect"}
24. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "customer_service", "topic": "health", "speaker_type": "venting_frustration", "indirectness": "direct"}

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
- Outcome: success (2.4s)
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
0. {"emotional_intensity": "moderate", "writing_style": "slightly_formal", "context": "personal_chat", "topic": "health", "speaker_type": "sharing_joy", "indirectness": "indirect"}
1. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "customer_service", "topic": "health", "speaker_type": "expressing_sadness", "indirectness": "direct"}
2. {"emotional_intensity": "strong", "writing_style": "slightly_formal", "context": "customer_service", "topic": "relationship", "speaker_type": "sharing_joy", "indirectness": "indirect"}
3. {"emotional_intensity": "strong", "writing_style": "casual", "context": "product_review", "topic": "relationship", "speaker_type": "venting_frustration", "indirectness": "direct"}
4. {"emotional_intensity": "strong", "writing_style": "conversational", "context": "product_review", "topic": "work", "speaker_type": "expressing_sadness", "indirectness": "indirect"}
5. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "personal_chat", "topic": "daily_life", "speaker_type": "neutral_message", "indirectness": "direct"}
6. {"emotional_intensity": "moderate", "writing_style": "conversational", "context": "customer_service", "topic": "relationship", "speaker_type": "sharing_joy", "indirectness": "indirect"}
7. {"emotional_intensity": "moderate", "writing_style": "conversational", "context": "social_media", "topic": "finances", "speaker_type": "venting_frustration", "indirectness": "restrained"}
8. {"emotional_intensity": "moderate", "writing_style": "conversational", "context": "personal_chat", "topic": "finances", "speaker_type": "expressing_sadness", "indirectness": "restrained"}
9. {"emotional_intensity": "strong", "writing_style": "conversational", "context": "personal_chat", "topic": "work", "speaker_type": "venting_frustration", "indirectness": "restrained"}
10. {"emotional_intensity": "strong", "writing_style": "casual", "context": "product_review", "topic": "work", "speaker_type": "sharing_joy", "indirectness": "direct"}
11. {"emotional_intensity": "strong", "writing_style": "casual", "context": "social_media", "topic": "daily_life", "speaker_type": "expressing_sadness", "indirectness": "direct"}
12. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "customer_service", "topic": "finances", "speaker_type": "neutral_message", "indirectness": "indirect"}
13. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "personal_chat", "topic": "health", "speaker_type": "venting_frustration", "indirectness": "restrained"}
14. {"emotional_intensity": "strong", "writing_style": "slightly_formal", "context": "customer_service", "topic": "daily_life", "speaker_type": "neutral_message", "indirectness": "restrained"}
15. {"emotional_intensity": "strong", "writing_style": "slightly_formal", "context": "personal_chat", "topic": "daily_life", "speaker_type": "sharing_joy", "indirectness": "restrained"}
16. {"emotional_intensity": "mild", "writing_style": "conversational", "context": "customer_service", "topic": "work", "speaker_type": "venting_frustration", "indirectness": "direct"}
17. {"emotional_intensity": "mild", "writing_style": "casual", "context": "product_review", "topic": "work", "speaker_type": "venting_frustration", "indirectness": "direct"}
18. {"emotional_intensity": "mild", "writing_style": "conversational", "context": "product_review", "topic": "health", "speaker_type": "sharing_joy", "indirectness": "restrained"}
19. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "customer_service", "topic": "health", "speaker_type": "venting_frustration", "indirectness": "restrained"}
20. {"emotional_intensity": "mild", "writing_style": "slightly_formal", "context": "customer_service", "topic": "finances", "speaker_type": "expressing_sadness", "indirectness": "indirect"}
21. {"emotional_intensity": "strong", "writing_style": "conversational", "context": "social_media", "topic": "finances", "speaker_type": "venting_frustration", "indirectness": "indirect"}
22. {"emotional_intensity": "mild", "writing_style": "conversational", "context": "social_media", "topic": "work", "speaker_type": "expressing_sadness", "indirectness": "restrained"}
23. {"emotional_intensity": "strong", "writing_style": "casual", "context": "customer_service", "topic": "work", "speaker_type": "sharing_joy", "indirectness": "indirect"}
24. {"emotional_intensity": "strong", "writing_style": "casual", "context": "customer_service", "topic": "relationship", "speaker_type": "sharing_joy", "indirectness": "direct"}

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


## Summary
- Input: 100 combinations
- Kept: 100 combinations
- Removed: 0 combinations
