from typing import Optional, Union

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

    limit: Optional[Union[int, float]] = None
    offset: Optional[Union[int, float]] = None
