from typing import Union

from pydantic import Field

from .base import PayXRocketObject


class SubscriptionResource(PayXRocketObject):
    id: Union[int, float]
    """Resource ID"""
    type: str
    """Resource type"""
    resource_id: str = Field(alias="resourceId")
    """Resource TG ID"""
    name: str
    """Resource TG title"""
    linked_chat: str = Field(alias="linkedChat")
    """Resource TG ID"""
