from stollen.enums import HTTPMethod

from ..types import App
from .base import PayXRocketMethod


class GetAppInfo(
    PayXRocketMethod[App],
    http_method=HTTPMethod.GET,
    api_method="/app/info",
    returning=App,
    response_data_key=["data"],
):
    """
    Returns information about your application
    """
