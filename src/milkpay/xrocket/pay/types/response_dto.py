from .base import PayXRocketObject


class ResponseDto(PayXRocketObject):
    success: bool
    """indicate if request is successful"""
