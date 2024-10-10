from datetime import datetime
from typing import Union

from pydantic import Field

from .base import PayXRocketObject
from .user_subscription_transaction import UserSubscriptionTransaction


class UserSubscription(PayXRocketObject):
    subscription_id: Union[int, float] = Field(alias="subscriptionId")
    """Subscription id for this payment"""
    subscription_code: str = Field(alias="subscriptionCode")
    """Subscription code for this payment"""
    user_id: Union[int, float] = Field(alias="userId")
    """TG user ID who pay subscription"""
    amount: Union[int, float]
    """Sum all payments which added to app balance"""
    currency: str
    """Subscription currency"""
    interval: str
    """Payed interval"""
    ref_fee: Union[int, float] = Field(alias="refFee")
    """Sum all referral rewards"""
    is_ref_pay: bool = Field(alias="isRefPay")
    """This payment by ref link"""
    total_amount: Union[int, float] = Field(alias="totalAmount")
    """Sum all payments which user pay"""
    payment_start: datetime = Field(alias="paymentStart")
    """When subscribe start"""
    payment_end: datetime = Field(alias="paymentEnd")
    """When subscribe ends"""
    auto_renewal: bool = Field(alias="autoRenewal")
    """Is auto renewal"""
    transactions: list[UserSubscriptionTransaction]
    """Payments for this user"""
