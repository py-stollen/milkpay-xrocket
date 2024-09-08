from stollen.enums import HTTPMethod

from ..types import FullInvoiceDto
from .base import PayXRocketMethod


class GetInvoice(
    PayXRocketMethod[FullInvoiceDto],
    http_method=HTTPMethod.GET,
    api_method="/tg-invoices/{id}",
    returning=FullInvoiceDto,
    response_data_key=["data"],
):
    """
    Get invoice info
    """

    id: str
