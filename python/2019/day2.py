import os
import itertools

def make_tidy_data(data_raw):
    data_split = data_raw.split(",")
    data_tidy = [int(i) for i in data_split]
    return(data_tidy)

def run_computer(data,new1,new2):
    data_new = data.copy()
    data_new[1] = new1
    data_new[2] = new2
    i = 0
    while True:
        if data_new[i] == 1:
            data_new[data_new[i + 3]] = data_new[data_new[i + 1]] + data_new[data_new[i + 2]]
            i += 4
        elif data_new[i] == 2:
            data_new[data_new[i + 3]] = data_new[data_new[i + 1]] * data_new[data_new[i + 2]]
            i += 4
        elif data_new[i] == 99:
            return(data_new[0])
        else:
            print("shouldn't be here")

def part1(data):
    return(run_computer(data,12,2))

def part2(data):
    for new1, new2 in itertools.product(range(100),range(100)):
        if run_computer(data,new1,new2) == 19690720:
            return((100*new1)+new2)

def main():
    file = os.path.abspath("../../data/2019/day2.txt")

    with open(file,'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' %part1(data))
    print('part 2 solution: %d' %part2(data))

if __name__ == "__main__":
    main()