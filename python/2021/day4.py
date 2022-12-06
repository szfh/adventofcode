import os
import sys

sys.path.append(os.path.abspath("../scripts"))
from aoc_functions import *


def make_tidy_data(data_raw):
    numbers = [int(x) for x in data_raw.split('\n\n')[0].split(',')]
    boards1 = data_raw.split('\n\n')[1:]
    boards2 = [board.split('\n') for board in boards1]
    boards3 = [[(line[0:2], line[3:5], line[6:8], line[9:11], line[12:14]) for line in board] for board in boards2]
    boards4 = [[[int(x) for x in line] for line in board] for board in boards3]
    return (numbers, boards4)


def check_win(board: list, numbers: list) -> bool:
    for row in board:
        if len(set(row) & set(numbers)) == 5:
            return True
    for column_number in range(len(board[0])):
        column = []
        [column.append(board[row][column_number]) for row in range(len(board))]
        if len(set(column) & set(numbers)) == 5:
            return True
    return False


def calculate_score(board: list, numbers: list) -> int:
    last_number = numbers[-1]
    board_numbers = []
    for line in board:
        board_numbers += line
    remaining_numbers = set(board_numbers).difference(set(numbers))
    score = last_number * sum(remaining_numbers)
    return score


def part1(numbers: list, boards: list):
    for k, n in enumerate(numbers):
        for b, board in enumerate(boards):
            if check_win(board, numbers[:k]) == True:
                score = calculate_score(boards[b], numbers[:k])
                return score


def part2(numbers: list, boards: list):
    winning_boards = []
    while True:
        for k, n in enumerate(numbers):
            remaining_boards = set(range(len(boards))).difference(set(winning_boards))
            for x in remaining_boards:
                if check_win(boards[x], numbers[:k]):
                    winning_boards.append(x)
            if len(winning_boards) == (len(boards)):
                score = calculate_score(boards[winning_boards[-1]], numbers[:k])
                return score


def main():
    file = os.path.abspath("../../data/2021/day4.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    (numbers, boards) = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(numbers, boards))
    print('part 2 solution: %d' % part2(numbers, boards))


if __name__ == "__main__":
    main()
