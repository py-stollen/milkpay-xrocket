from enum import Enum


class InvoiceStatus(str, Enum):
    ACTIVE = "active"
    PAID = "paid"
    EXPIRED = "expired"
