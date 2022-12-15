import os
import sys
import re

sys.path.append(os.path.abspath("../scripts"))


def make_tidy_data(data_raw):
    data1 = [re.findall('[-+]?[0-9]+', l) for l in data_raw.splitlines()]
    data2 = [[int(i) for i in l] for l in data1]
    data3 = [[(l[0], l[1]), (l[2], l[3])] for l in data2]
    return data3


def check_row(sensor: tuple, beacon: tuple, row: int) -> tuple:
    distance_to_sensor = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
    distance_to_row = abs(row - sensor[1])
    if distance_to_row >= distance_to_sensor:
        return None
    remaining_x_distance = abs(distance_to_sensor - distance_to_row)
    exclude_from_row = (sensor[0] - remaining_x_distance, sensor[0] + remaining_x_distance)
    return exclude_from_row


def count_positions(points_to_exclude: list, row: int) -> set:
    min_x, max_x = 0, 0
    for c in points_to_exclude:
        if c[0] < min_x:
            min_x = c[0]
        if c[1] > max_x:
            max_x = c[1]
    points_to_exclude_set = set()
    for c in points_to_exclude:
        for x in range(c[0], c[1] + 1):
            points_to_exclude_set.add(x)
    return points_to_exclude_set


def add_beacons(points_to_exclude_set: set, data: list, row: int) -> set:
    for _, beacon in data:
        if beacon[1] == row:
            points_to_exclude_set.discard(beacon[0])
    return points_to_exclude_set


def part1(data):
    row = 2000000
    points_to_exclude = []
    for sensor, beacon in data:
        points_to_exclude.append(check_row(sensor, beacon, row))
    points_to_exclude = [p for p in points_to_exclude if p is not None]
    points_to_exclude_set = count_positions(points_to_exclude, row)
    points_to_exclude_set = add_beacons(points_to_exclude_set, data, row)
    return len(points_to_exclude_set)


def part2(data):
    return 2


def main():
    file = os.path.abspath("../../data/2022/day15.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
