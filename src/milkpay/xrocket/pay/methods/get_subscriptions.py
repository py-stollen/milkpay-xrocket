from typing import Optional

from stollen.enums import HTTPMethod

from ..types import Pagination, Subscription
from .base import PayXRocketMethod


class GetSubscriptions(
    PayXRocketMethod[Pagination[Subscription]],
    http_method=HTTPMethod.GET,
    api_method="/subscriptions",
    returning=Pagination[Subscription],
    response_data_key=["data"],
):
    """
    Get list of subscription
    """

    limit: Optional[int | float] = None
    offset: Optional[int | float] = None
