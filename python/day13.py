import os

def make_tidy_data(data_raw):
    data_split = data_raw.splitlines()
    n = int(data_split[0])
    data = data_split[1].split(",")
    return (n, data)

def get_last_departure(n, id):
    schedule = []
    mult = 1
    while id * (mult-1) <= n:
        schedule.append(id * mult)
        mult += 1
    return(schedule[-1])

def part1(n, data):
    data = [id for id in data if id != "x"]
    last_departure = {}
    for id in data:
        last_departure[id] = get_last_departure(n, int(id))
    time, bus = min(last_departure.values()), min(last_departure, key=last_departure.get)
    return((time-n)*int(bus))

def main():
    file = os.path.abspath("../data/day13.txt")

    with open(file,'r') as f:
        data_raw = f.read()

    (n, data) = make_tidy_data(data_raw)

    print('part 1 solution: %d' %part1(n, data))
    # print('part 2 solution: %d' %part2(n, data))

if __name__ == "__main__":
    main()