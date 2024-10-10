from enum import Enum


class WithdrawalStatus(str, Enum):
    CREATED = "CREATED"
    COMPLETED = "COMPLETED"
    FAIL = "FAIL"
