from pydantic import Field

from .base import TradeXRocketObject


class OrderBookOrderDto(TradeXRocketObject):
    type: str
    """Order type"""
    rate: int | float
    """Order rate"""
    value: int | float
    """Order base value"""
    quote_value: int | float = Field(alias="quoteValue")
    """Order quote value"""
