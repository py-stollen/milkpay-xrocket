from typing import Union

from .base import PayXRocketObject


class AppBalance(PayXRocketObject):
    currency: str
    balance: Union[int, float]
