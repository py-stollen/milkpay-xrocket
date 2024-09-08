from pydantic import Field

from .base import TradeXRocketObject
from .time_serie_dto import TimeSerieDto


class TimeSeriesDto(TradeXRocketObject):
    pair: str
    """Pair name"""
    time_series: list[TimeSerieDto] = Field(alias="timeSeries")
    """Rate open"""
