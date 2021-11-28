import os

def make_tidy_data(data_raw):
    data_split = data_raw.split(",")
    data_tidy = [int(i) for i in data_split]
    return(data_tidy)

def part1(data):
    data_new = data.copy()
    data_new[1] = 12
    data_new[2] = 2
    i=0
    while True:
        if data_new[i] == 1:
            data_new[data_new[i+3]] = data_new[data_new[i+1]] + data_new[data_new[i+2]]
            i+=4
        elif data_new[i] == 2:
            data_new[data_new[i + 3]] = data_new[data_new[i+1]] * data_new[data_new[i+2]]
            i += 4
        elif data_new[i] == 99:
            print("99")
            break
        else:
            print("shouldn't be here")
    return(data_new[0])

def part2(data):
    return(2)

def main():
    file = os.path.abspath("../../data/2020/day2.txt")

    with open(file,'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' %part1(data))
    print('part 2 solution: %d' %part2(data))

if __name__ == "__main__":
    main()