from typing import Optional, Union

from pydantic import Field
from stollen.enums import HTTPMethod

from ..types import WithdrawalResponseDto
from .base import TradeXRocketMethod


class Withdrawal(
    TradeXRocketMethod[WithdrawalResponseDto],
    http_method=HTTPMethod.POST,
    api_method="/account/withdrawal",
    returning=WithdrawalResponseDto,
    response_data_key=["data"],
):
    """
    Make withdrawal of funds to external wallet
    """

    network: str
    """Network code"""
    address: str
    """Withdrawal address"""
    currency: str
    """Currency code"""
    amount: Union[int, float]
    """Withdrawal amount. 9 decimal places, others cut off"""
    withdrawal_id: str = Field(serialization_alias="withdrawalId")
    """Unique withdrawal ID in your system to prevent double spends"""
    comment: Optional[str] = None
    """Withdrawal comment"""
