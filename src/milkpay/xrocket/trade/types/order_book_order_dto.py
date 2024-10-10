from typing import Union

from pydantic import Field

from .base import TradeXRocketObject


class OrderBookOrderDto(TradeXRocketObject):
    type: str
    """Order type"""
    rate: Union[int, float]
    """Order rate"""
    value: Union[int, float]
    """Order base value"""
    quote_value: Union[int, float] = Field(alias="quoteValue")
    """Order quote value"""
