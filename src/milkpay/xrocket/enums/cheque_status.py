from enum import StrEnum, auto


class ChequeStatus(StrEnum):
    ACTIVE = auto()
    COMPLETED = auto()
    DRAFT = auto()
