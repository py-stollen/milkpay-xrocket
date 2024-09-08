from typing import Optional

from pydantic import Field

from .base import PayXRocketObject


class TgResource(PayXRocketObject):
    telegram_id: str = Field(alias="telegramId")
    name: str
    username: Optional[str] = None
