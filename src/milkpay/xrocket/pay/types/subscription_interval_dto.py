from typing import Union

from .base import PayXRocketObject


class SubscriptionIntervalDto(PayXRocketObject):
    interval: str
    """Interval for subscription"""
    amount: Union[int, float]
    """Cost subscription for current interval in currency"""
    status: str
    """Status for subscription"""
