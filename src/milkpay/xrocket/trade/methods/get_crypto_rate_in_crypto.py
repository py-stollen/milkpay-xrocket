from stollen.enums import HTTPMethod

from ..types import RateCryptoCryptoDto
from .base import TradeXRocketMethod


class GetCryptoRateInCrypto(
    TradeXRocketMethod[RateCryptoCryptoDto],
    http_method=HTTPMethod.GET,
    api_method="/rates/crypto/{base}/{quote}",
    returning=RateCryptoCryptoDto,
    response_data_key=["data"],
):
    """
    Returns rate crypto currency in crypto
    """

    base: str
    quote: str
