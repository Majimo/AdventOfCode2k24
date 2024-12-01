from main import toto, order_left_array, order_right_array
import pytest

class TestMain:
    @pytest.fixture
    def lines(self):
        return ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]
    @pytest.fixture
    def left_array(self):
        return []
    @pytest.fixture
    def right_array(self):
        return []

    def test_toto(self, lines):
        assert toto(lines, 1) == 11

    def test_order_arrays(self, left_array, right_array):
        left_array = [3, 4, 2, 1, 3, 3]
        right_array = [4, 3, 5, 3, 9, 3]

        assert order_left_array(left_array) == [1, 2, 3, 3, 3, 4]
        assert order_right_array(right_array) == [3, 3, 3, 4, 5, 9]