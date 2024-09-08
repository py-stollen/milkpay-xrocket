from stollen.enums import HTTPMethod

from ..types import AvailableCoinsData
from .base import PayXRocketMethod


class GetCoins(
    PayXRocketMethod[AvailableCoinsData],
    http_method=HTTPMethod.GET,
    api_method="/currencies/available",
    returning=AvailableCoinsData,
    response_data_key=["data"],
):
    """
    Returns available currencies
    """
