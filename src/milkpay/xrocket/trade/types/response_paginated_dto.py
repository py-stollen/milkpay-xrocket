from typing import Union

from .base import TradeXRocketObject


class ResponsePaginatedDto(TradeXRocketObject):
    success: bool
    """Indicate if request is successful"""
    total: Union[int, float]
    """Total times"""
    limit: Union[int, float]
    offset: Union[int, float]
