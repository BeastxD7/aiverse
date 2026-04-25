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
    "A college student venting about a difficult exam, using sarcastic and frustrated language.",
    "A young adult excitedly sharing news of a job offer, full of enthusiastic emojis.",
    "An elderly person quietly reflecting on a lost friend, writing in a melancholic tone.",
    "A customer service agent summarizing a support ticket, maintaining a neutral, factual style.",
    "A parent expressing disappointment over a child's behavior, using gentle but firm wording.",
    "A traveler sharing a breathtaking view from their vacation, with descriptive and joyful prose.",
    "A teenager lamenting a breakup via text, using slang and dramatic hyperbole.",
    "A software engineer reporting a bug, focusing on technical details without emotional coloring.",
    "A retiree expressing gratitude for a kind act from a neighbor, in a warm and sincere manner.",
    "A patient describing their symptoms to a doctor, conveying discomfort in a reserved way.",
    "A gamer frustrated with lag during an online match, using aggressive and impatient language.",
    "A musician celebrating a successful performance, radiating confidence and excitement.",
    "A recent graduate expressing anxiety about starting a new career, with hesitant phrasing.",
    "A librarian providing information about library hours, objective and concise.",
    "A homeowner complaining about a faulty appliance, using irritated and demanding language.",
    "A volunteer sharing a heartwarming experience from a charity event, filled with empathy.",
    "A high school student upset about being left out of plans, conveying hurt and resentment.",
    "An accountant clarifying a billing issue, professional and detached.",
    "A chef expressing pride in a new recipe, passionate and descriptive.",
    "A single person feeling lonely on a weekend, writing in a wistful and reflective style.",
    "A commuter describing a delayed train, matter-of-fact and inconvenienced.",
    "A pet owner expressing joy over a pet's funny antics, playful and affectionate.",
    "A teacher expressing concern about a student's progress, caring and thoughtful.",
    "A delivery driver explaining a package delay, apologetic and informative.",
    "A fitness enthusiast celebrating a personal best, motivating and self-assured.",
    "A caregiver expressing exhaustion from constant responsibility, weary and subdued.",
    "A receptionist answering a phone call, polite and neutral.",
    "An artist sharing their latest creation, proud and expressive.",
    "A student struggling with online learning, frustrated and overwhelmed.",
    "A foodie reviewing a restaurant, opinionated and descriptive.",
    "A friend consoling another after a loss, empathetic and supportive."
  ]
}
```
```

## Generated Personas (31)

1. A college student venting about a difficult exam, using sarcastic and frustrated language.
2. A young adult excitedly sharing news of a job offer, full of enthusiastic emojis.
3. An elderly person quietly reflecting on a lost friend, writing in a melancholic tone.
4. A customer service agent summarizing a support ticket, maintaining a neutral, factual style.
5. A parent expressing disappointment over a child's behavior, using gentle but firm wording.
6. A traveler sharing a breathtaking view from their vacation, with descriptive and joyful prose.
7. A teenager lamenting a breakup via text, using slang and dramatic hyperbole.
8. A software engineer reporting a bug, focusing on technical details without emotional coloring.
9. A retiree expressing gratitude for a kind act from a neighbor, in a warm and sincere manner.
10. A patient describing their symptoms to a doctor, conveying discomfort in a reserved way.
11. A gamer frustrated with lag during an online match, using aggressive and impatient language.
12. A musician celebrating a successful performance, radiating confidence and excitement.
13. A recent graduate expressing anxiety about starting a new career, with hesitant phrasing.
14. A librarian providing information about library hours, objective and concise.
15. A homeowner complaining about a faulty appliance, using irritated and demanding language.
16. A volunteer sharing a heartwarming experience from a charity event, filled with empathy.
17. A high school student upset about being left out of plans, conveying hurt and resentment.
18. An accountant clarifying a billing issue, professional and detached.
19. A chef expressing pride in a new recipe, passionate and descriptive.
20. A single person feeling lonely on a weekend, writing in a wistful and reflective style.
21. A commuter describing a delayed train, matter-of-fact and inconvenienced.
22. A pet owner expressing joy over a pet's funny antics, playful and affectionate.
23. A teacher expressing concern about a student's progress, caring and thoughtful.
24. A delivery driver explaining a package delay, apologetic and informative.
25. A fitness enthusiast celebrating a personal best, motivating and self-assured.
26. A caregiver expressing exhaustion from constant responsibility, weary and subdued.
27. A receptionist answering a phone call, polite and neutral.
28. An artist sharing their latest creation, proud and expressive.
29. A student struggling with online learning, frustrated and overwhelmed.
30. A foodie reviewing a restaurant, opinionated and descriptive.
31. A friend consoling another after a loss, empathetic and supportive.

## Stats
- Outcome: success
- Duration: 8.2s
