from ipg_opportunity_engine.business_intelligence import extract_business_signals
from ipg_opportunity_engine.opportunity_scoring import ScoreInputs, score_opportunity


def test_extracts_source_grounded_candidates():
    text = "Tired of wasting time? Our tool helps you save hours. Get yours today for $49."
    result = extract_business_signals(text)
    assert result["hook_candidate"] == "Tired of wasting time?"
    assert "$49" in result["price_mentions"]
    assert "buy" in result["cta_candidates"]
    assert result["interpretation_status"] == "candidate_extraction_only"


def test_score_is_not_profitability_probability():
    result = score_opportunity(ScoreInputs(
        demand_evidence=8,
        ad_persistence=7,
        complaint_opportunity=6,
        margin_potential=8,
        automation_advantage=7,
        fulfillment_simplicity=7,
        competition_risk=5,
        regulatory_ip_risk=2,
    ))
    assert 0 <= result["score"] <= 100
    assert result["meaning"] == "research_priority_score_not_profitability_probability"
