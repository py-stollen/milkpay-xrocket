from typing import Optional, Union

from pydantic import Field

from .base import PayXRocketObject
from .subscription_interval import SubscriptionInterval
from .subscription_resource import SubscriptionResource


class Subscription(PayXRocketObject):
    id: Union[int, float]
    """Subscription ID"""
    name: str
    """Subscription name"""
    description: Optional[str] = None
    """Subscription description"""
    currency: str
    """Subscription currency"""
    link: str
    """Link to subscription"""
    interval: SubscriptionInterval
    """Subscription interval"""
    referral_percent: Union[int, float] = Field(alias="referralPercent")
    """Subscription referral percent"""
    return_url: Optional[str] = Field(default=None, alias="returnUrl")
    """Return link after payment"""
    tg_resource: Optional[SubscriptionResource] = Field(default=None, alias="tgResource")
    """TG Resource for subscription"""
