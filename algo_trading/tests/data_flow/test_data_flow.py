from algo_trading.data_flow import data_flow
import pandas as pd


def test_data_flow_init():
    test_data_flow = data_flow.DataFlow()
    assert list(test_data_flow.candles_df.columns) == list(
        pd.DataFrame(columns=["open", "close", "high", "low", "volume"]).columns)
