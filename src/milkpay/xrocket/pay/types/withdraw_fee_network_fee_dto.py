from .base import PayXRocketObject


class WithdrawFeeNetworkFeeDto(PayXRocketObject):
    fee: int | float
    """Fee amount"""
    currency: str
    """Withdraw fee currency"""
