from stollen.enums import HTTPMethod

from ..types import AccountBalancesDto
from .base import TradeXRocketMethod


class GetBalances(
    TradeXRocketMethod[AccountBalancesDto],
    http_method=HTTPMethod.GET,
    api_method="/account/balance",
    returning=AccountBalancesDto,
    response_data_key=["data"],
):
    """
    Returns current balances of you account
    """
