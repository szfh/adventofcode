import os
import sys

sys.path.append(os.path.abspath("../scripts"))


def make_tidy_data(data_raw):
    data1 = data_raw.splitlines()
    return data1


def part1(data):
    return 1


def part2(data):
    return 2


def main():
    file = os.path.abspath("../../data/2022/day1.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
