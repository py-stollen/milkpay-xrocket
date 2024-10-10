from typing import Optional, Union

from stollen.enums import HTTPMethod

from ..types import LastTradesResponseDto
from .base import TradeXRocketMethod


class GetLastTrades(
    TradeXRocketMethod[list[LastTradesResponseDto]],
    http_method=HTTPMethod.GET,
    api_method="/trades/last/{pair}",
    returning=list[LastTradesResponseDto],
    response_data_key=["data"],
):
    """
    Get last trades by pair
    """

    pair: str
    limit: Optional[Union[int, float]] = None
