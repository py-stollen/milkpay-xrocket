from typing import Optional

from stollen.enums import HTTPMethod

from .base import TradeXRocketMethod


class GetVersion(
    TradeXRocketMethod[Optional[bool]],
    http_method=HTTPMethod.GET,
    api_method="/version",
    returning=Optional[bool],
    response_data_key=["success"],
):
    """
    Returns current version of API. You may use it as healthcheck
    """
