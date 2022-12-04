import sys
import os

sys.path.append(os.path.abspath("../scripts"))
from aoc_functions import *


def make_tidy_data(data_raw):
    data_tidy = data_raw.splitlines()
    return data_tidy


def count_values(data):
    length = len(data[0])
    breakpoint()
    for position in range(length):
        zeros, ones = 0, 0
        for j in data:
            breakpoint()


def get_gamma_epsilon(data):
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
    # breakpoint()
    return (gamma, epsilon)


def get_oxygen_co2(data):
    data_oxygen = data
    for i in range(len(data_oxygen[0])):
        zeros, ones = 0, 0
        for j in range(len(data_oxygen)):
            match data_oxygen[j][i]:
                case '0':
                    zeros += 1
                case '1':
                    ones += 1
        if zeros > ones:
            data_oxygen = list(filter(lambda x: x[i] == '0', data_oxygen))
        else:
            data_oxygen = list(filter(lambda x: x[i] == '1', data_oxygen))
        if len(data_oxygen) == 1:
            oxygen = []
            [oxygen.append(x) for x in data_oxygen[0]]
            break

    data_co2 = data
    for i in range(len(data_co2[0])):
        zeros, ones = 0, 0
        for j in range(len(data_co2)):
            match data_co2[j][i]:
                case '0':
                    zeros += 1
                case '1':
                    ones += 1
        if zeros > ones:
            data_co2 = list(filter(lambda x: x[i] == '1', data_co2))
        else:
            data_co2 = list(filter(lambda x: x[i] == '0', data_co2))
        if len(data_co2) == 1:
            co2 = []
            [co2.append(x) for x in data_co2[0]]
            break

    return (oxygen, co2)


def bin2dec(bin):
    bin.reverse()
    sum, mult = 0, 1
    for bit in bin:
        sum += (int(bit) * mult)
        mult *= 2
    return sum


def part1(data):
    gamma, epsilon = get_gamma_epsilon(data)
    power = bin2dec(gamma) * bin2dec(epsilon)
    return power


def part2(data):
    oxygen, co2 = get_oxygen_co2(data)
    power = bin2dec(oxygen) * bin2dec(co2)
    return power


def main():
    file = os.path.abspath("../../data/2021/day3.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
