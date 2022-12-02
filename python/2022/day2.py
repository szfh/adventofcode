import sys
import os

sys.path.append(os.path.abspath("../scripts"))
from aoc_functions import *


def make_tidy_data(data_raw):
    data_tidy = data_raw.splitlines()
    data_sep = [tuple(x.split(' ')) for x in data_tidy]
    return (data_sep)


def choice_score(game: str) -> int:
    match game:
        case 'X':
            score = 1
        case 'Y':
            score = 2
        case 'Z':
            score = 3
    return score


def play_game1(game: tuple) -> int:
    match game[0]:
        case 'A':
            match game[1]:
                case 'X':
                    score = 3
                case 'Y':
                    score = 6
                case 'Z':
                    score = 0
        case 'B':
            match game[1]:
                case 'X':
                    score = 0
                case 'Y':
                    score = 3
                case 'Z':
                    score = 6
        case 'C':
            match game[1]:
                case 'X':
                    score = 6
                case 'Y':
                    score = 0
                case 'Z':
                    score = 3
    return score


def outcome_score(result: str) -> int:
    match result:
        case 'X':
            score = 0
        case 'Y':
            score = 3
        case 'Z':
            score = 6
    return score


def play_game2(game: tuple) -> str:
    match game[0]:
        case 'A':
            match game[1]:
                case 'X':
                    choice = 'Z'
                case 'Y':
                    choice = 'X'
                case 'Z':
                    choice = 'Y'
        case 'B':
            match game[1]:
                case 'X':
                    choice = 'X'
                case 'Y':
                    choice = 'Y'
                case 'Z':
                    choice = 'Z'
        case 'C':
            match game[1]:
                case 'X':
                    choice = 'Y'
                case 'Y':
                    choice = 'Z'
                case 'Z':
                    choice = 'X'
    return choice


def part1(data):
    score = 0
    for game in data:
        score += play_game1(game)
        score += choice_score(game[1])
    return score


def part2(data):
    score = 0
    for game in data:
        choice = play_game2(game)
        score += outcome_score(game[1])
        score += choice_score(choice)
    return score


def main():
    file = os.path.abspath("../../data/2022/day2.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
