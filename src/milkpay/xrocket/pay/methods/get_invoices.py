from typing import Optional, Union

from stollen.enums import HTTPMethod

from ..types import InvoiceDto, Pagination
from .base import PayXRocketMethod


class GetInvoices(
    PayXRocketMethod[Pagination[InvoiceDto]],
    http_method=HTTPMethod.GET,
    api_method="/tg-invoices",
    returning=Pagination[InvoiceDto],
    response_data_key=["data"],
):
    """
    Get list of invoices
    """

    limit: Optional[Union[int, float]] = None
    offset: Optional[Union[int, float]] = None
