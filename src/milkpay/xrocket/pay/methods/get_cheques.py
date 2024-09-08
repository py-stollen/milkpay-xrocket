from typing import Optional

from stollen.enums import HTTPMethod

from ..types import Pagination, ShortChequeDto
from .base import PayXRocketMethod


class GetCheques(
    PayXRocketMethod[Pagination[ShortChequeDto]],
    http_method=HTTPMethod.GET,
    api_method="/multi-cheque",
    returning=Pagination[ShortChequeDto],
    response_data_key=["data"],
):
    """
    Get list of multi-cheques
    """

    limit: Optional[int | float] = None
    offset: Optional[int | float] = None
