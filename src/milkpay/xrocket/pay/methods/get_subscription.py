from stollen.enums import HTTPMethod

from ..types import Subscription
from .base import PayXRocketMethod


class GetSubscription(
    PayXRocketMethod[Subscription],
    http_method=HTTPMethod.GET,
    api_method="/subscriptions/{subscription_id}",
    returning=Subscription,
    response_data_key=["data"],
):
    """
    Get subscription info
    """

    subscription_id: str
