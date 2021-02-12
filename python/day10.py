def make_tidy_data(data_raw):
    data_split = data_raw.split("\n")
    data_tidy = [int(n) for n in data_split]
    return(data_tidy)

def part1(data):
    data.append(0)
    data.append(max(data)+3)
    differences = [0, 0, 0]
    data_sorted = sorted(data)
    for i in range(1,len(data_sorted)):
        if data_sorted[i]-data_sorted[i-1] == 1:
            differences[0] += 1
        elif data_sorted[i] - data_sorted[i - 1] == 2:
            differences[1] += 1
        elif data_sorted[i]-data_sorted[i-1] == 3:
            differences[2] += 1
    return(differences[0]*differences[2])

def main():
    file = "H:\\Projects\\adventofcode\\data\\day10.txt"

    with open(file,'r') as f:
        data_raw = f.read()
        data = make_tidy_data(data_raw)

        print('part 1 solution: %d' %part1(data))
        # print('part 2 solution: %d' %part2(data_tidy))

if __name__ == "__main__":
    main()