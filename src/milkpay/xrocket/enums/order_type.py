from enum import Enum


class OrderType(str, Enum):
    SELL = "SELL"
    BUY = "BUY"
