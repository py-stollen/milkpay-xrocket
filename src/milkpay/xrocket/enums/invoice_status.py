from enum import StrEnum, auto


class InvoiceStatus(StrEnum):
    ACTIVE = auto()
    PAID = auto()
    EXPIRED = auto()
