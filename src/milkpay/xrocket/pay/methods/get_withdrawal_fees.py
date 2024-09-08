from typing import Optional

from stollen.enums import HTTPMethod

from ..types import WithdrawalCoinResponseDto
from .base import PayXRocketMethod


class GetWithdrawalFees(
    PayXRocketMethod[list[WithdrawalCoinResponseDto]],
    http_method=HTTPMethod.GET,
    api_method="/app/withdrawal/fees",
    returning=list[WithdrawalCoinResponseDto],
    response_data_key=["data"],
):
    """
    Returns withdrawal fees
    """

    currency: Optional[str] = None
