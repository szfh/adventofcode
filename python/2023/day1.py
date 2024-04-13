import sys
import os

sys.path.append(os.path.abspath("../scripts"))

def make_tidy_data(data_raw):
    data_split = data_raw.split('\n')
    return data_split

def part1(data: list) -> int:
    values = []
    for line in data:
        for a in line:
            if a.isdigit():
                d1 = a
                break
        for b in reversed(line):
            if b.isdigit():
                d2 = b
                break
        values.append(int(d1+d2))
    return sum(values)

def main():
    file = os.path.abspath("../../data/2023/day1.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    # print('part 2 solution: %d' % part2(data))

if __name__ == "__main__":
    main()
