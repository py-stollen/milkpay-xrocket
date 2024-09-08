from typing import Optional

from stollen.enums import HTTPMethod

from .base import TradeXRocketMethod


class CancelOrder(
    TradeXRocketMethod[Optional[bool]],
    http_method=HTTPMethod.DELETE,
    api_method="/orders/{id}",
    returning=Optional[bool],
    response_data_key=["success"],
):
    """
    Cancel exchange order
    """

    id: str
