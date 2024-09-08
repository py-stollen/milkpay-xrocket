from datetime import datetime
from typing import Optional

from pydantic import Field

from .base import TradeXRocketObject


class PairDto(TradeXRocketObject):
    name: str
    """Pair name"""
    last_price: int | float = Field(alias="lastPrice")
    """Last price"""
    sell_price: int | float = Field(alias="sellPrice")
    """Best sell price"""
    buy_price: int | float = Field(alias="buyPrice")
    """Best buy price"""
    main_volume24h: int | float = Field(alias="mainVolume24h")
    """Volume in base currency, 24h"""
    quote_volume24h: int | float = Field(alias="quoteVolume24h")
    """Volume in quote currency, 24h"""
    min_main: int | float = Field(alias="minMain")
    """Min main value for exchange"""
    min_secondary: int | float = Field(alias="minSecondary")
    """Min secondary value for exchange"""
    rate_max_decimals: int | float = Field(alias="rateMaxDecimals")
    """Max decimals for rate"""
    is_open: bool = Field(alias="isOpen")
    """Indicate if trades open"""
    open24h: int | float
    """Open 24h rate"""
    main_decimals: int | float = Field(alias="mainDecimals")
    """Decimals main"""
    secondary_decimals: int | float = Field(alias="secondaryDecimals")
    """Decimals secondary"""
    open_time: Optional[datetime] = Field(default=None, alias="openTime")
    """Indicate time open trades"""
