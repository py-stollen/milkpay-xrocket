from .available_coins_data import AvailableCoinsData
from .base import PayXRocketObject


class AvailableCoins(PayXRocketObject):
    success: bool
    """indicate if request is successful"""
    data: AvailableCoinsData
