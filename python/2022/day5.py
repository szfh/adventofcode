import os
import sys
import re

sys.path.append(os.path.abspath("../scripts"))
from aoc_functions import *


def make_tidy_data(data_raw):
    length_line = data_raw.split('\n\n')[0].splitlines()[-1]
    length = int(re.findall('\d+', length_line)[-1])
    boxes = data_raw.split('\n\n')[0].splitlines()[:-1]
    boxes.reverse()
    boxes_list = []
    for n in range(length):
        column = (n * 4) + 1
        stack = []
        for b in boxes:
            if b[column] != ' ':
                stack.append(b[column])
        boxes_list.append(stack)

    moves = data_raw.split('\n\n')[1].splitlines()
    moves_list = [re.findall(r'\d+', move) for move in moves]
    moves_list_int = [[int(x) for x in move] for move in moves_list]
    return (length, boxes_list, moves_list_int)


def move_boxes(boxes: list, move: list) -> list:
    for n in range(move[0]):
        b = boxes[move[1] - 1].pop(-1)
        boxes[move[2] - 1].append(b)
    return boxes


def part1(length: int, boxes: list, moves: list) -> str:
    for move in moves:
        boxes = move_boxes(boxes, move)
    end_state = ''.join([box[-1] for box in boxes])
    return end_state


def part2(data):
    return 2


def main():
    file = os.path.abspath("../../data/2022/day5.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    (length, boxes_list, moves_list) = make_tidy_data(data_raw)

    print('part 1 solution: %s' % part1(length, boxes_list, moves_list))
    # print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
