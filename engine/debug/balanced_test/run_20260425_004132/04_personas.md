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
    "A college student casually texting friends about a frustrating group project, using slang and sarcasm.",
    "A young professional sharing a work achievement on LinkedIn, striving for optimistic and polished.",
    "A grieving widow privately journaling her feelings, writing in fragmented sentences and raw emotion.",
    "A customer service agent neutrally asking clarifying questions, maintaining a professional tone.",
    "A parent venting on a parenting forum about toddler tantrums, using exasperated but relatable language.",
    "A retiree reminiscing about a happy memory with their spouse, writing warmly and nostalgically.",
    "A teenager expressing disappointment over a cancelled concert, using dramatic but typical teen language.",
    "A software engineer reporting a bug in a professional chat, concise and focused on technical details.",
    "A dog owner sharing a heartwarming video of their pet, enthusiastic and filled with joy.",
    "A patient describing symptoms to a doctor via text, factual and slightly anxious.",
    "A book reviewer giving a neutral summary of a plot, analytical and objective.",
    "A person feeling lonely after moving to a new city, writing with quiet sadness and self-reflection.",
    "An online gamer expressing rage after losing a match, using some strong language but not excessive.",
    "A traveler sharing excitement about an upcoming vacation, using exclamation points and descriptive language.",
    "A volunteer expressing gratitude for donations to a cause, sincere and appreciative.",
    "A person politely requesting a refund for a defective product, assertive but respectful.",
    "A student describing a boring lecture, using dry wit and understatement.",
    "A person expressing sadness about a pet’s illness, vulnerable and heartbroken.",
    "A chef reviewing a new kitchen appliance, practical and focused on functionality.",
    "A musician sharing a joyful update about a successful gig, enthusiastic and energetic.",
    "A person feeling frustrated with slow internet service, complaining with mild irritation.",
    "An artist sharing their latest creation on Instagram, proud and hopeful for feedback.",
    "A teacher acknowledging a student’s improvement, encouraging and positive.",
    "A person expressing disappointment with a restaurant meal, specific and constructive criticism.",
    "A commuter complaining about a delayed train, using sarcastic humor and resignation.",
    "A person sharing a funny anecdote from their day, lighthearted and conversational.",
    "A lawyer neutrally summarizing case details, precise and formal but not overly emotional.",
    "A person feeling overwhelmed by work, expressing stress and fatigue in a subdued way.",
    "A fan reacting to a sports team's victory, ecstatic and exuberant.",
    "A person politely declining an invitation, apologetic and respectful.",
    "An employee expressing frustration with a company policy, cautiously worded and slightly passive-aggressive."
  ]
}
```
```

## Generated Personas (31)

1. A college student casually texting friends about a frustrating group project, using slang and sarcasm.
2. A young professional sharing a work achievement on LinkedIn, striving for optimistic and polished.
3. A grieving widow privately journaling her feelings, writing in fragmented sentences and raw emotion.
4. A customer service agent neutrally asking clarifying questions, maintaining a professional tone.
5. A parent venting on a parenting forum about toddler tantrums, using exasperated but relatable language.
6. A retiree reminiscing about a happy memory with their spouse, writing warmly and nostalgically.
7. A teenager expressing disappointment over a cancelled concert, using dramatic but typical teen language.
8. A software engineer reporting a bug in a professional chat, concise and focused on technical details.
9. A dog owner sharing a heartwarming video of their pet, enthusiastic and filled with joy.
10. A patient describing symptoms to a doctor via text, factual and slightly anxious.
11. A book reviewer giving a neutral summary of a plot, analytical and objective.
12. A person feeling lonely after moving to a new city, writing with quiet sadness and self-reflection.
13. An online gamer expressing rage after losing a match, using some strong language but not excessive.
14. A traveler sharing excitement about an upcoming vacation, using exclamation points and descriptive language.
15. A volunteer expressing gratitude for donations to a cause, sincere and appreciative.
16. A person politely requesting a refund for a defective product, assertive but respectful.
17. A student describing a boring lecture, using dry wit and understatement.
18. A person expressing sadness about a pet’s illness, vulnerable and heartbroken.
19. A chef reviewing a new kitchen appliance, practical and focused on functionality.
20. A musician sharing a joyful update about a successful gig, enthusiastic and energetic.
21. A person feeling frustrated with slow internet service, complaining with mild irritation.
22. An artist sharing their latest creation on Instagram, proud and hopeful for feedback.
23. A teacher acknowledging a student’s improvement, encouraging and positive.
24. A person expressing disappointment with a restaurant meal, specific and constructive criticism.
25. A commuter complaining about a delayed train, using sarcastic humor and resignation.
26. A person sharing a funny anecdote from their day, lighthearted and conversational.
27. A lawyer neutrally summarizing case details, precise and formal but not overly emotional.
28. A person feeling overwhelmed by work, expressing stress and fatigue in a subdued way.
29. A fan reacting to a sports team's victory, ecstatic and exuberant.
30. A person politely declining an invitation, apologetic and respectful.
31. An employee expressing frustration with a company policy, cautiously worded and slightly passive-aggressive.

## Stats
- Outcome: success
- Duration: 8.1s
