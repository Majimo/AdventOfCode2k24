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

def find_vertical_occurences(lines, rows, cols, word):
    vertical_count = 0
    for col in range(cols):
        for row in range(rows - 3):
            if all(lines[row + i][col] == word[i] for i in range(4)):
                vertical_count += 1
        for row in range(3, rows):
            if all(lines[row - i][col] == word[i] for i in range(4)):
                vertical_count += 1
    return vertical_count

def find_diagonal_occurrences(lines, rows, cols, word):
    diagonal_count = 0
    for row in range(rows - 3):
        for col in range(cols - 3):
            found_word = lines[row][col] + lines[row + 1][col + 1] + lines[row + 2][col + 2] + lines[row + 3][col + 3]
            if found_word == word:
                diagonal_count += 1
            if found_word == "SAMX":
                diagonal_count += 1
    
    for row in range(rows - 3):
        for col in range(3, cols):
            found_word = lines[row][col] + lines[row - 1][col - 1] + lines[row - 2][col - 2] + lines[row - 3][col - 3]
            if found_word == word:
                diagonal_count += 1
            if found_word == "SAMX":
                diagonal_count += 1

    # Faire colonne max en revenant sur les rows
    for row in range(rows - 3, rows):
        for col in range(3, cols - 3):
            found_word = lines[row][col] + lines[row - 1][col + 1] + lines[row - 2][col + 2] + lines[row - 3][col + 3]
            if found_word == word:
                diagonal_count += 1
            if found_word == "SAMX":
                diagonal_count += 1

    return diagonal_count

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