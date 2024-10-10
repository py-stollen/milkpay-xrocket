from typing import Optional, Union

from pydantic import Field

from .base import TradeXRocketObject


class WithdrawalResponseDto(TradeXRocketObject):
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
    status: Optional[str] = None
    """Withdrawal status"""
    tx_hash: Optional[str] = Field(default=None, alias="txHash")
    """Withdrawal TX hash. Provided only after withdrawal"""
    tx_link: Optional[str] = Field(default=None, alias="txLink")
    """Withdrawal TX link. Provided only after withdrawal"""
