from typing import Optional

from .base import TradeXRocketObject


class WithdrawalFeesRequestDto(TradeXRocketObject):
    currency: Optional[str] = None
    """Coin for get fees, optional"""
