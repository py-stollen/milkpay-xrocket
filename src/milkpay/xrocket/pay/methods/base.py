from stollen import StollenMethod
from stollen.types import StollenT

from ..client import PayXRocket


class PayXRocketMethod(StollenMethod[StollenT, PayXRocket], abstract=True):
    pass
