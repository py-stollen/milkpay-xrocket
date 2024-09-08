from stollen.enums import HTTPMethod

from ..types import UserFeesResponseDto
from .base import TradeXRocketMethod


class GetFees(
    TradeXRocketMethod[UserFeesResponseDto],
    http_method=HTTPMethod.GET,
    api_method="/account/fees",
    returning=UserFeesResponseDto,
    response_data_key=["data"],
):
    """
    Returns current user fees
    """
