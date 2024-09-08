from typing import Optional

from stollen.enums import HTTPMethod

from .base import PayXRocketMethod


class DeleteInvoice(
    PayXRocketMethod[Optional[bool]],
    http_method=HTTPMethod.DELETE,
    api_method="/tg-invoices/{id}",
    returning=Optional[bool],
    response_data_key=["success"],
):
    """
    Delete invoice
    """

    id: str
