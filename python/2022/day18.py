import os
import sys

sys.path.append(os.path.abspath("../scripts"))


def make_tidy_data(data_raw):
    data1 = data_raw.splitlines()
    data2 = [(int(d.split(',')[0]), int(d.split(',')[1]), int(d.split(',')[2])) for d in data1]
    return data2


def check_faces(cube: tuple, data: list) -> int:
    clear_faces = 0
    directions = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    for dir in directions:
        if (cube[0] + dir[0], cube[1] + dir[1], cube[2] + dir[2]) not in data:
            clear_faces += 1
    return clear_faces


def part1(data):
    total_clear_faces = sum([check_faces(cube, data) for cube in data])
    return total_clear_faces


def part2(data):
    return 2


def main():
    file = os.path.abspath("../../data/2022/day18.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
