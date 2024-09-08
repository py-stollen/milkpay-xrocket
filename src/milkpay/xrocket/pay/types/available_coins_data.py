from .base import PayXRocketObject
from .coin_dto import CoinDto


class AvailableCoinsData(PayXRocketObject):
    results: list[CoinDto]
