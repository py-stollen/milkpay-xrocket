from .base import TradeXRocketObject


class ResponsePaginatedDto(TradeXRocketObject):
    success: bool
    """Indicate if request is successful"""
    total: int | float
    """Total times"""
    limit: int | float
    offset: int | float
