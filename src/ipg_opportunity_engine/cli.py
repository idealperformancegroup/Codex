from __future__ import annotations

import json
from pathlib import Path

import typer
from rich import print

from .pipeline import run_social_pipeline
from .social_intelligence import create_signal_report

app = typer.Typer(help="IPG Opportunity Engine")


@app.command()
def intake(
    url: str = typer.Argument(..., help="Social or market URL to capture"),
    out: Path = typer.Option(Path("outputs/opportunity-report.json"), "--out", "-o"),
) -> None:
    """Capture a URL as a structured opportunity signal without downloading media."""
    report = create_signal_report(url)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps(report.model_dump(mode="json"), indent=2),
        encoding="utf-8",
    )
    print(f"[green]Captured[/green] {report.source.platform}: {url}")
    print(f"[green]Wrote[/green] {out}")


@app.command("analyze-social")
def analyze_social(
    url: str = typer.Argument(..., help="Permitted public social-media URL"),
    run_dir: Path = typer.Option(Path("runs/social"), "--run-dir"),
    whisper_model: str = typer.Option("small", "--whisper-model"),
) -> None:
    """Capture, transcribe, sample frames, and produce a Social Intelligence report."""
    output = run_social_pipeline(url, run_dir, whisper_model)
    print(f"[green]Social Intelligence report[/green] {output}")


if __name__ == "__main__":
    app()
