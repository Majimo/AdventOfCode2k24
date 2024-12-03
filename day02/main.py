import timeit

def determine_if_safe(array: list[int]) -> bool:
     for i, number in enumerate(array):
        if i < len(array) - 1:
            if array == sorted(array) or array == sorted(array, reverse=True):
                if abs(array[i] - array[i + 1]) < 4 and abs(array[i] - array[i + 1]) > 0:
                    continue
                else:
                    return False
            else:
                return False
        return True
     else:
          return False

def determine_if_really_safe(array: list[int], possible_error_count) -> bool:
    for i, number in enumerate(array):
        if i < len(array) - 1:
            if array == sorted(array) or array == sorted(array, reverse=True):
                if abs(array[i] - array[i + 1]) < 4 and abs(array[i] - array[i + 1]) > 0:
                    continue
                else:
                    possible_error_count += 1
                    del array[i + 1]
                    if determine_if_really_safe(array, possible_error_count) and possible_error_count < 2:
                        continue
                    else:
                        return False
            else:
                # return False
                possible_error_count += 1
                del array[i + 1]
                if determine_if_really_safe(array, possible_error_count) and possible_error_count < 2:
                    continue
                else:
                    return False
        return True
    else:
        return False

def split_lines(lines: list[str], part: int) -> list[int]:
        global_array = []
        for i, line in enumerate(lines):
            array = [int(x) for x in line.split(" ")]
            global_array.append(array)
        return global_array

def determine_safe_lines(array: list[int]):
    safe_lines = []
    for i, line in enumerate(array):
        if determine_if_safe(line):
            safe_lines.append(line)
    return safe_lines

def determine_really_safe_lines(array: list[int]):
    safe_lines = []
    for i, line in enumerate(array):
        possible_error_count = 0
        if determine_if_really_safe(line, possible_error_count):
            safe_lines.append(line)
    return safe_lines

with open("input.txt") as f:    
    start = timeit.default_timer()
    left_array = []
    right_array = []
    lines = [line.strip() for line in f.readlines()]
    print(f"Result PART 1 : {len(determine_safe_lines(split_lines(lines, 1)))}")
    stop_1 = timeit.default_timer()
    execution_time = stop_1 - start
    print(f"Execution time PART 1: {execution_time * 1000} ms")

with open("input.txt") as f:
    start_b = timeit.default_timer()
    left_array = []
    right_array = []
    lines = [line.strip() for line in f.readlines()]
    print(f"Result PART 2 : {len(determine_really_safe_lines(split_lines(lines, 2)))}")
    stop_2 = timeit.default_timer()
    execution_time_b = stop_2 - start_b
    print(f"Execution time PART 2: {execution_time_b * 1000} ms")