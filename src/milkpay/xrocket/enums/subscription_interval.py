from enum import Enum


class SubscriptionInterval(str, Enum):
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    YEAR = "YEAR"
    FOREVER = "FOREVER"
