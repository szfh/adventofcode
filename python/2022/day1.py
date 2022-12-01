import sys
import os

sys.path.append(os.path.abspath("../scripts"))
from aoc_functions import *


def make_tidy_data(data_raw):
    data_groups = data_raw.split('\n\n')
    data_groups_split = [x.split('\n') for x in data_groups]
    data_int = []
    for l in data_groups_split:
        data_int.append([int(n) for n in l])
    return data_int


def top_elf(data: list, n: int) -> list:
    sums = [sum(l) for l in data]
    sorted_sums = sorted(sums, reverse=True)
    total = sum(sorted_sums[0:n])
    return total


def part1(data: list) -> int:
    total = top_elf(data, n=1)
    return total


def part2(data: list) -> int:
    total = top_elf(data, n=3)
    return total


def main():
    file = os.path.abspath("../../data/2022/day1.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
