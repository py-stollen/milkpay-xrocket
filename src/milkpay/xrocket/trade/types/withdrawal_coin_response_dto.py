from typing import Union

from pydantic import Field

from .base import TradeXRocketObject
from .withdrawal_coin_fees_response_dto import WithdrawalCoinFeesResponseDto


class WithdrawalCoinResponseDto(TradeXRocketObject):
    code: str
    """Crypto code"""
    min_withdraw: Union[int, float] = Field(alias="minWithdraw")
    """Minimal amount for withdrawals"""
    fees: list[WithdrawalCoinFeesResponseDto]
    """Fees"""
