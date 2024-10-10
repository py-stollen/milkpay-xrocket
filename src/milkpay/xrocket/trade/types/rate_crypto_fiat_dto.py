from typing import Union

from pydantic import Field

from .base import TradeXRocketObject


class RateCryptoFiatDto(TradeXRocketObject):
    crypto_currency: str = Field(alias="cryptoCurrency")
    """Crypto currency"""
    fiat_currency: str = Field(alias="fiatCurrency")
    """Fiat currency"""
    rate: Union[int, float]
    """Crypto rate in fiat"""
