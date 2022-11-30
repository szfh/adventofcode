import sys
import os
sys.path.append(os.path.abspath("../scripts"))
from aoc_functions import *

def make_tidy_data(data_raw):
    data_tidy = data_raw.splitlines()
    data_numeric = [int(n) for n in data_tidy]
    return(data_numeric)

def part1(data):
    count = sum(y>x for x,y in zip(data, data[1:]))
    return(count)

def part2(data):
    d1 = zip(data,data[1:],data[2:])
    d2 = zip(data[1:], data[2:], data[3:])
    count = sum(sum(y)>sum(x) for x, y in zip(d1,d2))
    return(count)

def main():
    file = os.path.abspath("../../data/2021/day1.txt")

    with open(file,'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' %part1(data))
    print('part 2 solution: %d' %part2(data))

if __name__ == "__main__":
    main()