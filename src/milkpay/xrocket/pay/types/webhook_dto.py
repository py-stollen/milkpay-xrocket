from datetime import datetime

from .base import PayXRocketObject


class WebhookDto(PayXRocketObject):
    type: str
    """type of webhook sent"""
    timestamp: datetime
    """When webhook was sent"""
