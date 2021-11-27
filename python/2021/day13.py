import sys
import os

def make_tidy_data(data_raw):
    data_split = data_raw.splitlines()
    n = int(data_split[0])
    data_split = data_split[1].split(",")
    data = []
    for x in data_split:
        if x == "x":
            data.append(-1)
        else:
            data.append(int(x))
    return (n, data)

def get_last_departure(n, id):
    schedule = []
    mult = 1
    while id * (mult-1) <= n:
        schedule.append(id * mult)
        mult += 1
    return(schedule[-1])

def modular_multiplicative_inverse(a: int, b: int) -> int:
    return pow(a, -1, b)

def chinese_remainder_theorem(data):
    product = 1
    for bus, _ in data:
        product *= bus

    total = 0
    for bus, index in data:
        partial_product = product // bus
        inverse = modular_multiplicative_inverse(partial_product, bus)
        total += index * partial_product * inverse
    departure = total % product
    return(departure)

def part1(n, data):
    data = [id for id in data if id != -1]
    last_departure = {}
    for id in data:
        last_departure[id] = get_last_departure(n, int(id))
    time, bus = min(last_departure.values()), min(last_departure, key=last_departure.get)
    return((time-n)*int(bus))

def part2(data):
    bus_and_index = [(bus, bus-index) for index, bus in enumerate(data) if not bus < 0]
    departure = chinese_remainder_theorem(bus_and_index)
    return(departure)

def main():
    file = os.path.abspath("../../data/2021/day13.txt")
    print(sys.version)

    with open(file,'r') as f:
        data_raw = f.read()

    (n, data) = make_tidy_data(data_raw)

    print('part 1 solution: %d' %part1(n, data))
    print('part 2 solution: %d' %part2(data))

if __name__ == "__main__":
    main()