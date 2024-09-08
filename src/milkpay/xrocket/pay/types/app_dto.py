from .app import App
from .base import PayXRocketObject


class AppDto(PayXRocketObject):
    success: bool
    """indicate if request is successful"""
    data: App
