from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .providers.serper import SerperSearchProvider
from .research_collector import collect_research


def run_research_from_report(
    report_path: Path,
    output_path: Path,
    provider_name: str = "serper",
    results_per_query: int = 5,
) -> Path:
    report: dict[str, Any] = json.loads(report_path.read_text(encoding="utf-8"))
    plan = report.get("research_plan")
    if not plan:
        raise ValueError("Report does not contain a research_plan")

    if provider_name == "serper":
        provider = SerperSearchProvider()
    else:
        raise ValueError(f"Unknown provider: {provider_name}")

    bundle = collect_research(
        plan,
        provider,
        results_per_query=results_per_query,
        fetch_pages=True,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(bundle, indent=2), encoding="utf-8")
    return output_path
