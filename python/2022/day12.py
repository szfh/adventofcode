import os
import sys
import copy
import string

# import numpy as np

sys.path.append(os.path.abspath("../scripts"))


def make_tidy_data(data_raw):
    data_tidy = data_raw.splitlines()
    # breakpoint()
    return data_tidy


def find_point(data, letter) -> tuple:
    for p, line in enumerate(data):
        try:
            point = (line.index(letter), p)
            break
        except:
            continue
    return point


def update_surrounding_points(data: list, path: list, x: int, y: int, current_step: int):
    len_x = len(data[0])
    len_y = len(data)
    if (x > 0):
        if (alphabet[data[y][x - 1]] <= alphabet[data[y][x]] + 1):
            path[y][x - 1] = min(path[y][x - 1], current_step + 1)
    if (x < len_x - 1):
        if (alphabet[data[y][x + 1]] <= alphabet[data[y][x]] + 1):
            path[y][x + 1] = min(path[y][x + 1], current_step + 1)
    if (y > 0):
        if (alphabet[data[y - 1][x]] <= alphabet[data[y][x]] + 1):
            path[y - 1][x] = min(path[y - 1][x], current_step + 1)
    if (y < len_y - 1):
        if (alphabet[data[y + 1][x]] <= alphabet[data[y][x]] + 1):
            path[y + 1][x] = min(path[y + 1][x], current_step + 1)


def part1(data):
    path = [[1000 for char in range(len(data[0]))] for line in range(len(data))]
    global start, end, alphabet
    start, end = find_point(data, letter='S'), find_point(data, letter='E')
    alphabet = {letter: number for number, letter in enumerate(string.ascii_lowercase)}
    alphabet.update({'S': 0, 'E': 26})
    current_step = 0
    path[start[1]][start[0]] = 0
    while path[end[1]][end[0]] == 1000:
        for y, line in enumerate(path):
            for x, point in enumerate(line):
                if point == current_step:
                    update_surrounding_points(data, path, x, y, current_step)
        current_step += 1
    return path[end[1]][end[0]]


def part2(data):
    path = [[1000 for char in range(len(data[0]))] for line in range(len(data))]
    global start, end, alphabet
    start, end = find_point(data, letter='S'), find_point(data, letter='E')
    alphabet = {letter: number for number, letter in enumerate(string.ascii_lowercase)}
    alphabet.update({'S': 0, 'E': 26})
    current_step = 0
    for y, line in enumerate(path):
        for x, point in enumerate(line):
            if alphabet[data[y][x]] == 0:
                path[y][x] = 0
    while path[end[1]][end[0]] == 1000:
        for y, line in enumerate(path):
            for x, point in enumerate(line):
                if point == current_step:
                    update_surrounding_points(data, path, x, y, current_step)
        current_step += 1
    return path[end[1]][end[0]]


def main():
    file = os.path.abspath("../../data/2022/day12.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
