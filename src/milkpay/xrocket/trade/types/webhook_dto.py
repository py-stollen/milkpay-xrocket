from datetime import datetime

from .base import TradeXRocketObject


class WebhookDto(TradeXRocketObject):
    type: str
    """type of webhook sent"""
    timestamp: datetime
    """When webhook was sent"""
