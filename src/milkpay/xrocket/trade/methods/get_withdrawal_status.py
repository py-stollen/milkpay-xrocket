from stollen.enums import HTTPMethod

from ..types import WithdrawalResponseDto
from .base import TradeXRocketMethod


class GetWithdrawalStatus(
    TradeXRocketMethod[WithdrawalResponseDto],
    http_method=HTTPMethod.GET,
    api_method="/account/withdrawal/status/{withdrawal_id}",
    returning=WithdrawalResponseDto,
    response_data_key=["data"],
):
    """
    Returns withdrawal status
    """

    withdrawal_id: str
