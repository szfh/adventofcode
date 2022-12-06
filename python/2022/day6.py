import os
import sys
import itertools

sys.path.append(os.path.abspath("../scripts"))


def make_tidy_data(data_raw):
    return data_raw


def create_zip(data, n: int):
    data_list = []
    [data_list.append(data[i:]) for i in range(n)]
    zipped_list = zip(*data_list)
    return zipped_list


def unique_values(line: tuple) -> bool:
    for c in itertools.combinations((line), 2):
        if c[0] == c[1]:
            return False
    return True


def part1(data):
    n = 4
    data_zip = create_zip(data, n)
    for k, line in enumerate(data_zip):
        if unique_values(line):
            return n + k


def part2(data):
    n = 14
    data_zip = create_zip(data, n)
    for k, line in enumerate(data_zip):
        if unique_values(line):
            return n + k


def main():
    file = os.path.abspath("../../data/2022/day6.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
