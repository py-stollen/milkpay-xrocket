from typing import Optional

from pydantic import Field

from .base import TradeXRocketObject


class OrderEstimateDto(TradeXRocketObject):
    pair_id: int | float = Field(alias="pairId")
    """Pair ID"""
    in_amount: int | float = Field(alias="inAmount")
    """In amount"""
    rate: int | float
    """Order rate"""
    base_amount: int | float = Field(alias="baseAmount")
    """Base amount"""
    quote_amount: int | float = Field(alias="quoteAmount")
    """Quote amount"""
    return_amount: Optional[int | float] = Field(default=None, alias="returnAmount")
    """Return to balance, only for MARKET"""
    fee: int | float
    """Order fee"""
