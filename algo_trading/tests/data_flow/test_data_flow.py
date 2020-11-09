import pandas as pd
import pytest
from random import randint, seed, uniform
from algo_trading.data_flow import data_flow


def get_fake_df(*args):
    df = pd.DataFrame(columns=["volume", "open", "close", "high", "low"])
    seed(35)
    length = 20
    df["volume"] = [randint(1000, 100000) for _ in range(length)]
    df["open"] = [uniform(10, 20) for _ in range(length)]
    df["close"] = [uniform(10, 20) for _ in range(length)]
    df["high"] = [uniform(10, 20) for _ in range(length)]
    df["low"] = [uniform(10, 20) for _ in range(length)]
    return df


@pytest.fixture
def patch_get_dataframe(monkeypatch):
    monkeypatch.setattr(data_flow.PolygonBackTestDataFlow, "get_dataframe", get_fake_df)


def test_polygon_backtest_get_next(patch_get_dataframe):
    instance = data_flow.PolygonBackTestDataFlow("TICKER", 1, "minute", "2020-1-1", "2020-2-1", 6)
    df = instance.get_dataframe()
    generator = instance.get_data_generator()
    pd.testing.assert_frame_equal(next(generator), df[:6])
    pd.testing.assert_frame_equal(next(generator), df[:7])
    pd.testing.assert_frame_equal(list(generator)[-1], df)

