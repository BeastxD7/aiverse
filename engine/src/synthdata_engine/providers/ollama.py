"""Ollama provider — async calls with JSON repair, refusal detection, and retries."""

from __future__ import annotations

import asyncio
import json
import re
from typing import Any

import httpx
from ollama import AsyncClient

from .base import LLMResponse

_REFUSAL_PATTERNS = re.compile(
    r"\b(i cannot|i can't|i am unable|i'm unable|i apologi[sz]e|i'm sorry|"
    r"as an ai|i do not feel comfortable|against my (guidelines|policies))\b",
    re.IGNORECASE,
)

_JSON_FENCE = re.compile(r"```(?:json)?\s*(\{[\s\S]*?\}|\[[\s\S]*?\])\s*```", re.IGNORECASE)
_OUTER_OBJECT = re.compile(r"\{[\s\S]*\}")
_OUTER_ARRAY = re.compile(r"\[[\s\S]*\]")


class OllamaProvider:
    """Async Ollama wrapper with JSON-mode generation, repair, and backoff."""

    def __init__(
        self,
        model: str,
        *,
        host: str = "http://localhost:11434",
        timeout_seconds: int = 300,
        keep_alive: str = "30m",
        max_output_tokens: int = 1024,
    ) -> None:
        self.model = model
        self.host = host
        self.timeout = timeout_seconds
        self.keep_alive = keep_alive
        self.max_output_tokens = max_output_tokens
        self._client = AsyncClient(host=host, timeout=timeout_seconds)

    async def warmup(self) -> None:
        """Load the model into memory so the first real call isn't a cold start."""
        try:
            await self._client.chat(
                model=self.model,
                messages=[{"role": "user", "content": "ok"}],
                keep_alive=self.keep_alive,
                options={"num_predict": 1},
            )
        except Exception:  # noqa: BLE001
            pass

    async def generate_json(
        self,
        system: str,
        user: str,
        *,
        max_retries: int = 3,
    ) -> LLMResponse:
        last_err: str | None = None
        raw = ""
        for attempt in range(1, max_retries + 1):
            try:
                resp = await asyncio.wait_for(
                    self._client.chat(
                        model=self.model,
                        messages=[
                            {"role": "system", "content": system},
                            {"role": "user", "content": user},
                        ],
                        format="json",
                        keep_alive=self.keep_alive,
                        options={
                            "temperature": 0.8,
                            "num_predict": self.max_output_tokens,
                        },
                    ),
                    timeout=self.timeout,
                )
                raw = (resp.message.content or "").strip()
            except (httpx.TimeoutException, asyncio.TimeoutError) as e:
                last_err = f"timeout after {self.timeout}s ({type(e).__name__})"
                await _backoff(attempt)
                continue
            except Exception as e:  # noqa: BLE001 — bubble under "error" outcome
                last_err = f"{type(e).__name__}: {e}"
                await _backoff(attempt)
                continue

            if _looks_like_refusal(raw):
                return LLMResponse(
                    outcome="refusal",
                    raw_text=raw,
                    parsed=None,
                    error="model refused",
                    attempts=attempt,
                )

            parsed = _repair_json(raw)
            if parsed is not None:
                return LLMResponse(
                    outcome="success",
                    raw_text=raw,
                    parsed=parsed,
                    attempts=attempt,
                )
            last_err = "unparseable JSON"
            await _backoff(attempt)

        return LLMResponse(
            outcome="invalid_json" if last_err == "unparseable JSON" else ("timeout" if last_err and "timeout" in last_err else "error"),
            raw_text=raw,
            parsed=None,
            error=last_err,
            attempts=max_retries,
        )

    async def generate_text(
        self,
        system: str,
        user: str,
        *,
        max_retries: int = 3,
    ) -> LLMResponse:
        last_err: str | None = None
        raw = ""
        for attempt in range(1, max_retries + 1):
            try:
                resp = await asyncio.wait_for(
                    self._client.chat(
                        model=self.model,
                        messages=[
                            {"role": "system", "content": system},
                            {"role": "user", "content": user},
                        ],
                        keep_alive=self.keep_alive,
                        options={
                            "temperature": 0.7,
                            "num_predict": self.max_output_tokens,
                        },
                    ),
                    timeout=self.timeout,
                )
                raw = (resp.message.content or "").strip()
                return LLMResponse(outcome="success", raw_text=raw, parsed=None, attempts=attempt)
            except (httpx.TimeoutException, asyncio.TimeoutError) as e:
                last_err = f"timeout after {self.timeout}s ({type(e).__name__})"
                await _backoff(attempt)
            except Exception as e:  # noqa: BLE001
                last_err = f"{type(e).__name__}: {e}"
                await _backoff(attempt)

        return LLMResponse(
            outcome="timeout" if last_err and "timeout" in last_err else "error",
            raw_text=raw,
            parsed=None,
            error=last_err,
            attempts=max_retries,
        )

    async def health_check(self) -> bool:
        try:
            async with httpx.AsyncClient(timeout=5) as c:
                r = await c.get(f"{self.host}/api/tags")
                return r.status_code == 200
        except Exception:  # noqa: BLE001
            return False


async def _backoff(attempt: int) -> None:
    # 1s, 2s, 4s...
    await asyncio.sleep(min(2 ** (attempt - 1), 8))


def _looks_like_refusal(text: str) -> bool:
    if len(text) < 40 and _REFUSAL_PATTERNS.search(text):
        return True
    if not text:
        return True
    # If it's short and contains no braces at all, treat as refusal-ish.
    if len(text) < 80 and "{" not in text and "[" not in text:
        return True
    return False


def _repair_json(text: str) -> Any | None:
    """Best-effort JSON extraction. Returns parsed object or None."""
    if not text:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    m = _JSON_FENCE.search(text)
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            pass

    for pat in (_OUTER_OBJECT, _OUTER_ARRAY):
        m = pat.search(text)
        if m:
            try:
                return json.loads(m.group(0))
            except json.JSONDecodeError:
                continue

    return None
