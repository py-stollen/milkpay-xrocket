from stollen.exceptions import StollenAPIError


class PayXRocketError(StollenAPIError):
    pass


class UnknownAPIKeyError(PayXRocketError):
    pass
