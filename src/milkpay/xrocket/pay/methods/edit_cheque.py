from typing import Optional

from pydantic import Field
from stollen.enums import HTTPMethod

from ..types import Cheque
from .base import PayXRocketMethod


class EditCheque(
    PayXRocketMethod[Cheque],
    http_method=HTTPMethod.PUT,
    api_method="/multi-cheque/{id}",
    returning=Cheque,
    response_data_key=["data"],
):
    """
    Edit multi-cheque
    """

    id: str
    password: Optional[str] = None
    """Password for cheque"""
    description: Optional[str] = None
    """Description for cheque"""
    send_notifications: Optional[bool] = Field(
        default=None, serialization_alias="sendNotifications"
    )
    """Send notifications about activations"""
    enable_captcha: Optional[bool] = Field(default=None, serialization_alias="enableCaptcha")
    """Enable captcha"""
    telegram_resources_ids: Optional[list[str]] = Field(
        default=None, serialization_alias="telegramResourcesIds"
    )
    """IDs of telegram resources (groups, channels, private groups)"""
    for_premium: Optional[bool] = Field(default=None, serialization_alias="forPremium")
    """Only users with Telegram Premium can activate this cheque"""
    linked_wallet: Optional[bool] = Field(default=None, serialization_alias="linkedWallet")
    """Only users with linked wallet can activate this cheque"""
    disabled_languages: Optional[list[str]] = Field(
        default=None, serialization_alias="disabledLanguages"
    )
    """Disable languages"""
