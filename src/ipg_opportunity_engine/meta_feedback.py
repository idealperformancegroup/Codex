from __future__ import annotations

from statistics import mean
from typing import Any


def summarize_performance(rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not rows:
        return {"status": "no_data", "ads": 0}
    spend = sum(x.get("spend", 0) for x in rows)
    revenue = sum(x.get("revenue", 0) for x in rows)
    impressions = sum(x.get("impressions", 0) for x in rows)
    clicks = sum(x.get("clicks", 0) for x in rows)
    weighted_ctr = (clicks / impressions * 100) if impressions else 0
    return {
        "status": "observed_account_performance",
        "ads": len(rows),
        "spend": round(spend, 2),
        "revenue": round(revenue, 2),
        "roas": round(revenue / spend, 3) if spend else 0,
        "impressions": impressions,
        "clicks": clicks,
        "ctr": round(weighted_ctr, 3),
        "average_cpc": round(mean([x["cpc"] for x in rows if x.get("cpc") is not None]), 3) if rows else 0,
        "note": "Performance differences are observational; audience, offer, placement, timing, and attribution can confound creative comparisons.",
    }


def creative_learning(rows: list[dict[str, Any]], top_n: int = 5) -> dict[str, Any]:
    ranked = sorted(rows, key=lambda x: (x.get("roas", 0), x.get("spend", 0)), reverse=True)
    winners = ranked[:top_n]
    losers = sorted(rows, key=lambda x: (x.get("roas", 0), -x.get("spend", 0)))[:top_n]
    return {
        "top_observed_ads": winners,
        "weak_observed_ads": losers,
        "interpretation": "Use these as hypothesis inputs for the next creative test, not as proof of causation.",
    }
