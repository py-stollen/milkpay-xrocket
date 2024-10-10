from typing import Union

from .base import PayXRocketObject


class WithdrawFeeNetworkFeeDto(PayXRocketObject):
    fee: Union[int, float]
    """Fee amount"""
    currency: str
    """Withdraw fee currency"""
