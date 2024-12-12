import os
import itertools

def make_tidy_data(data_raw):
    data_split = [line.split(' ') for line in data_raw.split('\n')]
    data_int = [[int(x) for x in line] for line in data_split]
    return data_int

def all_increasing(line: list) -> bool:
    for a,b in itertools.pairwise(line):
        if a <= b:
            return(False)
    return(True)

def all_decreasing(line: list) -> bool:
    for a,b in itertools.pairwise(line):
        if a >= b:
            return(False)
    return(True)

def differ_by_at_least_one_and_at_most_three(line: list) -> bool:
    for a,b in itertools.pairwise(line):
        if abs(a-b) < 1:
            return(False)
        if abs(a-b) > 3:
            return(False)
    return(True)

def part1(data: list) -> int:
    safe_reports = 0
    for line in data:
        if (all_increasing(line) | all_decreasing(line)) & differ_by_at_least_one_and_at_most_three(line):
            safe_reports += 1
    return(safe_reports)

def main():
    file = os.path.abspath("./data/2024/day2.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    #print('part 2 solution: %d' % part2(data))

if __name__ == "__main__":
    main()