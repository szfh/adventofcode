import os
import sys
import itertools

sys.path.append(os.path.abspath("../scripts"))


def make_tidy_data(data_raw):
    return data_raw


def unique_values(line: tuple) -> bool:
    for c in itertools.combinations((line), 2):
        if c[0] == c[1]:
            return False
    return True


def part1(data):
    data_zip = zip(data[0:], data[1:], data[2:], data[3:])
    for n, line in enumerate(data_zip):
        if unique_values(line):
            return n + 4


def part2(data):
    return 2


def main():
    file = os.path.abspath("../../data/2022/day6.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
