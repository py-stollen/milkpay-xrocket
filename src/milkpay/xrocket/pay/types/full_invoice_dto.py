from datetime import datetime
from typing import Optional, Union

from pydantic import Field

from .base import PayXRocketObject
from .pay_invoice_stat_dto import PayInvoiceStatDto


class FullInvoiceDto(PayXRocketObject):
    id: Union[int, float]
    """Invoice ID"""
    amount: Union[int, float]
    """Amount of invoice"""
    min_payment: Optional[Union[int, float]] = Field(default=None, alias="minPayment")
    """Min payment of invoice"""
    total_activations: Union[int, float] = Field(alias="totalActivations")
    """Total activations of invoice"""
    activations_left: Union[int, float] = Field(alias="activationsLeft")
    """Activations left of invoice"""
    description: Optional[str] = None
    """Invoice description"""
    hidden_message: Optional[str] = Field(default=None, alias="hiddenMessage")
    """Message that will be displayed after invoice payment"""
    payload: Optional[str] = None
    """Any data that is attached to invoice"""
    callback_url: Optional[str] = Field(default=None, alias="callbackUrl")
    """url that will be set for Return button after invoice is paid"""
    comments_enabled: Optional[bool] = Field(default=None, alias="commentsEnabled")
    """Allow comments for invoice"""
    currency: str
    created: datetime
    """When invoice was created"""
    paid: Optional[datetime] = None
    """When invoice was paid"""
    status: str
    expired_in: Optional[Union[int, float]] = Field(default=None, alias="expiredIn")
    """Invoice expire time in seconds, max 1 day, 0 - none expired"""
    link: str
    payments: list[PayInvoiceStatDto]
    """Payment stat of invoice"""
