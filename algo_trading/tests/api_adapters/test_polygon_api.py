import pandas as pd

from algo_trading.api_adapters import polygon_api


def test_transform_json_data_to_df():
    json_data = [
        {
            "v": 1305,
            "vw": 53.8393,
            "o": 53.89,
            "c": 53.62,
            "h": 53.89,
            "l": 53.62,
            "t": 1590998400000,
            "n": 14,
        },
        {
            "v": 174,
            "vw": 53.6328,
            "o": 53.62,
            "c": 53.62,
            "h": 53.62,
            "l": 53.62,
            "t": 1590998460000,
            "n": 2,
        },
    ]
    transformed_data = polygon_api.transform_json_data_to_df(json_data)
    expected_dataframe = pd.DataFrame(
        {
            "volume": {
                pd.Timestamp("2020-06-01 08:00:00+0000", tz="UTC"): 1305,
                pd.Timestamp("2020-06-01 08:01:00+0000", tz="UTC"): 174,
            },
            "open": {
                pd.Timestamp("2020-06-01 08:00:00+0000", tz="UTC"): 53.89,
                pd.Timestamp("2020-06-01 08:01:00+0000", tz="UTC"): 53.62,
            },
            "close": {
                pd.Timestamp("2020-06-01 08:00:00+0000", tz="UTC"): 53.62,
                pd.Timestamp("2020-06-01 08:01:00+0000", tz="UTC"): 53.62,
            },
            "high": {
                pd.Timestamp("2020-06-01 08:00:00+0000", tz="UTC"): 53.89,
                pd.Timestamp("2020-06-01 08:01:00+0000", tz="UTC"): 53.62,
            },
            "low": {
                pd.Timestamp("2020-06-01 08:00:00+0000", tz="UTC"): 53.62,
                pd.Timestamp("2020-06-01 08:01:00+0000", tz="UTC"): 53.62,
            },
        }
    )
    expected_dataframe.index.name = "date"
    pd.testing.assert_frame_equal(transformed_data, expected_dataframe)
