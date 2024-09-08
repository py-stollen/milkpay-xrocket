from typing import Optional

from stollen.enums import HTTPMethod

from ..types import WithdrawalCoinResponseDto
from .base import TradeXRocketMethod


class GetWithdrawalFees(
    TradeXRocketMethod[list[WithdrawalCoinResponseDto]],
    http_method=HTTPMethod.GET,
    api_method="/account/withdrawal/fees",
    returning=list[WithdrawalCoinResponseDto],
    response_data_key=["data"],
):
    """
    Returns withdrawal fees
    """

    currency: Optional[str] = None
