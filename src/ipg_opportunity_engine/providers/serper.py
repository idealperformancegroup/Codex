from __future__ import annotations

import os

import requests

from ..research_types import SearchResult


class SerperSearchProvider:
    """Optional Google-search adapter via Serper.

    Requires SERPER_API_KEY. The rest of the engine is provider-agnostic.
    """

    endpoint = "https://google.serper.dev/search"

    def __init__(self, api_key: str | None = None, timeout: int = 20):
        self.api_key = api_key or os.getenv("SERPER_API_KEY")
        self.timeout = timeout
        if not self.api_key:
            raise RuntimeError("SERPER_API_KEY is required for SerperSearchProvider")

    def search(self, query: str, limit: int = 5) -> list[SearchResult]:
        response = requests.post(
            self.endpoint,
            headers={
                "X-API-KEY": self.api_key,
                "Content-Type": "application/json",
            },
            json={"q": query, "num": limit},
            timeout=self.timeout,
        )
        response.raise_for_status()
        data = response.json()
        results: list[SearchResult] = []
        for index, item in enumerate(data.get("organic", [])[:limit], start=1):
            url = item.get("link")
            title = item.get("title")
            if not url or not title:
                continue
            results.append(
                SearchResult(
                    query=query,
                    title=title,
                    url=url,
                    snippet=item.get("snippet"),
                    position=item.get("position", index),
                )
            )
        return results
