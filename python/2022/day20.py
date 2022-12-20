import os
import sys

sys.path.append(os.path.abspath("../scripts"))


def make_tidy_data(data_raw):
    data1 = data_raw.splitlines()
    data2 = [int(x) for x in data1]
    data_dict = list()
    for i, x in enumerate(data2):
        data_dict.append({
            'start_position': i,
            'value': x
        })
    return data_dict


def part1(data):
    for start_position, _ in enumerate(data):
        for current_position, item in enumerate(data):
            if item['start_position'] == start_position:
                new_position = (current_position + item['value']) % (len(data) - 1)
                if new_position == 0:
                    new_position = len(data) - 1
                data.insert(new_position, data.pop(current_position))
                break

    for i, item in enumerate(data):
        if item['value'] == 0:
            zero_index = i
            break

    values = [item['value'] for item in data]
    return values[(1000 + zero_index) % len(data)] + values[(2000 + zero_index) % len(data)] + values[
        (3000 + zero_index) % len(data)]


def part2(data):
    return 2


def main():
    file = os.path.abspath("../../data/2022/day20.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
