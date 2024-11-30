from main import get_second_line
import pytest

class TestMain:
    @pytest.fixture
    def lines(self):
        return ["first", "second"]
    
    def test_get_second_line(self, lines):
        assert get_second_line(lines, 1) == "second"