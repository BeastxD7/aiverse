"""CLI: `uv run synthdata run config.yaml`."""

from __future__ import annotations

import asyncio
import csv
import json
import sys
from pathlib import Path

import typer
from dotenv import find_dotenv, load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from .config import load_config
from .debug import make_run_dir
from .pipeline import run_job

# Auto-load .env — walks up from CWD so one .env at the repo root works from any subdir.
load_dotenv(find_dotenv(usecwd=True))

# Line-buffer stdout so live logs flush immediately even when piped.
try:
    sys.stdout.reconfigure(line_buffering=True)  # type: ignore[attr-defined]
except AttributeError:
    pass

app = typer.Typer(add_completion=False, help="SynthData engine CLI")
console = Console(force_terminal=True)


@app.command()
def run(
    config_path: Path = typer.Argument(..., exists=True, readable=True),
    output: Path = typer.Option(Path("out.jsonl"), "--output", "-o"),
    format: str = typer.Option("jsonl", "--format", "-f", help="jsonl | json | csv"),
    target: int | None = typer.Option(None, "--target", help="Override target_count"),
    debug_dir: Path | None = typer.Option(None, "--debug-dir", "-d", help="Write per-stage debug logs to this folder (e.g. debug/test1)"),
) -> None:
    """Run a generation job from a YAML config."""
    cfg = load_config(config_path)
    if target is not None:
        cfg.dataset.target_count = target

    run_debug_dir = make_run_dir(debug_dir) if debug_dir else None

    console.print(
        Panel.fit(
            f"[bold]{cfg.project.name}[/bold]\n"
            f"Target: {cfg.dataset.target_count} samples\n"
            f"Provider: {cfg.provider.type}/{cfg.provider.model}"
            + (f"\nDebug: {run_debug_dir}" if run_debug_dir else ""),
            title="SynthData run",
            border_style="cyan",
        )
    )

    def on_stage(stage: str, payload: dict) -> None:
        console.log(f"[cyan]{stage}[/cyan] {payload}")

    def on_progress(event: dict) -> None:
        t = event.get("type")
        if t == "sample":
            total = event.get("total_succeeded", 0)
            if total % 10 == 0:
                console.log(f"[green]✓[/green] {total} samples ok")
        elif t == "refusal":
            console.log(f"[yellow]⚠[/yellow] refusal on combo {event.get('combination_id')}")
        elif t == "schema_fail":
            console.log(f"[red]✗[/red] schema fail: {event.get('errors')}")
        elif t == "error":
            console.log(f"[red]![/red] error: {event.get('error')}")

    result = asyncio.run(run_job(cfg, on_stage=on_stage, on_progress=on_progress, debug_dir=run_debug_dir))

    _write_output(result.samples, output, format)
    _print_summary(result, output)


def _write_output(samples: list[dict], path: Path, fmt: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fmt == "jsonl":
        with path.open("w") as f:
            for s in samples:
                f.write(json.dumps(s, ensure_ascii=False) + "\n")
    elif fmt == "json":
        path.write_text(json.dumps(samples, ensure_ascii=False, indent=2))
    elif fmt == "csv":
        if not samples:
            path.write_text("")
            return
        keys = list(samples[0].keys())
        with path.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(samples)
    else:
        raise typer.BadParameter(f"unknown format: {fmt}")


def _print_summary(result, output: Path) -> None:
    t = Table(title="Run summary", show_header=False, border_style="green")
    t.add_column()
    t.add_column()
    t.add_row("Samples written", str(len(result.samples)))
    t.add_row("Axes discovered", str(len(result.axes)))
    t.add_row("Combinations total / kept", f"{result.combinations_total} / {result.combinations_kept}")
    t.add_row("Succeeded / schema-failed / refusals / errors",
              f"{result.gen_stats.succeeded} / {result.gen_stats.schema_failed} / "
              f"{result.gen_stats.refusals} / {result.gen_stats.errors}")
    t.add_row("Retries", str(result.gen_stats.retries))
    t.add_row("Duplicates removed", str(result.duplicates_removed))
    if result.judge_stats.judged:
        t.add_row("Judge passed / failed", f"{result.judge_stats.passed} / {result.judge_stats.failed}")
    t.add_row("Elapsed", f"{result.elapsed_seconds:.1f}s")
    t.add_row("Output", str(output))
    console.print(t)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
