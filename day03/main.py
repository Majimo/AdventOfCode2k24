import timeit
import re

def return_all_mul(line: str) -> list[str]:
    return re.findall(r"mul\((\d+),(\d+)\)", line)

def return_mul_with_do_and_dont(line: str) -> list[str]:
    return re.findall(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", line)

def recover_only_do_mul(array: list[str]) -> list[str]:
    computed_array = []

    mul_enabled = True
    for match in array:
        if match == "do()":
            mul_enabled = True
        elif match == "don't()":
            mul_enabled = False
        elif match.startswith("mul("):
            if mul_enabled:
                computed_array.append(match)
                
    for i, match in enumerate(computed_array):
        computed_array[i] = re.findall(r"mul\((\d+),(\d+)\)", match)[0]

    return computed_array

def transform_all_mul_to_int(array: list[str]) -> list[int]:
    return [(int(x), int(y)) for x, y in array]

def add_all_mul(array: list[int]) -> int:
    result = 0
    for x, y in array:
        result += mul(x, y)
    return result

def mul(x: int, y: int) -> int:
    return x * y

def return_result(line: str) -> int:
    return add_all_mul(transform_all_mul_to_int(return_all_mul(line)))

def return_result_with_do_and_dont(line: str) -> int:
    return add_all_mul(transform_all_mul_to_int(recover_only_do_mul(return_mul_with_do_and_dont(line))))

with open("input.txt") as f:    
    start = timeit.default_timer()
    lines = [line.strip() for line in f.readlines()]
    line = " ".join(lines)
    print(f"Result PART 1 : {return_result(line)}")
    stop_1 = timeit.default_timer()
    execution_time = stop_1 - start
    print(f"Execution time PART 1: {execution_time * 1000} ms")

with open("input.txt") as f:
    start_b = timeit.default_timer()
    lines = [line.strip() for line in f.readlines()]
    line = " ".join(lines)
    print(f"Result PART 1 : {return_result_with_do_and_dont(line)}")
    stop_2 = timeit.default_timer()
    execution_time_b = stop_2 - start_b
    print(f"Execution time PART 2: {execution_time_b * 1000} ms")