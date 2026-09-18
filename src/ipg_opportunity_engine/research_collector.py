from __future__ import annotations

from dataclasses import asdict
from typing import Any

from .http_collector import fetch_page_evidence
from .providers.base import SearchProvider


def collect_research(
    research_plan: dict[str, Any],
    provider: SearchProvider,
    results_per_query: int = 5,
    fetch_pages: bool = True,
) -> dict[str, Any]:
    """Execute planned queries, preserve URLs, and optionally fetch source excerpts."""
    queries = [q for q in research_plan.get("market_queries", []) if q]
    search_results = []
    seen_urls: set[str] = set()

    for query in queries:
        for result in provider.search(query, limit=results_per_query):
            if result.url in seen_urls:
                continue
            seen_urls.add(result.url)
            search_results.append(result)

    pages = []
    errors = []
    if fetch_pages:
        for result in search_results:
            try:
                pages.append(fetch_page_evidence(result.url))
            except Exception as exc:
                errors.append({
                    "url": result.url,
                    "error": type(exc).__name__,
                    "message": str(exc)[:500],
                })

    return {
        "queries": queries,
        "search_results": [r.to_dict() for r in search_results],
        "pages": [p.to_dict() for p in pages],
        "errors": errors,
        "status": "collected_uninterpreted_evidence",
    }
