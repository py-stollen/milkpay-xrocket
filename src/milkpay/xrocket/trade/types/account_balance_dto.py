from typing import Union

from pydantic import Field

from .base import TradeXRocketObject


class AccountBalanceDto(TradeXRocketObject):
    code: str
    """Crypto code"""
    amount: Union[int, float]
    """Amount crypto"""
    locked_in_orders: Union[int, float] = Field(alias="lockedInOrders")
    """Amount locked in exchange orders"""
