from typing import Optional, Union

from pydantic import Field

from .base import PayXRocketObject


class AppCreateWithdrawalDto(PayXRocketObject):
    network: str
    """Network code"""
    address: str
    """Withdrawal address"""
    currency: str
    """Currency code"""
    amount: Union[int, float]
    """Withdrawal amount. 9 decimal places, others cut off"""
    withdrawal_id: str = Field(alias="withdrawalId")
    """Unique withdrawal ID in your system to prevent double spends"""
    comment: Optional[str] = None
    """Withdrawal comment"""
