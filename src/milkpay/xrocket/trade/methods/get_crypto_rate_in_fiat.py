from stollen.enums import HTTPMethod

from ..types import RateCryptoFiatDto
from .base import TradeXRocketMethod


class GetCryptoRateInFiat(
    TradeXRocketMethod[RateCryptoFiatDto],
    http_method=HTTPMethod.GET,
    api_method="/rates/fiat/{crypto}/{fiat}",
    returning=RateCryptoFiatDto,
    response_data_key=["data"],
):
    """
    Returns rate crypto currency in fiat
    """

    crypto: str
    fiat: str
