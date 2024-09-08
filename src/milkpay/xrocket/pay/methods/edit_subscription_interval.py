from stollen.enums import HTTPMethod

from ..types import SubscriptionInterval
from .base import PayXRocketMethod


class EditSubscriptionInterval(
    PayXRocketMethod[SubscriptionInterval],
    http_method=HTTPMethod.PUT,
    api_method="/subscriptions/{subscription_id}/interval/{interval_code}",
    returning=SubscriptionInterval,
    response_data_key=["data"],
):
    """
    Edit subscription interval
    """

    subscription_id: str
    interval_code: str
    status: str
    """Status for subscription"""
