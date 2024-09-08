from .base import PayXRocketObject


class ApiError(PayXRocketObject):
    success: bool
    message: str
