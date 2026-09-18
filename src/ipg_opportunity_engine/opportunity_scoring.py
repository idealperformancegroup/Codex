from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass
class ScoreInputs:
    demand_evidence: float = 0
    ad_persistence: float = 0
    complaint_opportunity: float = 0
    margin_potential: float = 0
    automation_advantage: float = 0
    fulfillment_simplicity: float = 0
    competition_risk: float = 0
    regulatory_ip_risk: float = 0

    def validate(self) -> None:
        for name, value in asdict(self).items():
            if not 0 <= value <= 10:
                raise ValueError(f"{name} must be between 0 and 10")


def score_opportunity(inputs: ScoreInputs) -> dict:
    """Transparent 0-100 research score, never a profitability claim."""
    inputs.validate()
    positive = (
        inputs.demand_evidence * 0.25
        + inputs.ad_persistence * 0.15
        + inputs.complaint_opportunity * 0.15
        + inputs.margin_potential * 0.15
        + inputs.automation_advantage * 0.15
        + inputs.fulfillment_simplicity * 0.15
    )
    risk_penalty = (
        inputs.competition_risk * 0.10
        + inputs.regulatory_ip_risk * 0.15
    )
    raw = max(0.0, min(10.0, positive - risk_penalty))
    return {
        "score": round(raw * 10, 1),
        "scale": "0-100",
        "inputs": asdict(inputs),
        "meaning": "research_priority_score_not_profitability_probability",
        "missing_evidence_warning": any(v == 0 for v in asdict(inputs).values()),
    }
