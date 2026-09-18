from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone


@dataclass
class SearchResult:
    query: str
    title: str
    url: str
    snippet: str | None = None
    position: int | None = None

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class PageEvidence:
    url: str
    title: str | None
    text_excerpt: str
    fetched_at: str
    status_code: int
    content_type: str | None = None

    @classmethod
    def create(
        cls,
        url: str,
        title: str | None,
        text_excerpt: str,
        status_code: int,
        content_type: str | None,
    ) -> "PageEvidence":
        return cls(
            url=url,
            title=title,
            text_excerpt=text_excerpt,
            fetched_at=datetime.now(timezone.utc).isoformat(),
            status_code=status_code,
            content_type=content_type,
        )

    def to_dict(self) -> dict:
        return asdict(self)
