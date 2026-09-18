from ipg_opportunity_engine.economics import UnitEconomicsAssumptions, calculate_unit_economics
from ipg_opportunity_engine.market_intelligence import CompetitorEvidence, summarize_competitors
from ipg_opportunity_engine.review_mining import ReviewEvidence, mine_reviews


def test_competitor_price_range_is_observed_only():
    result = summarize_competitors([
        CompetitorEvidence("A", "https://a.test", price=49, acquisition_channel="meta"),
        CompetitorEvidence("B", "https://b.test", price=79, acquisition_channel="meta"),
    ])
    assert result["observed_price_range"]["min"] == 49
    assert result["observed_price_range"]["max"] == 79
    assert result["status"] == "observed_evidence_not_market_share"


def test_review_theme_requires_recurrence():
    result = mine_reviews([
        ReviewEvidence("https://a.test/1", "Shipping was late."),
        ReviewEvidence("https://a.test/2", "Delivery was late again."),
        ReviewEvidence("https://a.test/3", "Great quality."),
    ])
    themes = [x["theme"] for x in result["recurring_themes"]]
    assert "shipping_delivery" in themes
    assert "quality" not in themes


def test_unit_economics_scenario():
    result = calculate_unit_economics(UnitEconomicsAssumptions(
        selling_price=100, product_or_fulfillment_cost=30,
        payment_fees=3, shipping_cost=7, estimated_cac=20, refund_rate=.1
    ))
    assert result["contribution_after_acquisition"] == 30
    assert result["status"] == "scenario_not_verified_financial_result"
