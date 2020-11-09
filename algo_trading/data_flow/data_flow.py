import pandas as pd
from algo_trading.api_adapters import polygon_api
from abc import ABC, abstractmethod


class DataFlow(ABC):
    def __init__(self, previous_points_needed: int):
        self.candles_df = self.get_dataframe()
        self.previous_points_needed = previous_points_needed

    @abstractmethod
    def get_dataframe(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def get_data_generator(self) -> pd.DataFrame:
        pass


class PolygonBackTestDataFlow(DataFlow):
    def __init__(self, ticker: str, multiplier: int, timespan: str, from_: str, to: str, previous_points_needed: int):
        self.ticker = ticker
        self.multiplier = multiplier
        self.timespan = timespan
        self.from_ = from_
        self.to = to
        super().__init__(previous_points_needed)

    def get_dataframe(self) -> pd.DataFrame:
        return polygon_api.get_ticker_info(self.ticker, self.multiplier, self.timespan, self.from_, self.to)

    def get_data_generator(self) -> pd.DataFrame:
        for i in range(self.previous_points_needed, len(self.candles_df) + 1):
            yield self.candles_df[:i]


class PolygonLiveTradingDataFlow(DataFlow):
    def get_dataframe(self, **kwargs):
        pass

    def get_data_generator(self):
        pass
