from __future__ import annotations

import json
from typing import Any

from bs4 import BeautifulSoup

from .review_mining import ReviewEvidence


def _walk_jsonld(value: Any):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from _walk_jsonld(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk_jsonld(child)


def extract_jsonld_reviews(html: str, source_url: str) -> list[ReviewEvidence]:
    """Extract Schema.org Review objects when a public page exposes them in JSON-LD."""
    soup = BeautifulSoup(html, "html.parser")
    reviews: list[ReviewEvidence] = []

    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        raw = script.string or script.get_text()
        if not raw.strip():
            continue
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            continue

        for node in _walk_jsonld(payload):
            node_type = node.get("@type")
            types = node_type if isinstance(node_type, list) else [node_type]
            if "Review" not in types:
                continue

            body = node.get("reviewBody") or node.get("description")
            if not body:
                continue

            rating = None
            rating_obj = node.get("reviewRating")
            if isinstance(rating_obj, dict):
                try:
                    rating = float(rating_obj.get("ratingValue"))
                except (TypeError, ValueError):
                    rating = None

            item = node.get("itemReviewed")
            product = item.get("name") if isinstance(item, dict) else None

            reviews.append(
                ReviewEvidence(
                    source_url=source_url,
                    text=str(body),
                    rating=rating,
                    product_or_company=product,
                )
            )
    return reviews
