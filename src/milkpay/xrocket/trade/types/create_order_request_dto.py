from typing import Optional

from pydantic import Field

from .base import TradeXRocketObject


class CreateOrderRequestDto(TradeXRocketObject):
    pair: str
    """Exchange pair"""
    type: str
    """Order type"""
    execute_type: str = Field(alias="executeType")
    """Order execute type"""
    rate: Optional[int | float] = None
    """Order rate for executeType=LIMIT"""
    amount: int | float
    """Order amount"""
    currency: str
    """Amount currency"""
