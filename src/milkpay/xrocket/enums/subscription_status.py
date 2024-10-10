from enum import Enum


class SubscriptionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    ARCHIVE = "ARCHIVE"
    DELETED = "DELETED"
