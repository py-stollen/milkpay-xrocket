from datetime import datetime
from typing import Union

from pydantic import Field

from .base import TradeXRocketObject


class LastTradesResponseDto(TradeXRocketObject):
    amount: Union[int, float]
    """Amount in quote token"""
    order_time: datetime = Field(alias="orderTime")
    """Order time"""
    price: Union[int, float]
    """Order price"""
    quantity: Union[int, float]
    """Quantity in base token"""
    side: str
    """Volume"""
