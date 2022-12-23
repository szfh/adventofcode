import os
import sys
import itertools
import ast

sys.path.append(os.path.abspath("../scripts"))


def make_tidy_data(data_raw):
    data1 = data_raw.split('\n\n')
    data2 = [(ast.literal_eval(s.split('\n')[0]), ast.literal_eval(s.split('\n')[1])) for s in data1]
    return data2


def compare_values(x1, x2):
    if (x1 is None) & (x2 is not None):
        return True
    elif (x1 is not None) & (x2 is None):
        return False
    elif (x1 == []) & (x2 == []):
        return None
    elif isinstance(x1, int) & isinstance(x2, int):
        if x1 < x2:
            return True
        elif x1 > x2:
            return False
        else:
            return None
    elif isinstance(x1, int) & isinstance(x2, list):
        for y1, y2 in itertools.zip_longest([x1], x2):
            outcome = compare_values(y1, y2)
            if outcome is not None:
                return outcome
    elif isinstance(x1, list) & isinstance(x2, int):
        for y1, y2 in itertools.zip_longest(x1, [x2]):
            outcome = compare_values(y1, y2)
            if outcome is not None:
                return outcome
    else:
        for y1, y2 in itertools.zip_longest(x1, x2):
            outcome = compare_values(y1, y2)
            if outcome is not None:
                return outcome


def part1(data):
    correct_pairs = set()
    for i, d in enumerate(data, start=1):
        for x1, x2 in itertools.zip_longest(d[0], d[1]):
            outcome = compare_values(x1, x2)
            if outcome is True:
                correct_pairs.add(i)
                break
            if outcome is False:
                break
    return sum(correct_pairs)


def part2(data):
    return 2


def main():
    file = os.path.abspath("../../data/2022/day13.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
