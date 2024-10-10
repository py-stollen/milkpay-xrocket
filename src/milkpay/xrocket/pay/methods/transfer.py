from typing import Optional, Union

from pydantic import Field
from stollen.enums import HTTPMethod

from ..types import TransferDto
from .base import PayXRocketMethod


class Transfer(
    PayXRocketMethod[TransferDto],
    http_method=HTTPMethod.POST,
    api_method="/app/transfer",
    returning=TransferDto,
    response_data_key=["data"],
):
    """
    Make transfer of funds to another user
    """

    tg_user_id: Union[int, float] = Field(serialization_alias="tgUserId")
    """Telegram user ID. If we dont have this user in DB, we will fail transaction with error: 400 - User not found"""
    currency: str
    """Currency of transfer, info /currencies/available"""
    amount: Union[int, float]
    """Transfer amount. 9 decimal places, others cut off"""
    transfer_id: str = Field(serialization_alias="transferId")
    """Unique transfer ID in your system to prevent double spends"""
    description: Optional[str] = None
    """Transfer description"""
