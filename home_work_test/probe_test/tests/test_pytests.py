import pytest
from main import multiplication_int, multiplication_string

params = [
    (1, 1, 1),
    (2, 2, 4),
    (-5, 1, -5),
    (-10, 1 - 10)
]


class TestFunctions:
    @pytest.mark.parametrize('a, b, result', params)
    def test_multiplication_int_param(self, a, b, result):
        assert multiplication_int(a, b) == result
