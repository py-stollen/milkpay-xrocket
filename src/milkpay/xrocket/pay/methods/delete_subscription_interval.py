from stollen.enums import HTTPMethod

from ..types import SubscriptionInterval
from .base import PayXRocketMethod


class DeleteSubscriptionInterval(
    PayXRocketMethod[SubscriptionInterval],
    http_method=HTTPMethod.DELETE,
    api_method="/subscriptions/{subscription_id}/interval/{interval_code}",
    returning=SubscriptionInterval,
    response_data_key=["data"],
):
    """
    Delete subscription interval
    """

    subscription_id: str
    interval_code: str
