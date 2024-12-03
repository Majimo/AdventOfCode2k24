from main import split_lines, determine_safe_lines, determine_really_safe_lines
import pytest

class TestMain:
    @pytest.fixture
    def lines(self):
        return ["7 6 4 2 1", "1 2 7 8 9", "9 7 6 2 1", "1 3 2 4 5", "8 6 4 4 1", "1 3 6 7 9"]

    def test_split(self, lines):
        assert split_lines(lines, 1) == [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]

    def test_dumb_determine_safe_lines(self, lines):
        assert len(determine_safe_lines(split_lines(lines, 1))) == 2
    
    def test_determine_safe_lines(self, lines):
        assert determine_safe_lines(split_lines(lines, 1)) == [[7, 6, 4, 2, 1], [1, 3, 6, 7, 9]]

    def test_dumb_determine_really_safe_lines(self, lines):
        assert len(determine_really_safe_lines(split_lines(lines, 2))) == 4

    def test_determine_really_safe_lines(self, lines):
        assert determine_really_safe_lines(split_lines(lines, 2)) == [[7, 6, 4, 2, 1], [1, 2, 4, 5], [8, 6, 4, 1], [1, 3, 6, 7, 9]]