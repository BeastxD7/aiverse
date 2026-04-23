# Stage 3 — Persona Pool

## System Prompt
```
You generate diverse writer personas. Output strict JSON only.
```

## User Prompt
```
Generate 30 distinct personas that could plausibly AUTHOR
messages in this domain. Each persona is a short description (12-25 words)
covering: role, context, writing style.

DOMAIN:
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

HARD CONSTRAINTS:
- Every persona must represent an IN-SCOPE speaker (if scope is listed above).
- Never invent a persona for an OUT-OF-SCOPE speaker type.

Return JSON:
{"personas": ["persona 1...", "persona 2...", ...]}

JSON only.
```

## Raw LLM Response
```
```json
{
  "personas": [
    "A college student sharing daily life updates with friends, often sarcastic and relatable.",
    "A working mother venting about the stresses of balancing work and family, frustrated but resilient.",
    "A retiree reflecting on past memories, sometimes wistful and occasionally joyful.",
    "A teenager expressing excitement about a concert, using slang and emojis.",
    "A customer writing a product review after a disappointing purchase, calmly dissatisfied.",
    "A gamer sharing a thrilling victory in an online game, enthusiastic and competitive.",
    "An artist describing the emotional process of creating a new piece, introspective and sensitive.",
    "A traveler recounting a positive experience on vacation, grateful and descriptive.",
    "A person confiding in a friend about a recent breakup, heartbroken and vulnerable.",
    "A pet owner sharing a heartwarming story about their animal companion, affectionate and joyful.",
    "A fitness enthusiast celebrating a personal record, motivated and proud.",
    "A commuter complaining about a delayed train, annoyed and impatient.",
    "A food blogger describing a delicious meal, appreciative and detailed.",
    "A music lover sharing their feelings about a favorite song, emotional and poetic.",
    "A volunteer discussing a rewarding experience, fulfilled and compassionate.",
    "A student anxiously awaiting exam results, stressed and apprehensive.",
    "A friend offering support to someone going through a difficult time, empathetic and caring.",
    "A person sharing a funny anecdote from their day, lighthearted and amusing.",
    "A reader expressing disappointment with a book’s ending, let down and reflective.",
    "An employee frustrated with a difficult coworker, passive-aggressive and annoyed.",
    "A parent beaming with pride over their child’s accomplishment, overjoyed and sentimental.",
    "Someone expressing loneliness after moving to a new city, isolated and melancholic.",
    "A person neutrally asking for directions, factual and polite.",
    "A person stating a simple observation about the weather, unemotional and descriptive.",
    "A person responding to a quick question with a short answer, concise and direct.",
    "A person describing a technical issue with a device, objective and problem-focused.",
    "A person sharing a news headline without personal opinion, informational and impartial.",
    "A person briefly summarizing their day without emotional coloring, matter-of-fact.",
    "A person planning a simple task, practical and organized.",
    "A person making a casual suggestion, friendly and informal."
  ]
}
```
```

## Generated Personas (30)

1. A college student sharing daily life updates with friends, often sarcastic and relatable.
2. A working mother venting about the stresses of balancing work and family, frustrated but resilient.
3. A retiree reflecting on past memories, sometimes wistful and occasionally joyful.
4. A teenager expressing excitement about a concert, using slang and emojis.
5. A customer writing a product review after a disappointing purchase, calmly dissatisfied.
6. A gamer sharing a thrilling victory in an online game, enthusiastic and competitive.
7. An artist describing the emotional process of creating a new piece, introspective and sensitive.
8. A traveler recounting a positive experience on vacation, grateful and descriptive.
9. A person confiding in a friend about a recent breakup, heartbroken and vulnerable.
10. A pet owner sharing a heartwarming story about their animal companion, affectionate and joyful.
11. A fitness enthusiast celebrating a personal record, motivated and proud.
12. A commuter complaining about a delayed train, annoyed and impatient.
13. A food blogger describing a delicious meal, appreciative and detailed.
14. A music lover sharing their feelings about a favorite song, emotional and poetic.
15. A volunteer discussing a rewarding experience, fulfilled and compassionate.
16. A student anxiously awaiting exam results, stressed and apprehensive.
17. A friend offering support to someone going through a difficult time, empathetic and caring.
18. A person sharing a funny anecdote from their day, lighthearted and amusing.
19. A reader expressing disappointment with a book’s ending, let down and reflective.
20. An employee frustrated with a difficult coworker, passive-aggressive and annoyed.
21. A parent beaming with pride over their child’s accomplishment, overjoyed and sentimental.
22. Someone expressing loneliness after moving to a new city, isolated and melancholic.
23. A person neutrally asking for directions, factual and polite.
24. A person stating a simple observation about the weather, unemotional and descriptive.
25. A person responding to a quick question with a short answer, concise and direct.
26. A person describing a technical issue with a device, objective and problem-focused.
27. A person sharing a news headline without personal opinion, informational and impartial.
28. A person briefly summarizing their day without emotional coloring, matter-of-fact.
29. A person planning a simple task, practical and organized.
30. A person making a casual suggestion, friendly and informal.

## Stats
- Outcome: success
- Duration: 7.8s
