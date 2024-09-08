from stollen.enums import HTTPMethod

from ..types import TimeSeriesDto
from .base import TradeXRocketMethod


class GetTimeSeries(
    TradeXRocketMethod[TimeSeriesDto],
    http_method=HTTPMethod.GET,
    api_method="/time-series/{pair}",
    returning=TimeSeriesDto,
    response_data_key=["data"],
):
    """
    Get timeseries for pair
    """

    pair: str
    start_date: str
    end_date: str
    period: str
