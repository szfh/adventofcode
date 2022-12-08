import os
import sys
import itertools

sys.path.append(os.path.abspath("../scripts"))


def make_tidy_data(data_raw):
    data_tidy = data_raw.splitlines()
    data_int = [[int(x) for x in line] for line in data_tidy]
    return data_int


def check_clear_line(line: list, height: int):
    for tree in line:
        if tree >= height:
            return False
    return True


def check_clear_path(data: list, x_tree: int, y_tree: int) -> bool:
    height = data[y_tree][x_tree]
    x_max = len(data)
    y_max = len(data[0])
    for direction in ['up', 'down', 'left', 'right']:
        match direction:
            case 'up':
                line = []
                [line.append(data[y][x_tree]) for y in range(0, y_tree)]
                if check_clear_line(line, height):
                    return True
            case 'down':
                line = []
                [line.append(data[y][x_tree]) for y in range(y_tree + 1, y_max)]
                if check_clear_line(line, height):
                    return True
            case 'left':
                line = []
                [line.append(data[y_tree][x]) for x in range(0, x_tree)]
                if check_clear_line(line, height):
                    return True
            case 'right':
                line = []
                [line.append(data[y_tree][x]) for x in range(x_tree + 1, x_max)]
                if check_clear_line(line, height):
                    return True
    return False


def part1(data):
    visible_trees = 0
    for x, y in itertools.product(range(len(data)), range(len(data[0]))):
        if check_clear_path(data, x, y):
            visible_trees += 1
    return visible_trees


def part2(data):
    return 2


def main():
    file = os.path.abspath("../../data/2022/day8.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
