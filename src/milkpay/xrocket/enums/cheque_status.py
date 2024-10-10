from enum import Enum


class ChequeStatus(str, Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    DRAFT = "draft"
