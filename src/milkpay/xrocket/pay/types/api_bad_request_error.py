from typing import Optional

from .base import PayXRocketObject
from .property_error import PropertyError


class ApiBadRequestError(PayXRocketObject):
    success: bool
    message: str
    errors: Optional[list[PropertyError]] = None
