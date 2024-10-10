from typing import Optional, Union

from pydantic import Field

from .base import PayXRocketObject


class TransferDto(PayXRocketObject):
    id: Union[int, float]
    """Transfer ID"""
    tg_user_id: Union[int, float] = Field(alias="tgUserId")
    """Telegram user ID"""
    currency: str
    """Currency code"""
    amount: Union[int, float]
    """Transfer amount. 9 decimal places, others cut off"""
    description: Optional[str] = None
    """Transfer description"""
