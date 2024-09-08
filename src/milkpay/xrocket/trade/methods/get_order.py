from stollen.enums import HTTPMethod

from ..types import ExchangeOrderDto
from .base import TradeXRocketMethod


class GetOrder(
    TradeXRocketMethod[ExchangeOrderDto],
    http_method=HTTPMethod.GET,
    api_method="/orders/{id}",
    returning=ExchangeOrderDto,
    response_data_key=["data"],
):
    """
    Get exchange order
    """

    id: str
