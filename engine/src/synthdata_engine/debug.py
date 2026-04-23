"""Debug writer — per-stage markdown logs for inspection and validation."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class DebugWriter:
    run_dir: Path

    def __post_init__(self) -> None:
        self.run_dir.mkdir(parents=True, exist_ok=True)

    def write(self, filename: str, content: str) -> None:
        (self.run_dir / filename).write_text(content, encoding="utf-8")

    def append(self, filename: str, content: str) -> None:
        path = self.run_dir / filename
        with path.open("a", encoding="utf-8") as f:
            f.write(content)


def _json(obj: object) -> str:
    try:
        return json.dumps(obj, indent=2, ensure_ascii=False)
    except Exception:
        return str(obj)


def _fence(content: str, lang: str = "") -> str:
    return f"```{lang}\n{content.strip()}\n```"


def make_run_dir(base: Path, name: str | None = None) -> Path:
    """Create a uniquely named run directory inside `base`."""
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder = base / (name or f"run_{ts}")
    folder.mkdir(parents=True, exist_ok=True)
    return folder
