from typing import Union

from .base import TradeXRocketObject


class WithdrawFeeNetworkFeeDto(TradeXRocketObject):
    fee: Union[int, float]
    """Fee amount"""
    currency: str
    """Withdraw fee currency"""
