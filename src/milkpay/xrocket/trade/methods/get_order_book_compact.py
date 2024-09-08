from stollen.enums import HTTPMethod

from ..types import OrderBookFullDto
from .base import TradeXRocketMethod


class GetOrderBookCompact(
    TradeXRocketMethod[OrderBookFullDto],
    http_method=HTTPMethod.GET,
    api_method="/order-book/compact/{pair}",
    returning=OrderBookFullDto,
    response_data_key=["data"],
):
    """
    Returns full order book for pair
    """

    pair: str
