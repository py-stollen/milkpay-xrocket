from pydantic import Field

from .base import TradeXRocketObject


class AccountBalanceDto(TradeXRocketObject):
    code: str
    """Crypto code"""
    amount: int | float
    """Amount crypto"""
    locked_in_orders: int | float = Field(alias="lockedInOrders")
    """Amount locked in exchange orders"""
