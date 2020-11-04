import pandas as pd
from polygon_cache.cache import CachedRESTClient

from algo_trading.settings import POLYGON_KEY

client = CachedRESTClient(POLYGON_KEY)


def get_ticker_info(ticker: str, multiplier: int, timespan: str, from_: str, to: str) -> pd.DataFrame:
    """
    :param ticker: The ticker of the stock data you are trying to retrieve. i.e. AMD
    :param multiplier: Time multiplier for the timespan.
    :param timespan: Valid timespans are minute, hour, day, year.
    :param from_: Date in YYYY-MM-DD format.
    :param to: Date in YYYY-MM-DD format.
    :return: a pandas dataframe of requested values
    """
    json_data = client.stocks_equities_aggregates(
        ticker, multiplier, timespan, from_, to
    )

    return transform_json_data_to_df(json_data.results)


def transform_json_data_to_df(json_data: dict):
    df = pd.DataFrame(json_data)
    df["date"] = pd.to_datetime(df["t"], unit="ms", utc=True)
    df = df.set_index("date")
    df = df[["v", "o", "c", "h", "l"]]
    df = df.rename(
        columns={"v": "volume", "o": "open", "c": "close", "h": "high", "l": "low"}
    )
    return df
