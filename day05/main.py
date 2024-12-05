import timeit
import re

rules = []
orders = []

def get_middle_number_in_safe_lines(lines: list[str]) -> int:
    middle_numbers = []
    for line in lines:
        middle_numbers.append(int(line[len(line) // 2]))
    return sum(middle_numbers)

def reorder_wrong_lines(wrong_lines: list[str]) -> list[str]:
    return [["97","75","47","61","53"], ["61","29","13"], ["97","75","47","29","13"]]

def determine_safe_lines(orders, rules) -> tuple[list, list]:
    safe_lines = []
    wrong_lines = []
    for order in orders:
        all_cases = []
        for rule in rules:
            left, right = rule.split("|")
            if left in order and right in order:
                all_cases.append(order.index(left) < order.index(right))
                if order.index(left) > order.index(right):
                    print(f"Order {order} is wrong -> {rule}")
        if all(all_cases):
            safe_lines.append(order)
        else:
            wrong_lines.append(order)

    return (safe_lines, wrong_lines)

def recover_rules_and_print_orders(lines: list[str]) -> tuple[list, list]:
    for line in lines:
        if re.match(r"\d+\|\d+", line):
            rules.append(line)
        else:
            if line != "":
                orders.append(line.split(","))

with open("input.txt") as f:    
    start = timeit.default_timer()
    lines = [line.strip() for line in f.readlines()]
    recover_rules_and_print_orders(lines)
    safes = determine_safe_lines(orders, rules)
    print(f"Result PART 1 : {get_middle_number_in_safe_lines(safes[0])}")
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