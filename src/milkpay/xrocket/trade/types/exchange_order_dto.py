from datetime import datetime
from typing import Optional, Union

from pydantic import Field

from .base import TradeXRocketObject
from .exchange_order_balance_dto import ExchangeOrderBalanceDto
from .exchange_order_filled_balance_dto import ExchangeOrderFilledBalanceDto
from .exchange_order_last_execution_dto import ExchangeOrderLastExecutionDto


class ExchangeOrderDto(TradeXRocketObject):
    order_id: Union[int, float] = Field(alias="orderId")
    """Order ID"""
    pair: str
    """Pair name"""
    type: str
    """Order type"""
    execute_type: str = Field(alias="executeType")
    """Order execute type"""
    status: str
    """Order status"""
    rate: Union[int, float]
    """Rate"""
    main_amount: Union[int, float] = Field(alias="mainAmount")
    """Init main amount"""
    secondary_amount: Union[int, float] = Field(alias="secondaryAmount")
    """Init secondary amount"""
    filled: Union[int, float]
    """Filled percent"""
    balance: ExchangeOrderBalanceDto
    """Now order balance"""
    filled_balance: ExchangeOrderFilledBalanceDto = Field(alias="filledBalance")
    """Filled order balance"""
    last_execution: Optional[ExchangeOrderLastExecutionDto] = Field(
        default=None, alias="lastExecution"
    )
    """Last execution, for webhook only"""
    created: datetime
    """Created date"""
    closed: datetime
    """Closed date"""
