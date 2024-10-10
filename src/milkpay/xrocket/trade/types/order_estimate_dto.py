from typing import Optional, Union

from pydantic import Field

from .base import TradeXRocketObject


class OrderEstimateDto(TradeXRocketObject):
    pair_id: Union[int, float] = Field(alias="pairId")
    """Pair ID"""
    in_amount: Union[int, float] = Field(alias="inAmount")
    """In amount"""
    rate: Union[int, float]
    """Order rate"""
    base_amount: Union[int, float] = Field(alias="baseAmount")
    """Base amount"""
    quote_amount: Union[int, float] = Field(alias="quoteAmount")
    """Quote amount"""
    return_amount: Optional[Union[int, float]] = Field(default=None, alias="returnAmount")
    """Return to balance, only for MARKET"""
    fee: Union[int, float]
    """Order fee"""
