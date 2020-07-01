import pytest
from algo_trading import algorithm


def test_algorithm_instantiation():
    with pytest.raises(TypeError):
        algorithm.Algorithm()
