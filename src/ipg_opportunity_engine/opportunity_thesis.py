from __future__ import annotations

from typing import Any


def build_opportunity_thesis(
    business_intelligence: dict[str, Any],
    market_intelligence: dict[str, Any],
    review_intelligence: dict[str, Any],
) -> dict[str, Any]:
    recurring = review_intelligence.get("recurring_themes", [])
    gaps = [
        f"Investigate whether recurring '{x['theme']}' complaints can be solved."
        for x in recurring
    ]
    return {
        "signal": business_intelligence.get("source_grounded_signals", {}),
        "market_evidence": {
            "competitor_count": market_intelligence.get("evidence_count", 0),
            "observed_price_range": market_intelligence.get("observed_price_range", {}),
            "channels": market_intelligence.get("observed_acquisition_channels", {}),
        },
        "customer_evidence": {
            "review_count": review_intelligence.get("review_count", 0),
            "recurring_themes": recurring,
        },
        "gap_hypotheses": gaps,
        "decision": "research_more",
        "decision_reason": "A human decision requires sourced demand and economics evidence.",
        "next_test": None,
    }
