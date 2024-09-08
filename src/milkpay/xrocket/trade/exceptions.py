from stollen.exceptions import StollenAPIError


class TradeXRocketError(StollenAPIError):
    pass


class UnknownAPIKeyError(TradeXRocketError):
    pass
