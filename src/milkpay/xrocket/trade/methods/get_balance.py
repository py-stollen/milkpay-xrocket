from stollen.enums import HTTPMethod

from ..types import AccountBalanceDto
from .base import TradeXRocketMethod


class GetBalance(
    TradeXRocketMethod[AccountBalanceDto],
    http_method=HTTPMethod.GET,
    api_method="/account/balance/{coin}",
    returning=AccountBalanceDto,
    response_data_key=["data"],
):
    """
    Returns current balance of you account for coin
    """

    coin: str
