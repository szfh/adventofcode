import os
import sys
import string

sys.path.append(os.path.abspath("../scripts"))
from aoc_functions import *


def make_tidy_data(data_raw):
    data_tidy = data_raw.splitlines()
    data_split = [(x[:(len(x) // 2)], x[(len(x) // 2):]) for x in data_tidy]
    assert len(data_split[0]) == len(data_split[1])
    return data_split

def score_letter(letter: str) -> int:
    letters = string.ascii_letters
    score = letters.index(letter)+1
    return score

def part1(data):
    score = 0
    for x in data:
        (letter, ) = set(x[0]).intersection(x[1])
        score += score_letter(letter)
    return score


def part2(data):
    return 2


def main():
    file = os.path.abspath("../../data/2022/day3.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
