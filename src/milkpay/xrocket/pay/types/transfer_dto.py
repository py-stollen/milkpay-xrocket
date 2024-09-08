from typing import Optional

from pydantic import Field

from .base import PayXRocketObject


class TransferDto(PayXRocketObject):
    id: int | float
    """Transfer ID"""
    tg_user_id: int | float = Field(alias="tgUserId")
    """Telegram user ID"""
    currency: str
    """Currency code"""
    amount: int | float
    """Transfer amount. 9 decimal places, others cut off"""
    description: Optional[str] = None
    """Transfer description"""
