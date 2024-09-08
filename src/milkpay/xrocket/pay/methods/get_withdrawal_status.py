from stollen.enums import HTTPMethod

from ..types import WithdrawalDto
from .base import PayXRocketMethod


class GetWithdrawalStatus(
    PayXRocketMethod[WithdrawalDto],
    http_method=HTTPMethod.GET,
    api_method="/app/withdrawal/status/{withdrawal_id}",
    returning=WithdrawalDto,
    response_data_key=["data"],
):
    """
    Returns withdrawal status
    """

    withdrawal_id: str
