"""CLI: `uv run synthdata config.yaml`."""

from __future__ import annotations

import asyncio
import csv
import json
import sys
from datetime import datetime
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


def _default_output() -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return Path(f"out_{ts}.jsonl")


@app.command()
def run(
    config_path: Path = typer.Argument(..., exists=True, readable=True),
    output: Path | None = typer.Option(None, "--output", "-o", help="Output file (default: out_<timestamp>.jsonl)"),
    format: str = typer.Option("jsonl", "--format", "-f", help="jsonl | json | csv"),
    target: int | None = typer.Option(None, "--target", help="Override target_count"),
    debug_dir: Path | None = typer.Option(None, "--debug-dir", "-d", help="Write per-stage debug logs here"),
    checkpoint_dir: Path | None = typer.Option(None, "--checkpoint-dir", "-c", help="Resume interrupted runs from this folder"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Plan only: show axes, combinations, estimated calls — no generation"),
) -> None:
    """Run a generation job from a YAML config."""
    cfg = load_config(config_path)
    if target is not None:
        cfg.dataset.target_count = target

    out_path = output or _default_output()
    run_debug_dir = make_run_dir(debug_dir) if debug_dir else None

    panel_lines = [
        f"[bold]{cfg.project.name}[/bold]",
        f"Target: {cfg.dataset.target_count} samples",
        f"Provider: {cfg.provider.type}/{cfg.provider.model}",
    ]
    if dry_run:
        panel_lines.append("[yellow]DRY RUN — planning only, no generation[/yellow]")
    if run_debug_dir:
        panel_lines.append(f"Debug: {run_debug_dir}")
    if checkpoint_dir:
        panel_lines.append(f"Checkpoint: {checkpoint_dir}")

    console.print(Panel.fit("\n".join(panel_lines), title="SynthData run", border_style="cyan"))

    def on_stage(stage: str, payload: dict) -> None:
        if stage == "checkpoint" and payload.get("status") == "resuming":
            console.log(f"[cyan]checkpoint[/cyan] resuming — {payload['prior_samples']} prior samples loaded, {payload['remaining_target']} still needed")
        elif stage == "backfill":
            status = payload.get("status")
            pass_num = payload.get("pass", 1)
            pass_label = f" (pass {pass_num})" if pass_num > 1 else ""
            if status == "running":
                console.log(f"[yellow]backfill{pass_label}[/yellow] starting — {payload['gap']} samples short, {payload['overshoot']:.1f}× overshoot")
            elif status == "done":
                console.log(f"[yellow]backfill{pass_label}[/yellow] done — {payload.get('new_generated', 0)} new, total: {payload['final']}")
        elif stage == "balanced_axes":
            console.log(f"[cyan]balanced_axes[/cyan] injected label fields as axes: {payload.get('injected', [])}")
        elif stage == "quality_gate":
            console.log(f"[yellow]quality_gate[/yellow] removed {payload['filtered_by_length']} samples outside length bounds, kept {payload['kept']}")
        elif stage == "quality_report":
            pass  # shown in summary table
        elif stage == "dry_run":
            _print_dry_run(payload)
        else:
            console.log(f"[cyan]{stage}[/cyan] {payload}")

    _progress_milestone = max(10, cfg.dataset.target_count // 100)

    def on_progress(event: dict) -> None:
        t = event.get("type")
        if t == "sample":
            total = event.get("total_succeeded", 0)
            if total % _progress_milestone == 0:
                console.log(f"[green]✓[/green] {total} samples ok")
        elif t == "refusal":
            console.log(f"[yellow]⚠[/yellow] refusal on combo {event.get('combination_id')}")
        elif t == "schema_fail":
            console.log(f"[red]✗[/red] schema fail: {event.get('errors')}")
        elif t == "error":
            console.log(f"[red]![/red] error: {event.get('error')}")

    result = asyncio.run(run_job(
        cfg,
        on_stage=on_stage,
        on_progress=on_progress,
        debug_dir=run_debug_dir,
        checkpoint_dir=checkpoint_dir,
        dry_run=dry_run,
    ))

    if result.dry_run:
        return

    _write_output(result.samples, out_path, format)
    _print_summary(result, out_path)


def _print_dry_run(payload: dict) -> None:
    t = Table(title="Dry-run plan", show_header=False, border_style="yellow")
    t.add_column()
    t.add_column()
    t.add_row("Combinations total", str(payload.get("combinations_total")))
    t.add_row("Combinations kept (after filter)", str(payload.get("combinations_kept")))
    t.add_row("Plan rows", str(payload.get("plan_rows")))
    t.add_row("Planned samples (with overshoot)", str(payload.get("planned_samples")))
    t.add_row("Estimated LLM calls", str(payload.get("estimated_llm_calls")))
    t.add_row("Estimated tokens (~800/call)", f"~{payload.get('estimated_tokens_approx', 0):,}")
    console.print(t)
    axes = payload.get("axes", {})
    if axes:
        console.print("[dim]Axes:[/dim]")
        for name, vals in axes.items():
            console.print(f"  [cyan]{name}[/cyan]: {', '.join(vals)}")


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
    t.add_row(
        "Succeeded / schema-failed / refusals / errors",
        f"{result.gen_stats.succeeded} / {result.gen_stats.schema_failed} / "
        f"{result.gen_stats.refusals} / {result.gen_stats.errors}",
    )
    t.add_row("Retries", str(result.gen_stats.retries))
    t.add_row("Duplicates removed", str(result.duplicates_removed))
    if result.judge_stats.judged:
        t.add_row("Judge passed / failed", f"{result.judge_stats.passed} / {result.judge_stats.failed}")
    if result.backfill_used:
        t.add_row("Backfill", f"yes — was {result.backfill_gap} short")

    if result.quality_report:
        qr = result.quality_report
        if qr.filtered_by_length:
            t.add_row("Quality gate (length)", f"{qr.filtered_by_length} removed")
        for dist in qr.field_distributions:
            if dist.counts:
                counts_str = "  ".join(f"{k}: {v}" for k, v in dist.counts.items())
                t.add_row(f"  {dist.name}", counts_str)
            elif dist.mean_val is not None and dist.name != "source":
                if dist.is_char_count:
                    t.add_row(f"  {dist.name} (chars)", f"min={dist.min_val:.0f}  avg={dist.mean_val:.0f}  max={dist.max_val:.0f}")
                else:
                    t.add_row(f"  {dist.name}", f"min={dist.min_val:.3f}  avg={dist.mean_val:.3f}  max={dist.max_val:.3f}")
        if qr.imbalance_warnings:
            for w in qr.imbalance_warnings:
                severity = "[red]CRITICAL[/red]" if "CRITICAL" in w else "[yellow]WARNING[/yellow]"
                t.add_row(severity, w.split(":", 1)[-1].strip())

    t.add_row("Elapsed", f"{result.elapsed_seconds:.1f}s")
    t.add_row("Output", str(output))
    console.print(t)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
