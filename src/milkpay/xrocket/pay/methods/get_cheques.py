from typing import Optional, Union

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

    limit: Optional[Union[int, float]] = None
    offset: Optional[Union[int, float]] = None
