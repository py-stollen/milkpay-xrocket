from .base import TradeXRocketObject


class ResponseSingleDto(TradeXRocketObject):
    success: bool
    """Indicate if request is successful"""
