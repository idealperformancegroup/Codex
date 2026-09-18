from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, asdict
from typing import Iterable


@dataclass
class ReviewEvidence:
    source_url: str
    text: str
    rating: float | None = None
    product_or_company: str | None = None


THEMES = {
    "price_value": r"\b(expensive|overpriced|price|value|worth)\b",
    "quality": r"\b(quality|cheap|broke|broken|durable|flimsy)\b",
    "shipping_delivery": r"\b(shipping|delivery|late|arrived|package)\b",
    "support": r"\b(customer service|support|refund|return|response)\b",
    "ease_of_use": r"\b(easy|difficult|hard to use|confusing|setup)\b",
    "performance": r"\b(works|worked|doesn't work|failed|effective|results)\b",
}


def mine_reviews(reviews: Iterable[ReviewEvidence]) -> dict:
    rows = [asdict(r) for r in reviews]
    counts: Counter[str] = Counter()
    examples: dict[str, list[dict]] = {k: [] for k in THEMES}
    for row in rows:
        text = row["text"]
        for theme, pattern in THEMES.items():
            if re.search(pattern, text, re.I):
                counts[theme] += 1
                if len(examples[theme]) < 3:
                    examples[theme].append({
                        "source_url": row["source_url"],
                        "text": text[:300],
                        "rating": row["rating"],
                    })
    recurring = [
        {"theme": theme, "mentions": count, "examples": examples[theme]}
        for theme, count in counts.most_common()
        if count >= 2
    ]
    return {
        "review_count": len(rows),
        "theme_counts": dict(counts),
        "recurring_themes": recurring,
        "status": "descriptive_review_evidence",
        "warning": "Themes are not causal claims and samples may not represent all customers.",
    }
