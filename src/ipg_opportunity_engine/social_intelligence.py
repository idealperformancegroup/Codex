from __future__ import annotations

from urllib.parse import urlparse

from .models import OpportunityReport, Source


def detect_platform(url: str) -> str:
    host = urlparse(url).netloc.lower()
    if "instagram.com" in host:
        return "instagram"
    if "facebook.com" in host or "fb.watch" in host:
        return "facebook"
    if "tiktok.com" in host:
        return "tiktok"
    if "youtube.com" in host or "youtu.be" in host:
        return "youtube"
    if "x.com" in host or "twitter.com" in host:
        return "x"
    return "unknown"


def create_signal_report(url: str) -> OpportunityReport:
    platform = detect_platform(url)
    report = OpportunityReport(source=Source(url=url, platform=platform))
    report.evidence.observable_signals.append(
        "Source captured for analysis; profitability has not been established."
    )
    report.evidence.assumptions.append(
        "Further transcription, visual analysis, and market research are required."
    )
    return report
