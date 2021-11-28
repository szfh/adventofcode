import os

def make_tidy_data(data_raw):
    data_tidy = data_raw.splitlines()
    return(data_tidy)

def part1(data):
    fuel = []
    [fuel.append((int(element) // 3) - 2) for element in data]
    return(sum(fuel))

def part2(data):
    fuel = []
    for element in data:
        fuel_needed = int(element)
        while fuel_needed > 0:
            fuel_needed = (fuel_needed // 3) - 2
            fuel.append(fuel_needed)
    return (sum(fuel))

def main():
    file = os.path.abspath("../../data/2019/day1.txt")

    with open(file,'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' %part1(data))
    print('part 2 solution: %d' %part2(data))

if __name__ == "__main__":
    main()