from datetime import datetime
from typing import Union

from pydantic import Field

from .base import TradeXRocketObject


class TimeSerieDto(TradeXRocketObject):
    open_rate: Union[int, float] = Field(alias="openRate")
    """Rate open"""
    close_rate: Union[int, float] = Field(alias="closeRate")
    """Rate close"""
    min_rate: Union[int, float] = Field(alias="minRate")
    """Min rate"""
    max_rate: Union[int, float] = Field(alias="maxRate")
    """Max rate"""
    open_time: datetime = Field(alias="openTime")
    """Open time"""
    close_time: datetime = Field(alias="closeTime")
    """Close time"""
    volume: Union[int, float]
    """Volume"""
    quote_volume: Union[int, float] = Field(alias="quoteVolume")
    """Quote volume"""
