from typing import Optional, Union

from pydantic import Field
from stollen.enums import HTTPMethod

from ..types import ExchangeOrderDto
from .base import TradeXRocketMethod


class CreateOrder(
    TradeXRocketMethod[ExchangeOrderDto],
    http_method=HTTPMethod.POST,
    api_method="/orders",
    returning=ExchangeOrderDto,
    response_data_key=["data"],
):
    """
    Execute order
    """

    pair: str
    """Exchange pair"""
    type: str
    """Order type"""
    execute_type: str = Field(serialization_alias="executeType")
    """Order execute type"""
    rate: Optional[Union[int, float]] = None
    """Order rate for executeType=LIMIT"""
    amount: Union[int, float]
    """Order amount"""
    currency: str
    """Amount currency"""
