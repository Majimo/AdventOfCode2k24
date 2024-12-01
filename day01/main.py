import timeit

left_array = []
right_array = []

def toto(lines: list[str], part: int) -> int:
    return 11

def add_array_to_left_and_right(array: list[str]):
    left_array.append(array[0])
    right_array.append(array[1])
    order_arrays()

def order_left_array(array: list[str]) -> list[str]:
    return sorted(array)

def order_right_array(array: list[str]) -> list[str]:
    return sorted(array)

def order_arrays():
    left_array.sort()
    right_array.sort()

def determine_global_diff(left_array: list[str], right_array: list[str]) -> int:
    global_diff = 0
    for i, line in enumerate(left_array):
        difference = 0
        if int(left_array[i]) > int(right_array[i]):
            difference = int(left_array[i]) - int(right_array[i])
        else:
            difference = int(right_array[i]) - int(left_array[i])
        global_diff += difference
    return global_diff

def determine_occurence(left_array: list[str], right_array: list[str]) -> int:
    global_occurence = 0
    for i, left_line in enumerate(left_array):
        multiplier = 0
        occurence = 0
        for j, right_line in enumerate(right_array):
            if left_array[i] == right_array[j]:
                occurence += 1
        
        multiplier = occurence * int(left_line)
        global_occurence += multiplier
    return global_occurence

def split_and_add_to_array(lines: list[str], part: int) -> int:
    for i, line in enumerate(lines):
        # Split lines into 2 parts and find the lowest number in first part and the highest number in the second part
        array = line.split("   ")
        add_array_to_left_and_right(array)

    if part == 1:
        return determine_global_diff(left_array, right_array)
    else:
        return determine_occurence(left_array, right_array)
    
with open("input.txt") as f:    
    start = timeit.default_timer()
    left_array = []
    right_array = []
    lines = [line.strip() for line in f.readlines()]
    print(f"Result PART 1 : {split_and_add_to_array(lines, 1)}")
    stop_1 = timeit.default_timer()
    execution_time = stop_1 - start
    print(f"Execution time PART 1: {execution_time * 1000} ms")

with open("input2.txt") as f:
    start_b = timeit.default_timer()
    left_array = []
    right_array = []
    lines = [line.strip() for line in f.readlines()]
    print(f"Result PART 2 : {split_and_add_to_array(lines, 2)}")
    stop_2 = timeit.default_timer()
    execution_time_b = stop_2 - start_b
    print(f"Execution time PART 2: {execution_time_b * 1000} ms")