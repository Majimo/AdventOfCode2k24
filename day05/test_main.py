from main import determine_safe_lines, get_middle_number_in_safe_lines, reorder_wrong_lines
import pytest
import re


class TestMain:
    @pytest.fixture
    def rules(self):
        return ["47|53", "97|13", "97|61", "97|47", "75|29", "61|13", "75|53", "29|13", "97|29", "53|29", "61|53", "97|53", "61|29", "47|13", "75|47", "97|75", "47|61", "75|61", "47|29", "75|13", "53|13"]
    @pytest.fixture
    def orders(self):
        return [["75","47","61","53","29"], ["97","61","53","29","13"], ["75","29","13"], ["75","97","47","61","53"], ["61","13","29"], ["97","13","75","29","47"]]
    @pytest.fixture
    def safe_lines(self):
        return [["75","47","61","53","29"], ["97","61","53","29","13"], ["75","29","13"]]
    @pytest.fixture
    def wrong_lines(self):
        return [["75","97","47","61","53"], ["61","13","29"], ["97","13","75","29","47"]]
    @pytest.fixture
    def wrong_lines_reordered(self):
        return [["97","75","47","61","53"], ["61","29","13"], ["97","75","47","29","13"]]

    def test_determine_safe_lines(self, rules, orders, safe_lines, wrong_lines):
        assert determine_safe_lines(orders, rules) == (safe_lines, wrong_lines)

    def test_get_middle_number_in_safe_lines(self, safe_lines):
        assert get_middle_number_in_safe_lines(safe_lines) == 143

    def test_reorder_wrong_lines(self, wrong_lines, wrong_lines_reordered):
        assert reorder_wrong_lines(wrong_lines) == wrong_lines_reordered

    def test_get_middle_number_in_safe_lines(self, wrong_lines_reordered):
        assert get_middle_number_in_safe_lines(wrong_lines_reordered) == 124