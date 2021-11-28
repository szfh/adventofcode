import os

def make_tidy_data(data_raw):
    data_tidy = data_raw.splitlines()
    return(data_tidy)

def part1(data):
    fuel = []
    [fuel.append((int(element) // 3) - 2) for element in data]
    sum(fuel)
    return(sum(fuel))

def part2(data):
    return(2)

def main():
    file = os.path.abspath("../../data/2020/day1.txt")

    with open(file,'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' %part1(data))
    print('part 2 solution: %d' %part2(data))

if __name__ == "__main__":
    main()