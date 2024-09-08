from datetime import datetime

from pydantic import Field

from .base import TradeXRocketObject


class TimeSerieDto(TradeXRocketObject):
    open_rate: int | float = Field(alias="openRate")
    """Rate open"""
    close_rate: int | float = Field(alias="closeRate")
    """Rate close"""
    min_rate: int | float = Field(alias="minRate")
    """Min rate"""
    max_rate: int | float = Field(alias="maxRate")
    """Max rate"""
    open_time: datetime = Field(alias="openTime")
    """Open time"""
    close_time: datetime = Field(alias="closeTime")
    """Close time"""
    volume: int | float
    """Volume"""
    quote_volume: int | float = Field(alias="quoteVolume")
    """Quote volume"""
