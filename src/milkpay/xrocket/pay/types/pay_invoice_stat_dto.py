from datetime import datetime
from typing import Union, Optional

from pydantic import Field

from .base import PayXRocketObject


class PayInvoiceStatDto(PayXRocketObject):
    user_id: Union[int, float] = Field(alias="userId")
    """Telegram ID of user who made transaction"""
    payment_num: Union[int, float] = Field(alias="paymentNum")
    """Num of payments in transaction"""
    payment_amount: Union[int, float] = Field(alias="paymentAmount")
    """Amount of payments in transaction"""
    comment: Optional[str] = None
    """Comment on payment"""
    paid: Optional[datetime] = None
    """When transaction was paid"""
