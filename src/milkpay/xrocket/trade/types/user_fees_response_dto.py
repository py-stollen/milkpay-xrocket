from pydantic import Field

from .base import TradeXRocketObject


class UserFeesResponseDto(TradeXRocketObject):
    buy_taker: int | float = Field(alias="buyTaker")
    """Buy taker fee"""
    sell_taker: int | float = Field(alias="sellTaker")
    """Sell taker fee"""
    buy_maker: int | float = Field(alias="buyMaker")
    """Buy maker fee"""
    sell_maker: int | float = Field(alias="sellMaker")
    """Sell maker fee"""
