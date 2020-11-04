import pandas as pd

from algo_trading.data_flow import data_flow


def test_data_flow_init():
    test_data_flow = data_flow.DataFlow()
    assert list(test_data_flow.candles_df.columns) == list(
        pd.DataFrame(columns=["open", "close", "high", "low", "volume"]).columns
    )
