import numbers

import pandas as pd
import pytest

from algo_trading.algorithm import Algorithm


@pytest.fixture
def create_algorithm_class():
    class TestingAlgorithm(Algorithm):
        def setup(self):
            pass

        def algorithm(self):
            pass

    testing_algorithm = TestingAlgorithm()
    return testing_algorithm


def test_algorithm_instantiation():
    with pytest.raises(TypeError):
        Algorithm()


attributes = [("buying_power", numbers.Real), ("buys", pd.Series), ("sells", pd.Series)]


@pytest.mark.parametrize("attribute, expected_type", attributes)
def test_algorithm_attribute_types(attribute, expected_type, create_algorithm_class):
    assert isinstance(getattr(create_algorithm_class, attribute), expected_type)
