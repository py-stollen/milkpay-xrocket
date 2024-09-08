from typing import Optional

from pydantic import Field

from .base import PayXRocketObject


class UpdateChequeDto(PayXRocketObject):
    password: Optional[str] = None
    """Password for cheque"""
    description: Optional[str] = None
    """Description for cheque"""
    send_notifications: Optional[bool] = Field(default=None, alias="sendNotifications")
    """Send notifications about activations"""
    enable_captcha: Optional[bool] = Field(default=None, alias="enableCaptcha")
    """Enable captcha"""
    telegram_resources_ids: Optional[list[str]] = Field(default=None, alias="telegramResourcesIds")
    """IDs of telegram resources (groups, channels, private groups)"""
    for_premium: Optional[bool] = Field(default=None, alias="forPremium")
    """Only users with Telegram Premium can activate this cheque"""
    linked_wallet: Optional[bool] = Field(default=None, alias="linkedWallet")
    """Only users with linked wallet can activate this cheque"""
    disabled_languages: Optional[list[str]] = Field(default=None, alias="disabledLanguages")
    """Disable languages"""
