from typing import Optional

from stollen.enums import HTTPMethod

from .base import PayXRocketMethod


class GetVersion(
    PayXRocketMethod[Optional[bool]],
    http_method=HTTPMethod.GET,
    api_method="/version",
    returning=Optional[bool],
    response_data_key=["success"],
):
    """
    Returns current version of API. You may use it as healthcheck
    """
