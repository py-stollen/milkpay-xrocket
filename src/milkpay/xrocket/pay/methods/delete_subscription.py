from typing import Optional

from stollen.enums import HTTPMethod

from .base import PayXRocketMethod


class DeleteSubscription(
    PayXRocketMethod[Optional[bool]],
    http_method=HTTPMethod.DELETE,
    api_method="/subscriptions/{subscription_id}",
    returning=Optional[bool],
    response_data_key=["success"],
):
    """
    Delete subscription
    """

    subscription_id: str
