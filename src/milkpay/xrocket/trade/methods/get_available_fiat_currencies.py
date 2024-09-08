from stollen.enums import HTTPMethod

from ..types import FiatCurrenciesDto
from .base import TradeXRocketMethod


class GetAvailableFiatCurrencies(
    TradeXRocketMethod[FiatCurrenciesDto],
    http_method=HTTPMethod.GET,
    api_method="/rates/fiat/available",
    returning=FiatCurrenciesDto,
    response_data_key=["data"],
):
    """
    Returns available fiat currencies for exchange rates
    """
