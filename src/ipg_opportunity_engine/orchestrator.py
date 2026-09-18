from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .business_intelligence import build_business_intelligence
from .opportunity_scoring import ScoreInputs, score_opportunity
from .pipeline import run_social_pipeline
from .research_collector import collect_research
from .providers.serper import SerperSearchProvider


def _derive_score_inputs(bundle: dict[str, Any]) -> ScoreInputs:
    """Derive conservative placeholder scoring inputs from available evidence.

    This intentionally avoids pretending we know profitability. Values are modest
    unless there is actual collected evidence. Downstream adapters can later replace
    these heuristics with stronger, source-backed metrics.
    """
    search_results = bundle.get("search_results", [])
    pages = bundle.get("pages", [])
    demand = min(10.0, len(search_results) / 2)
    persistence = min(10.0, len(pages) / 3)
    return ScoreInputs(
        demand_evidence=demand,
        ad_persistence=persistence,
        complaint_opportunity=0,
        margin_potential=0,
        automation_advantage=0,
        fulfillment_simplicity=0,
        competition_risk=0,
        regulatory_ip_risk=0,
    )


def run_opportunity_engine(
    url: str,
    run_dir: Path,
    *,
    whisper_model: str = "small",
    research_provider: str = "serper",
    results_per_query: int = 5,
    do_research: bool = True,
) -> Path:
    """Run the end-to-end opportunity pipeline and write a single final report."""
    run_dir.mkdir(parents=True, exist_ok=True)

    social_report_path = run_social_pipeline(url, run_dir / "social", whisper_model)
    report: dict[str, Any] = json.loads(
        social_report_path.read_text(encoding="utf-8")
    )

    if do_research:
        if research_provider != "serper":
            raise ValueError(f"Unsupported research provider: {research_provider}")
        provider = SerperSearchProvider()
        research_plan = report.get("research_plan", {})
        research_bundle = collect_research(
            research_plan,
            provider,
            results_per_query=results_per_query,
            fetch_pages=True,
        )
        report["research_evidence"] = research_bundle
        report["opportunity_score"] = score_opportunity(
            _derive_score_inputs(research_bundle)
        )
    else:
        report["research_evidence"] = {
            "status": "skipped",
            "reason": "Research disabled by user/runtime option.",
        }
        report["opportunity_score"] = {
            "status": "not_scored",
            "reason": "No external evidence collected.",
        }

    report["engine_status"] = {
        "stage": "opportunity_report_generated",
        "requires_human_capital_decision": True,
        "profitability_verified": False,
    }

    output = run_dir / "opportunity-engine-report.json"
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return output
