from stollen.enums import HTTPMethod

from ..types import ShortChequeDto
from .base import PayXRocketMethod


class GetCheque(
    PayXRocketMethod[ShortChequeDto],
    http_method=HTTPMethod.GET,
    api_method="/multi-cheque/{id}",
    returning=ShortChequeDto,
    response_data_key=["data"],
):
    """
    Get multi-cheque info
    """

    id: str
