import os
import re

def make_tidy_data(data_raw):
    return data_raw

def part1(data: str) -> int:
    commands = re.findall("mul\([0-9]+,[0-9]+\)", data)
    total = 0
    for c in commands:
        a = re.findall("[0-9]+", c)
        total += int(a[0])*int(a[1])
    return(total)

def part2(data: str) -> int:
    commands = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)", data)
    do = True
    total = 0
    for c in commands:
        if c == "do()":
            do = True
        elif c == "don't()":
            do = False
        else:
            a = re.findall("[0-9]+", c)
            if do:
                total += int(a[0])*int(a[1])
    return(total)

def main():
    file = os.path.abspath("./data/2024/day3.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))

if __name__ == "__main__":
    main()