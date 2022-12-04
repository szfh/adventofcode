import os
import sys
import re

sys.path.append(os.path.abspath("../scripts"))
from aoc_functions import *


def make_tidy_data(data_raw):
    data_tidy = data_raw.splitlines()
    data_sep = [re.split(',|-', x) for x in data_tidy]
    data_int = []
    for line in data_sep:
        line_int = [int(x) for x in line]
        line_sep = tuple(line_int[0:2]), tuple(line_int[2:4])
        data_int.append(line_sep)
    return data_int


def fully_contains(line0, line1) -> bool:
    if (line1[0] >= line0[0]) & (line1[1] <= line0[1]):
        return True
    else:
        return False


def partially_contains(line0, line1) -> bool:
    if (line1[1] < line0[0]) | (line1[0] > line0[1]):
        return False
    else:
        return True


def part1(data):
    count = 0
    for line in data:
        if fully_contains(line[0], line[1]) | fully_contains(line[1], line[0]):
            count += 1
    return count


def part2(data):
    count = 0
    for line in data:
        if partially_contains(line[0], line[1]) | fully_contains(line[1], line[0]):
            count += 1
    return count


def main():
    file = os.path.abspath("../../data/2022/day4.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
