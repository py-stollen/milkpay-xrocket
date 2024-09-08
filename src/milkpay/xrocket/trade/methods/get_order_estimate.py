from pydantic import Field
from stollen.enums import HTTPMethod

from ..types import OrderEstimateDto
from .base import TradeXRocketMethod


class GetOrderEstimate(
    TradeXRocketMethod[OrderEstimateDto],
    http_method=HTTPMethod.POST,
    api_method="/orders/estimate",
    returning=OrderEstimateDto,
    response_data_key=["data"],
):
    """
    Returns order estimate
    """

    pair_id: int | float = Field(serialization_alias="pairId")
    """Pair ID"""
    type: str
    """Order type"""
    execute_type: str = Field(serialization_alias="executeType")
    """Order execute type"""
    rate: int | float
    """Order rate"""
    amount: int | float
    """Amount"""
    currency: str
    """Amount currency"""
