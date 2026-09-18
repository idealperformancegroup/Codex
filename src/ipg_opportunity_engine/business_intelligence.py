from __future__ import annotations

import re
from collections import Counter
from typing import Any


CTA_PATTERNS = {
    "buy": r"\b(buy|order|shop|get yours)\b",
    "learn_more": r"\b(learn more|find out more|see how)\b",
    "signup": r"\b(sign up|register|join|subscribe)\b",
    "book": r"\b(book|schedule|reserve)\b",
    "download": r"\b(download|get the guide|get the app)\b",
    "comment_dm": r"\b(comment|dm me|message me|send me)\b",
}

MONEY_PATTERNS = [
    re.compile(r"\$\s?\d+(?:[,.]\d{1,2})?"),
    re.compile(r"\b\d+(?:\.\d+)?\s?(?:dollars|usd)\b", re.I),
]


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def extract_business_signals(transcript: str) -> dict[str, Any]:
    """Extract conservative, source-grounded business signals from transcript text.

    This layer deliberately labels candidates rather than asserting inferred truth.
    """
    text = transcript.strip()
    lower = text.lower()
    sentences = _sentences(text)

    prices: list[str] = []
    for pattern in MONEY_PATTERNS:
        prices.extend(pattern.findall(text))

    ctas = [
        name for name, pattern in CTA_PATTERNS.items()
        if re.search(pattern, lower, flags=re.I)
    ]

    hook = sentences[0] if sentences else None
    claims = [
        s for s in sentences
        if re.search(r"\b(save|make|earn|increase|reduce|faster|better|guarantee|proven|results?)\b", s, re.I)
    ]
    problem_candidates = [
        s for s in sentences
        if re.search(r"\b(problem|struggle|tired of|hate|difficult|hard to|waste|losing|can't|cannot)\b", s, re.I)
    ]

    words = re.findall(r"[a-zA-Z][a-zA-Z'-]{2,}", lower)
    stop = {
        "the","and","that","this","with","you","your","for","are","was","have",
        "from","they","but","not","can","will","just","our","what","how","get",
        "all","out","about","into","when","then","than","who","why"
    }
    keywords = [w for w, _ in Counter(w for w in words if w not in stop).most_common(12)]

    return {
        "hook_candidate": hook,
        "price_mentions": sorted(set(prices)),
        "cta_candidates": ctas,
        "claim_candidates": claims[:10],
        "problem_candidates": problem_candidates[:10],
        "keywords": keywords,
        "interpretation_status": "candidate_extraction_only",
    }


def build_business_intelligence(transcript: dict[str, Any], visual_analysis: dict[str, Any] | None = None) -> dict[str, Any]:
    text = transcript.get("text", "") if transcript else ""
    extracted = extract_business_signals(text)
    return {
        "source_grounded_signals": extracted,
        "offer": {
            "what_is_sold": None,
            "price": extracted["price_mentions"],
            "promise": extracted["claim_candidates"],
            "cta": extracted["cta_candidates"],
        },
        "customer": {
            "problem_candidates": extracted["problem_candidates"],
            "target_customer": None,
        },
        "creative_structure": {
            "hook": extracted["hook_candidate"],
            "proof": [],
            "objections": [],
            "mechanism": None,
        },
        "visual_context": visual_analysis or {},
        "research_questions": [
            "Is there independent evidence of demand for this category?",
            "Which comparable offers have repeated or long-running advertising?",
            "What complaints recur in customer reviews?",
            "What are realistic price, gross-margin, and fulfillment ranges?",
            "What can IPG differentiate without copying protected intellectual property?",
        ],
        "status": "requires_market_validation",
    }
