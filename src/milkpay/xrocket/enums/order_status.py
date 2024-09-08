from enum import StrEnum


class OrderStatus(StrEnum):
    CREATED = "CREATED"
    CANCELLED = "CANCELLED"
    EXECUTED = "EXECUTED"
    PARTIALLY = "PARTIALLY"
