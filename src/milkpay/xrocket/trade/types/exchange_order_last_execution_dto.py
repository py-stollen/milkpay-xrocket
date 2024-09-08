from pydantic import Field

from .base import TradeXRocketObject


class ExchangeOrderLastExecutionDto(TradeXRocketObject):
    main_amount: int | float = Field(alias="mainAmount")
    """Current base amount"""
    secondary_amount: int | float = Field(alias="secondaryAmount")
    """Current quote amount"""
    fee: int | float
    """Execution fee"""
    rate: int | float
    """Execution rate"""
