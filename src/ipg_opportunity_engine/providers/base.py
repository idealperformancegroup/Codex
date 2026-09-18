from __future__ import annotations

from typing import Protocol

from ..research_types import SearchResult


class SearchProvider(Protocol):
    def search(self, query: str, limit: int = 5) -> list[SearchResult]:
        ...
