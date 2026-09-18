from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, asdict
from typing import Iterable


@dataclass
class CompetitorEvidence:
    name: str
    source_url: str
    offer: str | None = None
    price: float | None = None
    currency: str = "USD"
    acquisition_channel: str | None = None
    observed_ad_signal: str | None = None


def summarize_competitors(items: Iterable[CompetitorEvidence]) -> dict:
    rows = [asdict(x) for x in items]
    prices = [x["price"] for x in rows if x["price"] is not None]
    channels = Counter(
        x["acquisition_channel"] for x in rows if x["acquisition_channel"]
    )
    return {
        "competitors": rows,
        "observed_price_range": {
            "min": min(prices) if prices else None,
            "max": max(prices) if prices else None,
            "sample_size": len(prices),
        },
        "observed_acquisition_channels": dict(channels),
        "evidence_count": len(rows),
        "status": "observed_evidence_not_market_share",
    }
