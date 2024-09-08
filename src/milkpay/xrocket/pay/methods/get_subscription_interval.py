from stollen.enums import HTTPMethod

from ..types import SubscriptionInterval
from .base import PayXRocketMethod


class GetSubscriptionInterval(
    PayXRocketMethod[SubscriptionInterval],
    http_method=HTTPMethod.GET,
    api_method="/subscriptions/{subscription_id}/interval/{interval_code}",
    returning=SubscriptionInterval,
    response_data_key=["data"],
):
    """
    Get subscription interval info
    """

    subscription_id: str
    interval_code: str
