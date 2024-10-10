from typing import Optional, Union

from stollen.enums import HTTPMethod

from ..types import ExchangeOrderDto, Pagination
from .base import TradeXRocketMethod


class GetOrdersByPair(
    TradeXRocketMethod[Pagination[ExchangeOrderDto]],
    http_method=HTTPMethod.GET,
    api_method="/orders/pair/{pair}",
    returning=Pagination[ExchangeOrderDto],
    response_data_key=["data"],
):
    """
    Get list of exchange orders by pair
    """

    pair: str
    limit: Optional[Union[int, float]] = None
    offset: Optional[Union[int, float]] = None
    only_active: bool
