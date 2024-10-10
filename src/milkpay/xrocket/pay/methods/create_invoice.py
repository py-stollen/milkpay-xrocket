from typing import Optional, Union

from pydantic import Field
from stollen.enums import HTTPMethod

from ..types import InvoiceDto
from .base import PayXRocketMethod


class CreateInvoice(
    PayXRocketMethod[InvoiceDto],
    http_method=HTTPMethod.POST,
    api_method="/tg-invoices",
    returning=InvoiceDto,
    response_data_key=["data"],
):
    """
    Create invoice
    """

    amount: Optional[Union[int, float]] = None
    """Invoice amount. 9 decimal places, others cut off"""
    min_payment: Optional[Union[int, float]] = Field(
        default=None, serialization_alias="minPayment"
    )
    """Min payment only for multi invoice if invoice amount is null"""
    num_payments: Union[int, float] = Field(serialization_alias="numPayments")
    """Num payments for invoice"""
    currency: str
    """Currency of transfer, info /currencies/available"""
    description: Optional[str] = None
    """Description for invoice"""
    hidden_message: Optional[str] = Field(default=None, serialization_alias="hiddenMessage")
    """Hidden message after invoice is paid"""
    comments_enabled: Optional[bool] = Field(default=None, serialization_alias="commentsEnabled")
    """Allow comments"""
    callback_url: Optional[str] = Field(default=None, serialization_alias="callbackUrl")
    """Url for Return button after invoice is paid"""
    payload: Optional[str] = None
    """Any data. Invisible to user, will be returned in callback"""
    expired_in: Optional[Union[int, float]] = Field(default=None, serialization_alias="expiredIn")
    """Invoice expire time in seconds, max 1 day, 0 - none expired"""
