from enum import Enum


class OrderExecuteType(str, Enum):
    LIMIT = "LIMIT"
    MARKET = "MARKET"
