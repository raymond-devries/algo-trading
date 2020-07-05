from abc import ABC, abstractmethod

import pandas as pd


class Algorithm(ABC):
    def __init__(self, capital: float = 10000):
        self.buying_power = capital
        self.buys = pd.Series(dtype=int)
        self.sells = pd.Series(dtype=int)

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def algorithm(self):
        pass

    def buy(self):
        pass

    def sell(self):
        pass

