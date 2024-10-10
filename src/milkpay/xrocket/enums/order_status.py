from enum import Enum


class OrderStatus(str, Enum):
    CREATED = "CREATED"
    CANCELLED = "CANCELLED"
    EXECUTED = "EXECUTED"
    PARTIALLY = "PARTIALLY"
