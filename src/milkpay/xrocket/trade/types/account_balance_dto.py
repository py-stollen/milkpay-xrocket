from typing import Union

from pydantic import Field

from .base import TradeXRocketObject


class AccountBalanceDto(TradeXRocketObject):
    code: str
    """Crypto code"""
    amount: Union[int, float]
    """Amount crypto"""
    locked_in_orders: Union[int, float, None] = Field(alias="lockedInOrders", default=None)
    """Amount locked in exchange orders"""
