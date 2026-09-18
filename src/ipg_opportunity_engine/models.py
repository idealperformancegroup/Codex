from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field


class Source(BaseModel):
    url: str
    platform: str
    creator_or_advertiser: Optional[str] = None
    captured_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Evidence(BaseModel):
    verified_facts: list[str] = []
    observable_signals: list[str] = []
    estimates: list[str] = []
    assumptions: list[str] = []
    hypotheses: list[str] = []


class BusinessModel(BaseModel):
    what_is_sold: Optional[str] = None
    customer: Optional[str] = None
    monetization: Optional[str] = None
    acquisition: Optional[str] = None
    fulfillment: Optional[str] = None


class Opportunity(BaseModel):
    problem: Optional[str] = None
    gap: Optional[str] = None
    differentiation: Optional[str] = None
    automation_advantage: Optional[str] = None
    estimated_complexity: Optional[str] = None
    estimated_capital_required: Optional[float] = None


class Experiment(BaseModel):
    test: Optional[str] = None
    budget: Optional[float] = None
    success_metric: Optional[str] = None
    kill_condition: Optional[str] = None


class OpportunityReport(BaseModel):
    source: Source
    evidence: Evidence = Field(default_factory=Evidence)
    business_model: BusinessModel = Field(default_factory=BusinessModel)
    opportunity: Opportunity = Field(default_factory=Opportunity)
    experiment: Experiment = Field(default_factory=Experiment)
