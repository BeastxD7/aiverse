"""Provider contract shared across Ollama / OpenAI / Anthropic / etc."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Protocol


Outcome = Literal["success", "invalid_json", "refusal", "timeout", "error"]


@dataclass
class LLMResponse:
    outcome: Outcome
    raw_text: str
    parsed: dict | list | None
    error: str | None = None
    attempts: int = 1


class LLMProvider(Protocol):
    model: str

    async def generate_json(
        self,
        system: str,
        user: str,
        *,
        max_retries: int = 3,
    ) -> LLMResponse: ...

    async def generate_text(
        self,
        system: str,
        user: str,
        *,
        max_retries: int = 3,
    ) -> LLMResponse: ...
