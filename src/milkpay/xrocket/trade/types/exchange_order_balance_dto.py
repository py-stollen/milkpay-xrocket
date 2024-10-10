from typing import Union

from pydantic import Field

from .base import TradeXRocketObject


class ExchangeOrderBalanceDto(TradeXRocketObject):
    main_amount: Union[int, float] = Field(alias="mainAmount")
    """Current base amount"""
    secondary_amount: Union[int, float] = Field(alias="secondaryAmount")
    """Current quote amount"""
