from pydantic import Field

from .base import TradeXRocketObject


class OrderEstimateRequestDto(TradeXRocketObject):
    pair_id: int | float = Field(alias="pairId")
    """Pair ID"""
    type: str
    """Order type"""
    execute_type: str = Field(alias="executeType")
    """Order execute type"""
    rate: int | float
    """Order rate"""
    amount: int | float
    """Amount"""
    currency: str
    """Amount currency"""
