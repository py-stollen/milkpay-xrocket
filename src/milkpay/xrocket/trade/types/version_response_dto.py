from typing import Union

from .base import TradeXRocketObject


class VersionResponseDto(TradeXRocketObject):
    version: Union[int, float]
