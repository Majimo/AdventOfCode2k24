import timeit
import re

def find_horizontal_occurences(lines) -> bool:
    occurence = 0
    for row in lines:
        if len(re.findall(r"XMAS", row)) > 0:
            occurence += 1
        if len(re.findall(r"SAMX", row)) > 0:
            occurence += 1
    return occurence

def make_col_to_string(lines, rows, cols) -> list[str]:
    col_to_string = []
    for col in range(cols):
        col_to_string.append("".join([lines[row][col] for row in range(rows)]))
    return col_to_string

def make_diagonal_to_string(lines, rows, cols) -> list[str]:
    diagonal_to_string = []
    for row in range(rows):
        for col in range(cols):
            try:
                diagonal_to_string.append("".join([lines[row + i][col + i] for i in range(4)]))
            except IndexError:
                pass
    # Partir de la dernière ligne et remonter
    for row in range(rows - 1, 0, -1):
        for col in range(cols):
            try:
                diagonal_to_string.append("".join([lines[row - i][col + i] for i in range(4)]))
            except IndexError:
                pass
    return diagonal_to_string

def find_vertical_occurences(lines, rows, cols, word):
    return find_horizontal_occurences(make_col_to_string(lines, rows, cols))

def find_diagonal_occurrences(lines, rows, cols, word):
    return find_horizontal_occurences(make_diagonal_to_string(lines, rows, cols))

def find_xmas(lines):
    count = 0
    rows, cols = len(lines), len(lines[0])

    word = "XMAS"
    
    count += find_horizontal_occurences(lines)
    
    count += find_vertical_occurences(lines, rows, cols, word)
    
    count += find_diagonal_occurrences(lines, rows, cols, word)

    return count

with open("input.txt") as f:    
    start = timeit.default_timer()
    lines = [line.strip() for line in f.readlines()]
    print(f"Result PART 1 : {find_xmas(lines)}")
    stop_1 = timeit.default_timer()
    execution_time = stop_1 - start
    print(f"Execution time PART 1: {execution_time * 1000} ms")

# with open("input.txt") as f:
#     start_b = timeit.default_timer()
#     lines = [line.strip() for line in f.readlines()]
#     line = " ".join(lines)
#     print(f"Result PART 1 : {return_result_with_do_and_dont(line)}")
#     stop_2 = timeit.default_timer()
#     execution_time_b = stop_2 - start_b
#     print(f"Execution time PART 2: {execution_time_b * 1000} ms")