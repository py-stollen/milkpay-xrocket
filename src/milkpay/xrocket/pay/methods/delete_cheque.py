from typing import Optional

from stollen.enums import HTTPMethod

from .base import PayXRocketMethod


class DeleteCheque(
    PayXRocketMethod[Optional[bool]],
    http_method=HTTPMethod.DELETE,
    api_method="/multi-cheque/{id}",
    returning=Optional[bool],
    response_data_key=["success"],
):
    """
    Delete multi-cheque
    """

    id: str
