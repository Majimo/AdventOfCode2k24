from main import return_result, return_all_mul, transform_all_mul_to_int, add_all_mul, return_mul_with_do_and_dont, recover_only_do_mul, return_result_with_do_and_dont
import pytest
import re


class TestMain:
    @pytest.fixture
    def line(self):
        return "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    @pytest.fixture
    def second_line(self):
        return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    def test_return_result(self, line):
        return_result(line) == 161
    
    def test_return_all_mul(self, line):
        assert return_all_mul(line) == [('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]

    def test_transform_all_mul_to_int(self, line):
        assert transform_all_mul_to_int(return_all_mul(line)) == [(2, 4), (5, 5), (11, 8), (8, 5)]

    def test_add_all_mul(self, line):
        assert add_all_mul(transform_all_mul_to_int(return_all_mul(line))) == 161

    
    def test_return_mul_with_do_and_dont(self, second_line):
        assert return_mul_with_do_and_dont(second_line) == ['mul(2,4)', "don't()", 'mul(5,5)', 'mul(11,8)', 'do()', 'mul(8,5)']

    def test_recover_only_do_mul(self, second_line):
        assert recover_only_do_mul(return_mul_with_do_and_dont(second_line)) == [('2', '4'), ('8', '5')]
    
    def test_return_result_with_do_and_dont(self, second_line):
        assert return_result_with_do_and_dont(second_line) == 48