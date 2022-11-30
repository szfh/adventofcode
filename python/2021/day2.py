import sys
import os
sys.path.append(os.path.abspath("../scripts"))
from aoc_functions import *

def make_tidy_data(data_raw):
    data_split = data_raw.splitlines()
    data_tidy = [line.split(' ') for line in data_split]
    data_tidy = [(x[0], int(x[1])) for x in data_tidy]
    return(data_tidy)

def part1(data):
    h,d = 0,0
    for dir, n in data:
        match dir:
            case 'forward':
                h+=n
            case 'up':
                d-=n
            case 'down':
                d+=n
    return(h*d)

def part2(data):
    h,d,aim = 0,0,0
    for dir, n in data:
        match dir:
            case 'forward':
                h+=n
                d+=n*aim
            case 'up':
                aim-=n
            case 'down':
                aim+=n
    return(h*d)

def main():
    file = os.path.abspath("../../data/2021/day2.txt")

    with open(file,'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)
    print('part 1 solution: %d' %part1(data))
    print('part 2 solution: %d' %part2(data))

if __name__ == "__main__":
    main()