from typing import Union

from stollen.enums import HTTPMethod

from ..types import SubscriptionInterval
from .base import PayXRocketMethod


class CreateSubscriptionInterval(
    PayXRocketMethod[SubscriptionInterval],
    http_method=HTTPMethod.POST,
    api_method="/subscriptions/{subscription_id}/interval",
    returning=SubscriptionInterval,
    response_data_key=["data"],
):
    """
    Create subscription interval
    """

    subscription_id: str
    interval: str
    """Interval for subscription"""
    amount: Union[int, float]
    """Cost subscription for current interval in currency"""
    status: str
    """Status for subscription"""
