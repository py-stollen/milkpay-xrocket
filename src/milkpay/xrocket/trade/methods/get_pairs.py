from stollen.enums import HTTPMethod

from ..types import PairDto
from .base import TradeXRocketMethod


class GetPairs(
    TradeXRocketMethod[list[PairDto]],
    http_method=HTTPMethod.GET,
    api_method="/pairs",
    returning=list[PairDto],
    response_data_key=["data"],
):
    """
    Returns available pairs on Rocket Exchange
    """
