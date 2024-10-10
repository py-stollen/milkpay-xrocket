from typing import Optional, Union

from pydantic import Field

from .base import PayXRocketObject
from .withdraw_fee_dto import WithdrawFeeDto


class CoinDto(PayXRocketObject):
    currency: str
    """ID of currency, use in Rocket Pay Api"""
    name: str
    """Name of currency"""
    min_transfer: Union[int, float] = Field(alias="minTransfer")
    """Minimal amount for transfer"""
    min_cheque: Union[int, float] = Field(alias="minCheque")
    """Minimal amount for cheque"""
    min_invoice: Union[int, float] = Field(alias="minInvoice")
    """Minimal amount for invoice"""
    min_withdraw: Union[int, float] = Field(alias="minWithdraw")
    """Minimal amount for withdrawals"""
    fee_withdraw: Optional[WithdrawFeeDto] = Field(default=None, alias="feeWithdraw")
    """Fee for token withdrawals in main currency"""
