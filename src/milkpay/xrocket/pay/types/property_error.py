from .base import PayXRocketObject


class PropertyError(PayXRocketObject):
    property: str
    """name of input field that cannot be processed"""
    error: str
    """text explaining what exactly wrong"""
