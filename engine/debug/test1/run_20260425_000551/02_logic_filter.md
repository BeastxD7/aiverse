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
0. {"emotional_intensity": "strong", "writing_style": "casual", "context": "social_media", "topic": "daily_life", "speaker_type": "expressing_sadness"}
1. {"emotional_intensity": "mild", "writing_style": "formal", "context": "personal_chat", "topic": "daily_life", "speaker_type": "expressing_sadness"}
2. {"emotional_intensity": "mild", "writing_style": "casual", "context": "personal_chat", "topic": "work", "speaker_type": "sharing_joy"}
3. {"emotional_intensity": "strong", "writing_style": "formal", "context": "personal_chat", "topic": "purchase", "speaker_type": "neutral_message"}
4. {"emotional_intensity": "mild", "writing_style": "reflective", "context": "customer_service", "topic": "relationship", "speaker_type": "sharing_joy"}
5. {"emotional_intensity": "mild", "writing_style": "reflective", "context": "social_media", "topic": "health", "speaker_type": "expressing_sadness"}
6. {"emotional_intensity": "mild", "writing_style": "abbreviated", "context": "product_review", "topic": "health", "speaker_type": "venting_frustration"}
7. {"emotional_intensity": "mild", "writing_style": "formal", "context": "product_review", "topic": "relationship", "speaker_type": "expressing_sadness"}
8. {"emotional_intensity": "strong", "writing_style": "formal", "context": "personal_chat", "topic": "daily_life", "speaker_type": "expressing_sadness"}
9. {"emotional_intensity": "mild", "writing_style": "formal", "context": "personal_chat", "topic": "work", "speaker_type": "venting_frustration"}
10. {"emotional_intensity": "strong", "writing_style": "casual", "context": "customer_service", "topic": "daily_life", "speaker_type": "venting_frustration"}
11. {"emotional_intensity": "strong", "writing_style": "formal", "context": "personal_chat", "topic": "purchase", "speaker_type": "expressing_sadness"}
12. {"emotional_intensity": "strong", "writing_style": "reflective", "context": "personal_chat", "topic": "daily_life", "speaker_type": "sharing_joy"}
13. {"emotional_intensity": "moderate", "writing_style": "abbreviated", "context": "product_review", "topic": "purchase", "speaker_type": "expressing_sadness"}
14. {"emotional_intensity": "mild", "writing_style": "formal", "context": "social_media", "topic": "health", "speaker_type": "sharing_joy"}
15. {"emotional_intensity": "moderate", "writing_style": "reflective", "context": "customer_service", "topic": "work", "speaker_type": "venting_frustration"}
16. {"emotional_intensity": "moderate", "writing_style": "formal", "context": "personal_chat", "topic": "daily_life", "speaker_type": "venting_frustration"}
17. {"emotional_intensity": "mild", "writing_style": "casual", "context": "personal_chat", "topic": "daily_life", "speaker_type": "venting_frustration"}
18. {"emotional_intensity": "mild", "writing_style": "casual", "context": "personal_chat", "topic": "health", "speaker_type": "expressing_sadness"}
19. {"emotional_intensity": "mild", "writing_style": "formal", "context": "social_media", "topic": "daily_life", "speaker_type": "neutral_message"}
20. {"emotional_intensity": "mild", "writing_style": "abbreviated", "context": "product_review", "topic": "relationship", "speaker_type": "neutral_message"}
21. {"emotional_intensity": "mild", "writing_style": "abbreviated", "context": "product_review", "topic": "purchase", "speaker_type": "expressing_sadness"}
22. {"emotional_intensity": "moderate", "writing_style": "abbreviated", "context": "personal_chat", "topic": "purchase", "speaker_type": "sharing_joy"}
23. {"emotional_intensity": "moderate", "writing_style": "reflective", "context": "customer_service", "topic": "purchase", "speaker_type": "venting_frustration"}
24. {"emotional_intensity": "mild", "writing_style": "casual", "context": "personal_chat", "topic": "work", "speaker_type": "neutral_message"}

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
- Outcome: success (10.5s)
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
0. {"emotional_intensity": "moderate", "writing_style": "reflective", "context": "social_media", "topic": "daily_life", "speaker_type": "expressing_sadness"}
1. {"emotional_intensity": "mild", "writing_style": "abbreviated", "context": "customer_service", "topic": "relationship", "speaker_type": "neutral_message"}
2. {"emotional_intensity": "strong", "writing_style": "formal", "context": "social_media", "topic": "daily_life", "speaker_type": "sharing_joy"}
3. {"emotional_intensity": "strong", "writing_style": "casual", "context": "personal_chat", "topic": "work", "speaker_type": "sharing_joy"}
4. {"emotional_intensity": "strong", "writing_style": "casual", "context": "product_review", "topic": "purchase", "speaker_type": "expressing_sadness"}
5. {"emotional_intensity": "strong", "writing_style": "reflective", "context": "product_review", "topic": "work", "speaker_type": "expressing_sadness"}
6. {"emotional_intensity": "moderate", "writing_style": "formal", "context": "personal_chat", "topic": "health", "speaker_type": "sharing_joy"}
7. {"emotional_intensity": "mild", "writing_style": "abbreviated", "context": "product_review", "topic": "work", "speaker_type": "sharing_joy"}
8. {"emotional_intensity": "moderate", "writing_style": "formal", "context": "customer_service", "topic": "purchase", "speaker_type": "neutral_message"}
9. {"emotional_intensity": "moderate", "writing_style": "reflective", "context": "customer_service", "topic": "relationship", "speaker_type": "neutral_message"}
10. {"emotional_intensity": "mild", "writing_style": "reflective", "context": "customer_service", "topic": "work", "speaker_type": "venting_frustration"}
11. {"emotional_intensity": "strong", "writing_style": "abbreviated", "context": "personal_chat", "topic": "health", "speaker_type": "venting_frustration"}
12. {"emotional_intensity": "strong", "writing_style": "reflective", "context": "social_media", "topic": "health", "speaker_type": "expressing_sadness"}
13. {"emotional_intensity": "mild", "writing_style": "casual", "context": "social_media", "topic": "work", "speaker_type": "expressing_sadness"}
14. {"emotional_intensity": "strong", "writing_style": "formal", "context": "customer_service", "topic": "purchase", "speaker_type": "sharing_joy"}
15. {"emotional_intensity": "strong", "writing_style": "abbreviated", "context": "personal_chat", "topic": "work", "speaker_type": "sharing_joy"}
16. {"emotional_intensity": "mild", "writing_style": "abbreviated", "context": "social_media", "topic": "relationship", "speaker_type": "neutral_message"}
17. {"emotional_intensity": "strong", "writing_style": "casual", "context": "product_review", "topic": "daily_life", "speaker_type": "expressing_sadness"}
18. {"emotional_intensity": "strong", "writing_style": "reflective", "context": "product_review", "topic": "relationship", "speaker_type": "neutral_message"}
19. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "personal_chat", "topic": "health", "speaker_type": "venting_frustration"}
20. {"emotional_intensity": "strong", "writing_style": "reflective", "context": "customer_service", "topic": "work", "speaker_type": "venting_frustration"}
21. {"emotional_intensity": "mild", "writing_style": "formal", "context": "product_review", "topic": "purchase", "speaker_type": "neutral_message"}
22. {"emotional_intensity": "mild", "writing_style": "abbreviated", "context": "product_review", "topic": "relationship", "speaker_type": "venting_frustration"}
23. {"emotional_intensity": "strong", "writing_style": "formal", "context": "product_review", "topic": "relationship", "speaker_type": "sharing_joy"}
24. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "personal_chat", "topic": "work", "speaker_type": "venting_frustration"}

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
0. {"emotional_intensity": "strong", "writing_style": "reflective", "context": "product_review", "topic": "health", "speaker_type": "expressing_sadness"}
1. {"emotional_intensity": "mild", "writing_style": "formal", "context": "social_media", "topic": "daily_life", "speaker_type": "expressing_sadness"}
2. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "product_review", "topic": "health", "speaker_type": "sharing_joy"}
3. {"emotional_intensity": "mild", "writing_style": "formal", "context": "social_media", "topic": "purchase", "speaker_type": "neutral_message"}
4. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "customer_service", "topic": "work", "speaker_type": "neutral_message"}
5. {"emotional_intensity": "strong", "writing_style": "abbreviated", "context": "product_review", "topic": "work", "speaker_type": "neutral_message"}
6. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "personal_chat", "topic": "daily_life", "speaker_type": "venting_frustration"}
7. {"emotional_intensity": "moderate", "writing_style": "reflective", "context": "customer_service", "topic": "purchase", "speaker_type": "expressing_sadness"}
8. {"emotional_intensity": "mild", "writing_style": "reflective", "context": "personal_chat", "topic": "health", "speaker_type": "expressing_sadness"}
9. {"emotional_intensity": "strong", "writing_style": "abbreviated", "context": "personal_chat", "topic": "work", "speaker_type": "expressing_sadness"}
10. {"emotional_intensity": "mild", "writing_style": "casual", "context": "customer_service", "topic": "work", "speaker_type": "venting_frustration"}
11. {"emotional_intensity": "strong", "writing_style": "formal", "context": "personal_chat", "topic": "work", "speaker_type": "neutral_message"}
12. {"emotional_intensity": "moderate", "writing_style": "formal", "context": "product_review", "topic": "health", "speaker_type": "expressing_sadness"}
13. {"emotional_intensity": "moderate", "writing_style": "abbreviated", "context": "product_review", "topic": "health", "speaker_type": "sharing_joy"}
14. {"emotional_intensity": "mild", "writing_style": "formal", "context": "customer_service", "topic": "work", "speaker_type": "neutral_message"}
15. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "product_review", "topic": "work", "speaker_type": "neutral_message"}
16. {"emotional_intensity": "mild", "writing_style": "formal", "context": "social_media", "topic": "relationship", "speaker_type": "venting_frustration"}
17. {"emotional_intensity": "moderate", "writing_style": "reflective", "context": "social_media", "topic": "work", "speaker_type": "sharing_joy"}
18. {"emotional_intensity": "mild", "writing_style": "reflective", "context": "product_review", "topic": "relationship", "speaker_type": "venting_frustration"}
19. {"emotional_intensity": "strong", "writing_style": "abbreviated", "context": "customer_service", "topic": "health", "speaker_type": "sharing_joy"}
20. {"emotional_intensity": "strong", "writing_style": "casual", "context": "social_media", "topic": "relationship", "speaker_type": "neutral_message"}
21. {"emotional_intensity": "moderate", "writing_style": "reflective", "context": "product_review", "topic": "daily_life", "speaker_type": "sharing_joy"}
22. {"emotional_intensity": "strong", "writing_style": "reflective", "context": "social_media", "topic": "relationship", "speaker_type": "expressing_sadness"}
23. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "customer_service", "topic": "health", "speaker_type": "expressing_sadness"}
24. {"emotional_intensity": "moderate", "writing_style": "reflective", "context": "personal_chat", "topic": "health", "speaker_type": "neutral_message"}

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
0. {"emotional_intensity": "mild", "writing_style": "abbreviated", "context": "personal_chat", "topic": "purchase", "speaker_type": "venting_frustration"}
1. {"emotional_intensity": "strong", "writing_style": "formal", "context": "social_media", "topic": "relationship", "speaker_type": "sharing_joy"}
2. {"emotional_intensity": "mild", "writing_style": "casual", "context": "product_review", "topic": "health", "speaker_type": "neutral_message"}
3. {"emotional_intensity": "mild", "writing_style": "casual", "context": "customer_service", "topic": "work", "speaker_type": "expressing_sadness"}
4. {"emotional_intensity": "strong", "writing_style": "casual", "context": "personal_chat", "topic": "purchase", "speaker_type": "sharing_joy"}
5. {"emotional_intensity": "mild", "writing_style": "abbreviated", "context": "product_review", "topic": "daily_life", "speaker_type": "sharing_joy"}
6. {"emotional_intensity": "strong", "writing_style": "formal", "context": "product_review", "topic": "health", "speaker_type": "neutral_message"}
7. {"emotional_intensity": "mild", "writing_style": "reflective", "context": "customer_service", "topic": "purchase", "speaker_type": "venting_frustration"}
8. {"emotional_intensity": "mild", "writing_style": "formal", "context": "social_media", "topic": "relationship", "speaker_type": "sharing_joy"}
9. {"emotional_intensity": "strong", "writing_style": "abbreviated", "context": "product_review", "topic": "daily_life", "speaker_type": "neutral_message"}
10. {"emotional_intensity": "strong", "writing_style": "reflective", "context": "customer_service", "topic": "purchase", "speaker_type": "expressing_sadness"}
11. {"emotional_intensity": "mild", "writing_style": "formal", "context": "personal_chat", "topic": "relationship", "speaker_type": "neutral_message"}
12. {"emotional_intensity": "strong", "writing_style": "reflective", "context": "personal_chat", "topic": "work", "speaker_type": "neutral_message"}
13. {"emotional_intensity": "strong", "writing_style": "reflective", "context": "personal_chat", "topic": "daily_life", "speaker_type": "expressing_sadness"}
14. {"emotional_intensity": "moderate", "writing_style": "formal", "context": "product_review", "topic": "work", "speaker_type": "venting_frustration"}
15. {"emotional_intensity": "strong", "writing_style": "casual", "context": "social_media", "topic": "health", "speaker_type": "expressing_sadness"}
16. {"emotional_intensity": "strong", "writing_style": "abbreviated", "context": "customer_service", "topic": "daily_life", "speaker_type": "expressing_sadness"}
17. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "customer_service", "topic": "daily_life", "speaker_type": "sharing_joy"}
18. {"emotional_intensity": "mild", "writing_style": "abbreviated", "context": "social_media", "topic": "work", "speaker_type": "expressing_sadness"}
19. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "customer_service", "topic": "purchase", "speaker_type": "neutral_message"}
20. {"emotional_intensity": "moderate", "writing_style": "casual", "context": "customer_service", "topic": "relationship", "speaker_type": "neutral_message"}
21. {"emotional_intensity": "mild", "writing_style": "abbreviated", "context": "customer_service", "topic": "daily_life", "speaker_type": "expressing_sadness"}
22. {"emotional_intensity": "strong", "writing_style": "casual", "context": "customer_service", "topic": "work", "speaker_type": "expressing_sadness"}
23. {"emotional_intensity": "mild", "writing_style": "reflective", "context": "personal_chat", "topic": "daily_life", "speaker_type": "sharing_joy"}
24. {"emotional_intensity": "strong", "writing_style": "reflective", "context": "customer_service", "topic": "health", "speaker_type": "expressing_sadness"}

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


## Summary
- Input: 100 combinations
- Kept: 100 combinations
- Removed: 0 combinations
