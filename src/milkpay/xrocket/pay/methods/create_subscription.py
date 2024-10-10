from typing import Optional, Union

from pydantic import Field
from stollen.enums import HTTPMethod

from ..types import Subscription, SubscriptionIntervalDto
from .base import PayXRocketMethod


class CreateSubscription(
    PayXRocketMethod[Subscription],
    http_method=HTTPMethod.POST,
    api_method="/subscriptions",
    returning=Subscription,
    response_data_key=["data"],
):
    """
    Create subscription
    """

    name: Optional[str] = None
    """Subscription name, view in bot"""
    description: Optional[str] = None
    """Subscription description, view in bot"""
    currency: str
    """Subscription currency"""
    interval: list[SubscriptionIntervalDto]
    """Subscription interval"""
    tg_resource: Optional[str] = Field(default=None, serialization_alias="tgResource")
    """Subscription TG resource"""
    referral_percent: Union[int, float] = Field(serialization_alias="referralPercent")
    """Subscription referral percent"""
    return_url: Optional[str] = Field(default=None, serialization_alias="returnUrl")
    """Return link after payment"""
