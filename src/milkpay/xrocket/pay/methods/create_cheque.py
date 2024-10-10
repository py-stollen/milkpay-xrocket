from typing import Optional, Union

from pydantic import Field
from stollen.enums import HTTPMethod

from ..types import Cheque
from .base import PayXRocketMethod


class CreateCheque(
    PayXRocketMethod[Cheque],
    http_method=HTTPMethod.POST,
    api_method="/multi-cheque",
    returning=Cheque,
    response_data_key=["data"],
):
    """
    Create multi-cheque
    """

    currency: str
    """Currency of transfer, info /currencies/available"""
    cheque_per_user: Union[int, float] = Field(serialization_alias="chequePerUser")
    """Cheque amount for one user. 9 decimal places, others cut off"""
    users_number: Union[int, float] = Field(serialization_alias="usersNumber")
    """Number of users to save multicheque. 0 decimal places"""
    ref_program: Union[int, float] = Field(serialization_alias="refProgram")
    """Referral program percentage (%). 0 decimal places"""
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
