from stollen.enums import HTTPMethod

from ..types import PairDto
from .base import TradeXRocketMethod


class GetPair(
    TradeXRocketMethod[PairDto],
    http_method=HTTPMethod.GET,
    api_method="/pairs/{pair}",
    returning=PairDto,
    response_data_key=["data"],
):
    """
    Return pair by base/quote coin on Rocket Exchange
    """

    pair: str
