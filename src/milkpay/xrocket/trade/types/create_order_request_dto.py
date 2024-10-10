from typing import Optional, Union

from pydantic import Field

from .base import TradeXRocketObject


class CreateOrderRequestDto(TradeXRocketObject):
    pair: str
    """Exchange pair"""
    type: str
    """Order type"""
    execute_type: str = Field(alias="executeType")
    """Order execute type"""
    rate: Optional[Union[int, float]] = None
    """Order rate for executeType=LIMIT"""
    amount: Union[int, float]
    """Order amount"""
    currency: str
    """Amount currency"""
