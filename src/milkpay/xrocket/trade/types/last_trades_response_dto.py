from datetime import datetime

from pydantic import Field

from .base import TradeXRocketObject


class LastTradesResponseDto(TradeXRocketObject):
    amount: int | float
    """Amount in quote token"""
    order_time: datetime = Field(alias="orderTime")
    """Order time"""
    price: int | float
    """Order price"""
    quantity: int | float
    """Quantity in base token"""
    side: str
    """Volume"""
