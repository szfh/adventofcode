import os
import sys

sys.path.append(os.path.abspath("../scripts"))


def make_tidy_data(data_raw):
    data_tidy = data_raw.split('\n')
    data_split = [line.split(' ') for line in data_tidy]
    data_split = [(line[0], int(line[1])) for line in data_split]
    return data_split


def move_head(pos: tuple, dir: str) -> tuple:
    dir_map = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    new_position = tuple(a + b for a, b in zip(pos, dir_map[dir]))
    return new_position


def move_tail(head_pos: tuple, tail_pos: tuple) -> tuple:
    if (abs(head_pos[0] - tail_pos[0]) <= 1) & (abs(head_pos[1] - tail_pos[1]) <= 1):
        return tail_pos
    x = head_pos[0] - tail_pos[0]
    y = head_pos[1] - tail_pos[1]
    if x >= 1 and y >= 1:
        new_x = tail_pos[0] + 1
        new_y = tail_pos[1] + 1
    elif x >= 1 and y <= -1:
        new_x = tail_pos[0] + 1
        new_y = tail_pos[1] - 1
    elif x <= -1 and y >= 1:
        new_x = tail_pos[0] - 1
        new_y = tail_pos[1] + 1
    elif x <= -1 and y <= -1:
        new_x = tail_pos[0] - 1
        new_y = tail_pos[1] - 1
    elif x >= 1 and y == 0:
        new_x = tail_pos[0] + 1
        new_y = tail_pos[1]
    elif x <= -1 and y == 0:
        new_x = tail_pos[0] - 1
        new_y = tail_pos[1]
    elif x == 0 and y >= 1:
        new_x = tail_pos[0]
        new_y = tail_pos[1] + 1
    elif x == 0 and y <= -1:
        new_x = tail_pos[0]
        new_y = tail_pos[1] - 1

    return (new_x, new_y)


def part1(data):
    head_position, tail_position = (0, 0), (0, 0)
    all_tail_positions = set()
    for line in data:
        for n in range(line[1]):
            head_position = move_head(head_position, line[0])
            tail_position = move_tail(head_position, tail_position)
            all_tail_positions.add(tail_position)
    return len(all_tail_positions)


def part2(data):
    return 2


def main():
    file = os.path.abspath("../../data/2022/day9.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
