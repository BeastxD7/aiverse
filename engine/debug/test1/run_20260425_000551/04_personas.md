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
    "A college student venting to a friend about a difficult exam, using casual slang and exaggeration.",
    "A young parent happily sharing a milestone their child achieved on social media, with emojis.",
    "An elderly person quietly expressing loneliness in a message to a distant relative, using polite language.",
    "A customer service agent neutrally asking for clarification about an order, avoiding emotional language.",
    "A frustrated gamer complaining about lag in an online game, using internet slang and sarcasm.",
    "A recently engaged person enthusiastically sharing the news with family, filled with excitement.",
    "A person mourning the loss of a pet, writing a short, heartfelt message to a friend.",
    "A commuter describing a delayed train, stating facts without expressing personal feeling.",
    "A retail worker expressing annoyance about a rude customer on a personal chat, using passive-aggression.",
    "A chef proudly showcasing a new dish on Instagram, with descriptive and positive wording.",
    "A teenager expressing disappointment about a cancelled concert, using dramatic language.",
    "A librarian responding to a factual inquiry, maintaining a professional and neutral tone.",
    "A homeowner venting about a repair issue, detailing the problem without overt anger.",
    "A teacher sharing a student's success story, expressing pride and joy.",
    "A person feeling down after a rejection, writing a melancholic message to a close friend.",
    "A data analyst reporting statistical findings, objective and devoid of emotional coloring.",
    "A software developer frustrated with a bug, briefly describing the problem in a team chat.",
    "A volunteer excitedly sharing their experience helping at a local event, full of gratitude.",
    "A person feeling isolated during the holidays, writing a subdued message to a sibling.",
    "A receptionist confirming an appointment, polite and factual without any emotional content.",
    "An artist annoyed by negative criticism, subtly hinting at frustration instead of direct accusation.",
    "A musician overjoyed by positive feedback on their new song, sharing the comments.",
    "A person grieving a breakup, writing a short, raw message detailing their sadness.",
    "A travel agent providing flight information, strictly focused on details and logistics.",
    "A mechanic describing a car repair, using technical terms and neutral language.",
    "A student relieved after finishing a project, expressing a sense of accomplishment.",
    "A person feeling overwhelmed with work, hinting at stress without explicitly complaining.",
    "A book club member recommending a novel, stating their opinion without strong emotion.",
    "A gardener lamenting a crop failure, expressing mild disappointment.",
    "A dog owner sharing a funny anecdote about their pet, using lighthearted language." ,
    "A person feeling anxious about an upcoming presentation, hinting at nervousness."
  ]
}
```
```

## Generated Personas (31)

1. A college student venting to a friend about a difficult exam, using casual slang and exaggeration.
2. A young parent happily sharing a milestone their child achieved on social media, with emojis.
3. An elderly person quietly expressing loneliness in a message to a distant relative, using polite language.
4. A customer service agent neutrally asking for clarification about an order, avoiding emotional language.
5. A frustrated gamer complaining about lag in an online game, using internet slang and sarcasm.
6. A recently engaged person enthusiastically sharing the news with family, filled with excitement.
7. A person mourning the loss of a pet, writing a short, heartfelt message to a friend.
8. A commuter describing a delayed train, stating facts without expressing personal feeling.
9. A retail worker expressing annoyance about a rude customer on a personal chat, using passive-aggression.
10. A chef proudly showcasing a new dish on Instagram, with descriptive and positive wording.
11. A teenager expressing disappointment about a cancelled concert, using dramatic language.
12. A librarian responding to a factual inquiry, maintaining a professional and neutral tone.
13. A homeowner venting about a repair issue, detailing the problem without overt anger.
14. A teacher sharing a student's success story, expressing pride and joy.
15. A person feeling down after a rejection, writing a melancholic message to a close friend.
16. A data analyst reporting statistical findings, objective and devoid of emotional coloring.
17. A software developer frustrated with a bug, briefly describing the problem in a team chat.
18. A volunteer excitedly sharing their experience helping at a local event, full of gratitude.
19. A person feeling isolated during the holidays, writing a subdued message to a sibling.
20. A receptionist confirming an appointment, polite and factual without any emotional content.
21. An artist annoyed by negative criticism, subtly hinting at frustration instead of direct accusation.
22. A musician overjoyed by positive feedback on their new song, sharing the comments.
23. A person grieving a breakup, writing a short, raw message detailing their sadness.
24. A travel agent providing flight information, strictly focused on details and logistics.
25. A mechanic describing a car repair, using technical terms and neutral language.
26. A student relieved after finishing a project, expressing a sense of accomplishment.
27. A person feeling overwhelmed with work, hinting at stress without explicitly complaining.
28. A book club member recommending a novel, stating their opinion without strong emotion.
29. A gardener lamenting a crop failure, expressing mild disappointment.
30. A dog owner sharing a funny anecdote about their pet, using lighthearted language.
31. A person feeling anxious about an upcoming presentation, hinting at nervousness.

## Stats
- Outcome: success
- Duration: 8.9s
