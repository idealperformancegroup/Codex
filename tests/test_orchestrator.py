from pathlib import Path

from ipg_opportunity_engine.orchestrator import _derive_score_inputs


def test_derive_score_inputs_are_conservative():
    score = _derive_score_inputs({
        "search_results": [{"url": "a"}] * 6,
        "pages": [{"url": "a"}] * 3,
    })
    assert score.demand_evidence == 3
    assert score.ad_persistence == 1
    assert score.margin_potential == 0
    assert score.complaint_opportunity == 0
