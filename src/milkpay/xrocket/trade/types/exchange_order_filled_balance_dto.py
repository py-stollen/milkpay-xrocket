from pydantic import Field

from .base import TradeXRocketObject


class ExchangeOrderFilledBalanceDto(TradeXRocketObject):
    main_amount: int | float = Field(alias="mainAmount")
    """Current base amount"""
    secondary_amount: int | float = Field(alias="secondaryAmount")
    """Current quote amount"""
