import copy
import os
import sys

sys.path.append(os.path.abspath("../scripts"))


def make_tidy_data(data_raw):
    data_tidy = data_raw.splitlines()
    data_split = [x if len(x) <= 1 else [x[0], int(x[1])] for x in [l.split(' ') for l in data_tidy]]
    return data_split


def part1(data):
    c, X, next_cycle = 0, 1, 20
    values = []
    for line in data:
        match line[0]:
            case 'noop':
                c += 1
                if c >= next_cycle:
                    values.append((next_cycle, X))
                    next_cycle += 40
            case 'addx':
                c += 2
                if c >= next_cycle:
                    values.append((next_cycle, X))
                    next_cycle += 40
                X += line[1]

    return sum([a * b for a, b in values])


def part2(data):
    return 2


def main():
    file = os.path.abspath("../../data/2022/day10.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
