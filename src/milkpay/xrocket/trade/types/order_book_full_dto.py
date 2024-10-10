from typing import Union

from pydantic import Field

from .base import TradeXRocketObject
from .order_book_order_dto import OrderBookOrderDto


class OrderBookFullDto(TradeXRocketObject):
    pair: str
    """Pair name"""
    sell_count: Union[int, float] = Field(alias="sellCount")
    """Count sell orders"""
    buy_count: Union[int, float] = Field(alias="buyCount")
    """Count buy orders"""
    sell: list[OrderBookOrderDto]
    """List of sell orders"""
    buy: list[OrderBookOrderDto]
    """List of buy orders"""
