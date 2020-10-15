import pandas as pd


class DataFlow:
    def __init__(self):
        self.candles_df = pd.DataFrame(
            columns=["open", "close", "high", "low", "volume"])
