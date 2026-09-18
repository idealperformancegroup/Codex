from __future__ import annotations

from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from .research_types import PageEvidence


DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; IPGOpportunityResearch/0.1; "
        "+https://github.com/idealperformancegroup/Codex)"
    )
}


def fetch_page_evidence(url: str, timeout: int = 20, max_chars: int = 12000) -> PageEvidence:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        raise ValueError("Only http/https URLs are supported")

    response = requests.get(
        url,
        headers=DEFAULT_HEADERS,
        timeout=timeout,
        allow_redirects=True,
    )
    response.raise_for_status()
    content_type = response.headers.get("content-type")
    title = None
    text = ""

    if content_type and "html" in content_type.lower():
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style", "noscript", "svg"]):
            tag.decompose()
        title = soup.title.get_text(" ", strip=True) if soup.title else None
        text = " ".join(soup.stripped_strings)
    else:
        text = response.text

    return PageEvidence.create(
        url=response.url,
        title=title,
        text_excerpt=text[:max_chars],
        status_code=response.status_code,
        content_type=content_type,
    )
