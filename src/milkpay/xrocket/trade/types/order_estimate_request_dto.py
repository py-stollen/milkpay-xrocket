from typing import Union

from pydantic import Field

from .base import TradeXRocketObject


class OrderEstimateRequestDto(TradeXRocketObject):
    pair_id: Union[int, float] = Field(alias="pairId")
    """Pair ID"""
    type: str
    """Order type"""
    execute_type: str = Field(alias="executeType")
    """Order execute type"""
    rate: Union[int, float]
    """Order rate"""
    amount: Union[int, float]
    """Amount"""
    currency: str
    """Amount currency"""
