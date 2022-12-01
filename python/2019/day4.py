import sys
import os
sys.path.append(os.path.abspath("../scripts"))
from aoc_functions import *

def make_tidy_data(data_raw):
    data_split = data_raw.split('-')
    data_int = [int(n) for n in data_split]
    return(data_int)

def check_length(password, n=6):
    if len(password) == n:
        return(True)
    else:
        return(False)

def check_decreasing_digits(password):
    for l1, l2 in zip(password, password[1:]):
        if int(l2) < int(l1):
            return (False)
        else:
            continue
    return(True)

def check_double_digits(password):
    for l1, l2 in zip(password, password[1:]):
        if int(l2) == int(l1):
            return (True)
        else:
            continue
    return(False)

def count_matches(data):
    matches = 0
    for n in range(int(data[0]),int(data[1])):
        n_str = str(n)
        if not check_length(n_str, 6):
            continue
        if not check_decreasing_digits(n_str):
            continue
        if not check_double_digits(n_str):
            continue
        matches+=1
    return(matches)

def part1(data):
    matches = count_matches(data)
    return(matches)

def main():
    file = os.path.abspath("../../data/2019/day4.txt")

    with open(file,'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' %part1(data))
    print('part 2 solution: %d' %part2(data))

if __name__ == "__main__":
    main()