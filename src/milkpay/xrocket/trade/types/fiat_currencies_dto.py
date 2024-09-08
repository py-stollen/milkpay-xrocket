from .base import TradeXRocketObject


class FiatCurrenciesDto(TradeXRocketObject):
    currencies: list[str]
    """Fiat currencies"""
