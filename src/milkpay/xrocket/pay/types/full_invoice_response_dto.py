from .base import PayXRocketObject


class FullInvoiceResponseDto(PayXRocketObject):
    success: bool
    """indicate if request is successful"""
