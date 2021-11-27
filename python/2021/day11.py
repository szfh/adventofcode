def make_tidy_data(data_raw):
    data_split = data_raw.splitlines()
    return data_split

def count_occupied_adjacent(data,j,i):
    steps = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    occupied_adj = 0
    for a, b in steps:
        if (0 <= (j + a) < len(data)) & (0 <= (i + b) < len(data[j])):
            if data[j+a][i+b] == "#":
                occupied_adj += 1
    return occupied_adj

def count_occupied_line(data,j,i):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    occupied_line = 0
    for a, b in directions:
        a2, b2 = a, b
        while (0 <= (j + a2) < len(data)) & (0 <= (i + b2) < len(data[j])):
            if data[j+a2][i+b2] == "#":
                occupied_line += 1
                break
            elif data[j+a2][i+b2] == "L":
                break
            elif data[j+a2][i+b2] == ".":
                a2 += a
                b2 += b
    return occupied_line

def run_rule1(data):
    data_new = []
    for j, row in enumerate(data):
        data_new.append("")
        for i, seat in enumerate(data[j]):
            if seat == ".":
                data_new[j] += "."
            elif seat == "L":
                if count_occupied_adjacent(data, j, i) == 0:
                    data_new[j] += "#"
                else:
                    data_new[j] += "L"
            elif seat == "#":
                if count_occupied_adjacent(data, j, i) >= 4:
                    data_new[j] += "L"
                else:
                    data_new[j] += "#"
    return data_new

def run_rule2(data):
    data_new = []
    for j, row in enumerate(data):
        data_new.append("")
        for i, seat in enumerate(data[j]):
            if seat == ".":
                data_new[j] += "."
            elif seat == "L":
                if count_occupied_line(data, j, i) == 0:
                    data_new[j] += "#"
                else:
                    data_new[j] += "L"
            elif seat == "#":
                if count_occupied_line(data, j, i) >= 5:
                    data_new[j] += "L"
                else:
                    data_new[j] += "#"
    return data_new

def count_occupied(data):
    count = 0
    for row in data:
        count += row.count("#")
    return count

def part1(data):
    while True:
        data_new = run_rule1(data)
        if data == data_new:
            return(count_occupied(data))
        else:
            data = data_new

def part2(data):
    while True:
        data_new = run_rule2(data)
        if data == data_new:
            return(count_occupied(data))
        else:
            data = data_new

def main():
    file = "H:\\Projects\\adventofcode\\data\\2021\\day11.txt"

    with open(file,'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' %part1(data))
    print('part 2 solution: %d' %part2(data))

if __name__ == "__main__":
    main()