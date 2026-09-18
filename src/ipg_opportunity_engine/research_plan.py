from __future__ import annotations

from typing import Any


def build_research_plan(business_intelligence: dict[str, Any]) -> dict[str, Any]:
    signals = business_intelligence.get("source_grounded_signals", {})
    keywords = signals.get("keywords", [])
    problems = business_intelligence.get("customer", {}).get("problem_candidates", [])
    return {
        "market_queries": [
            f"{' '.join(keywords[:5])} market competitors".strip(),
            f"{' '.join(keywords[:5])} customer reviews complaints".strip(),
            f"{' '.join(keywords[:5])} pricing alternatives".strip(),
        ],
        "review_questions": [
            "What do buyers praise repeatedly?",
            "What do buyers complain about repeatedly?",
            "What causes refunds, churn, returns, or low ratings?",
            "What feature or service do customers repeatedly ask for?",
        ],
        "economics_questions": [
            "Observed selling-price range",
            "Estimated landed/delivery cost with source",
            "Gross-margin range with assumptions shown",
            "Customer-acquisition-cost evidence when available",
            "Fulfillment, return, support, and compliance burden",
        ],
        "problem_language": problems,
        "required_evidence": {
            "demand": "At least two independent demand signals",
            "competition": "Named comparable offers with source URLs",
            "complaints": "Recurring review themes, not isolated anecdotes",
            "economics": "Explicit assumptions and source-backed ranges",
        },
    }
