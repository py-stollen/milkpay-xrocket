from stollen.enums import HTTPMethod

from ..types import CryptoCurrenciesResponseDto
from .base import TradeXRocketMethod


class GetAvailableCryptoCurrencies(
    TradeXRocketMethod[CryptoCurrenciesResponseDto],
    http_method=HTTPMethod.GET,
    api_method="/rates/crypto/available",
    returning=CryptoCurrenciesResponseDto,
    response_data_key=["data"],
):
    """
    Returns available crypto currencies for exchange rates
    """
