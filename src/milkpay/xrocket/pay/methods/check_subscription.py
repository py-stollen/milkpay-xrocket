from typing import Union

from pydantic import Field
from stollen.enums import HTTPMethod

from ..types import UserSubscription
from .base import PayXRocketMethod


class CheckSubscription(
    PayXRocketMethod[UserSubscription],
    http_method=HTTPMethod.POST,
    api_method="/subscriptions/check/{subscription_id}",
    returning=UserSubscription,
    response_data_key=["data"],
):
    subscription_id: str
    user_id: Union[int, float] = Field(serialization_alias="userId")
    """TG User id"""
