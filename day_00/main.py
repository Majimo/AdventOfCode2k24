def get_second_line(lines, i):
    if (i == 1):
        return lines[i]
    

def read_lines(part: str):
    lines = [line.strip() for line in f.readlines()]
    for i, line in enumerate(lines):
        get_second_line(lines, i)
        print(part)
        print(i, line)

with open("input.txt") as f:
    read_lines('PART 1 :')

with open("input2.txt") as f:
    read_lines('PART 2 :')