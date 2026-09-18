from ipg_opportunity_engine.social_intelligence import detect_platform, create_signal_report


def test_platform_detection():
    assert detect_platform("https://www.instagram.com/reel/abc") == "instagram"
    assert detect_platform("https://www.facebook.com/reel/abc") == "facebook"
    assert detect_platform("https://www.tiktok.com/@x/video/1") == "tiktok"
    assert detect_platform("https://youtu.be/abc") == "youtube"
    assert detect_platform("https://x.com/user/status/1") == "x"


def test_signal_is_not_profitability_claim():
    report = create_signal_report("https://www.instagram.com/reel/abc")
    assert report.source.platform == "instagram"
    assert any("profitability" in s.lower() for s in report.evidence.observable_signals)
