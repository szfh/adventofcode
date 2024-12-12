import os

def make_tidy_data(data_raw):
    data_split = [line.split('   ') for line in data_raw.split('\n')]
    data_int = [[int(x) for x in line] for line in data_split]
    return data_int

def part1(data: list) -> int:
    list0 = []
    list1 = []

    for line in data:
        list0.append(line[0])
        list1.append(line[1])

    list0.sort()
    list1.sort()

    differences = []

    for a, b in zip(list0, list1):
        differences.append(abs(a-b))
    
    total = sum(differences)
    return(total)

def part2(data: list) -> int:
    list0 = []
    list1 = []

    for line in data:
        list0.append(line[0])
        list1.append(line[1])
    
    score = 0
    for a in range(len(list0)):
        for b in range(len(list1)):
            if list0[a] == list1[b]:
                score+=list0[a]
    return(score)

def main():
    file = os.path.abspath("./data/2024/day1.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))

if __name__ == "__main__":
    main()