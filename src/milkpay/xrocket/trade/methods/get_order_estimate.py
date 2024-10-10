from typing import Union

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

    pair_id: Union[int, float] = Field(serialization_alias="pairId")
    """Pair ID"""
    type: str
    """Order type"""
    execute_type: str = Field(serialization_alias="executeType")
    """Order execute type"""
    rate: Union[int, float]
    """Order rate"""
    amount: Union[int, float]
    """Amount"""
    currency: str
    """Amount currency"""
