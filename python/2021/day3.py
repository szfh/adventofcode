import sys
import os

sys.path.append(os.path.abspath("../scripts"))
from aoc_functions import *


def make_tidy_data(data_raw):
    data_tidy = data_raw.splitlines()
    return (data_tidy)


def count_values(data):
    length = len(data[0])
    breakpoint()
    for position in range(length):
        zeros, ones = 0, 0
        for j in data:
            breakpoint()


def find_rates(data):
    length = len(data[0])
    gamma, epsilon = [], []
    for position in range(length):
        zeros, ones = 0, 0
        for word in data:
            match word[position]:
                case '0':
                    zeros += 1
                case '1':
                    ones += 1
        if zeros > ones:
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')
    return (gamma, epsilon)


def bin2dec(bin):
    bin.reverse()
    sum, mult = 0, 1
    for bit in bin:
        sum += (int(bit) * mult)
        mult *= 2
    return (sum)


def part1(data):
    gamma, epsilon = find_rates(data)
    power = bin2dec(gamma) * bin2dec(epsilon)
    return (power)


def part2(data):
    return (2)


def main():
    file = os.path.abspath("../../data/2021/day3.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
