from typing import Union

from pydantic import Field

from .base import TradeXRocketObject


class UserFeesResponseDto(TradeXRocketObject):
    buy_taker: Union[int, float] = Field(alias="buyTaker")
    """Buy taker fee"""
    sell_taker: Union[int, float] = Field(alias="sellTaker")
    """Sell taker fee"""
    buy_maker: Union[int, float] = Field(alias="buyMaker")
    """Buy maker fee"""
    sell_maker: Union[int, float] = Field(alias="sellMaker")
    """Sell maker fee"""
