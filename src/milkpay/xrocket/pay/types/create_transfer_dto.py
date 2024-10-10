from typing import Optional, Union

from pydantic import Field

from .base import PayXRocketObject


class CreateTransferDto(PayXRocketObject):
    tg_user_id: Union[int, float] = Field(alias="tgUserId")
    """Telegram user ID. If we dont have this user in DB, we will fail transaction with error: 400 - User not found"""
    currency: str
    """Currency of transfer, info /currencies/available"""
    amount: Union[int, float]
    """Transfer amount. 9 decimal places, others cut off"""
    transfer_id: str = Field(alias="transferId")
    """Unique transfer ID in your system to prevent double spends"""
    description: Optional[str] = None
    """Transfer description"""
