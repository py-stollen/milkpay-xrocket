from .base import PayXRocketObject


class ResponseMultiDto(PayXRocketObject):
    success: bool
    """Indicate if request is successful"""
