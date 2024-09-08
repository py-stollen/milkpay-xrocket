from enum import StrEnum


class SubscriptionStatus(StrEnum):
    ACTIVE = "ACTIVE"
    ARCHIVE = "ARCHIVE"
    DELETED = "DELETED"
