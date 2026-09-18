from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass
class UnitEconomicsAssumptions:
    selling_price: float
    product_or_fulfillment_cost: float
    payment_fees: float = 0
    shipping_cost: float = 0
    support_cost: float = 0
    estimated_cac: float | None = None
    refund_rate: float = 0


def calculate_unit_economics(x: UnitEconomicsAssumptions) -> dict:
    if x.selling_price <= 0:
        raise ValueError("selling_price must be positive")
    if not 0 <= x.refund_rate <= 1:
        raise ValueError("refund_rate must be between 0 and 1")
    realized_revenue = x.selling_price * (1 - x.refund_rate)
    variable_cost = (
        x.product_or_fulfillment_cost + x.payment_fees
        + x.shipping_cost + x.support_cost
    )
    pre_acquisition_contribution = realized_revenue - variable_cost
    post_acquisition_contribution = (
        None if x.estimated_cac is None
        else pre_acquisition_contribution - x.estimated_cac
    )
    return {
        "assumptions": asdict(x),
        "realized_revenue_after_refund_assumption": round(realized_revenue, 2),
        "variable_cost_before_acquisition": round(variable_cost, 2),
        "contribution_before_acquisition": round(pre_acquisition_contribution, 2),
        "contribution_after_acquisition": (
            None if post_acquisition_contribution is None
            else round(post_acquisition_contribution, 2)
        ),
        "status": "scenario_not_verified_financial_result",
    }
