from __future__ import annotations

import json
from pathlib import Path

import typer
from rich import print

from .orchestrator import run_opportunity_engine
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


@app.command("run")
def run_engine(
    url: str = typer.Argument(..., help="Permitted public signal URL"),
    run_dir: Path = typer.Option(Path("runs/opportunity"), "--run-dir"),
    whisper_model: str = typer.Option("small", "--whisper-model"),
    research: bool = typer.Option(True, "--research/--no-research"),
    results_per_query: int = typer.Option(5, "--results-per-query", min=1, max=20),
) -> None:
    """Run the end-to-end IPG Opportunity Engine."""
    output = run_opportunity_engine(
        url,
        run_dir,
        whisper_model=whisper_model,
        results_per_query=results_per_query,
        do_research=research,
    )
    print(f"[bold green]Opportunity Engine report[/bold green] {output}")


if __name__ == "__main__":
    app()
