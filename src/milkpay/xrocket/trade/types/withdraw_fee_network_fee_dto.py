from .base import TradeXRocketObject


class WithdrawFeeNetworkFeeDto(TradeXRocketObject):
    fee: int | float
    """Fee amount"""
    currency: str
    """Withdraw fee currency"""
