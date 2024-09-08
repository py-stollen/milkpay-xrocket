from stollen import StollenMethod
from stollen.types import StollenT

from ..client import TradeXRocket


class TradeXRocketMethod(StollenMethod[StollenT, TradeXRocket], abstract=True):
    pass
