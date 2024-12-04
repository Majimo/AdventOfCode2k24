from main import find_xmas, find_horizontal_occurences, find_vertical_occurences, find_diagonal_occurrences
import pytest
import re


class TestMain:
    @pytest.fixture
    def dumb_lines(self):
        return ["..X...X", ".SAMXM.", ".A..A..", "XMAS.S.", ".X....."]
    @pytest.fixture
    def lines(self):
        return ["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM", "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX"]
    @pytest.fixture
    def rows(self, lines):
        return len(lines)
    @pytest.fixture
    def cols(self, lines):
        return len(lines[0])

    def test_dumb_find_xmas(self, dumb_lines):
        assert find_xmas(dumb_lines) == 5

    def test_find_xmas(self, lines):
        assert find_xmas(lines) == 18
    
    def test_dumb_find_horizontal_occurences(self, dumb_lines):
        assert find_horizontal_occurences(dumb_lines) == 2

    def test_find_horizontal_occurences(self, lines):
        assert find_horizontal_occurences(lines) == 5
    
    def test_dumb_find_vertical_occurences(self, dumb_lines):
        assert find_vertical_occurences(dumb_lines, 5, 7, "XMAS") == 1

    def test_find_vertical_occurences(self, lines, rows, cols):
        assert find_vertical_occurences(lines, rows, cols, "XMAS") == 3
    
    def test_dumb_find_diagonal_occurrences(self, dumb_lines):
        assert find_diagonal_occurrences(dumb_lines, 5, 7, "XMAS") == 2
    
    def test_find_diagonal_occurrences(self, lines, rows, cols):
        assert find_diagonal_occurrences(lines, rows, cols, "XMAS") == 10