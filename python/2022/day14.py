import os
import sys
import itertools

sys.path.append(os.path.abspath("../scripts"))


def make_tidy_data(data_raw):
    data_tidy = data_raw.splitlines()
    data_split = [d.split(' -> ') for d in data_tidy]
    data_int = [[(int(c.split(',')[0]), int(c.split(',')[1])) for c in l] for l in data_split]
    return data_int


def make_structure(data, add_floor=False):
    structure_points = set()
    if add_floor:
        temp_max_depth = 0
        for l in data:
            for c1, c2 in l:
                if c2 > temp_max_depth:
                    temp_max_depth = c2
        data.append([(0, temp_max_depth + 2), (1000, temp_max_depth + 2)])
    for l in data:
        for c1, c2 in itertools.pairwise(l):
            x_points = range(min(c1[0], c2[0]), max(c1[0], c2[0]) + 1)  # not right if reversed direction
            y_points = range(min(c1[1], c2[1]), max(c1[1], c2[1]) + 1)
            [structure_points.add((x, y)) for x, y in itertools.product(x_points, y_points)]
    max_depth = 0
    for p in structure_points:
        if p[1] > max_depth:
            max_depth = p[1]
    return (structure_points, max_depth)


def draw_structure(structure_points, sand_points, max_depth):
    structure = []
    for y in range(0, max_depth + 1):
        structure.append([])
        for x in range(0, 1001):
            if (x, y) == (500, 0):
                structure[y].append('S')
            if (x, y) in (structure_points):
                structure[y].append('#')
            elif (x, y) in (sand_points):
                structure[y].append('o')
            else:
                structure[y].append('.')
    [print(''.join(row)) for row in structure]
    return structure


def drop_sand(structure_points, sand_points, count):
    current_position = (500, 0)
    points = structure_points.union(sand_points)
    while True:
        if current_position[1] == len(structure_points):
            return (sand_points, count, True, False)
        elif (current_position[0], current_position[1] + 1) not in points:
            current_position = (current_position[0], current_position[1] + 1)
        elif (current_position[0] - 1, current_position[1] + 1) not in points:
            current_position = (current_position[0] - 1, current_position[1] + 1)
        elif (current_position[0] + 1, current_position[1] + 1) not in points:
            current_position = (current_position[0] + 1, current_position[1] + 1)
        else:
            sand_points.add(current_position)
            count += 1
            if current_position == (500, 0):
                return (sand_points, count, False, True)
            else:
                return (sand_points, count, False, False)


def part1(data):
    (structure_points, max_depth) = make_structure(data)
    sand_points = set()
    count = 0
    overflow = False
    while overflow == False:
        (sand_points, count, overflow, _) = drop_sand(structure_points, sand_points, count)
    structure = draw_structure(structure_points, sand_points, max_depth)
    return count


def part2(data):
    (structure_points, max_depth) = make_structure(data, True)
    sand_points = set()
    count = 0
    blocked = False
    while blocked == False:
        (sand_points, count, _, blocked) = drop_sand(structure_points, sand_points, count)
    structure = draw_structure(structure_points, sand_points, max_depth)
    return count


def main():
    file = os.path.abspath("../../data/2022/day14.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
