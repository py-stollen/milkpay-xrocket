from .base import PayXRocketObject


class AppBalance(PayXRocketObject):
    currency: str
    balance: int | float
