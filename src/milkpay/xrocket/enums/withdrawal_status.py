from enum import StrEnum


class WithdrawalStatus(StrEnum):
    CREATED = "CREATED"
    COMPLETED = "COMPLETED"
    FAIL = "FAIL"
