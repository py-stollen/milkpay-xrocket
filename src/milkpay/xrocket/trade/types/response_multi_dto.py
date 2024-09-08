from .base import TradeXRocketObject


class ResponseMultiDto(TradeXRocketObject):
    success: bool
    """Indicate if request is successful"""
