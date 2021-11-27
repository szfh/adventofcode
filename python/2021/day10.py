from collections import Counter

def make_tidy_data(data_raw):
    data_split = data_raw.split("\n")
    data = [int(n) for n in data_split]
    data.append(0)
    data.append(max(data)+3)
    return(data)

def part1(data):
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

def part2(data):
    data_sorted = sorted(data)
    c = Counter()
    c[0] = 1
    for j in data_sorted[1:]:
        c[j] = c[j-1] + c[j-2] + c[j-3]
    return(c[data_sorted[-1]])

def main():
    file = "H:\\Projects\\adventofcode\\data\\2021\\day10.txt"

    with open(file,'r') as f:
        data_raw = f.read()
        data = make_tidy_data(data_raw)

        print('part 1 solution: %d' %part1(data))
        print('part 2 solution: %d' %part2(data))

if __name__ == "__main__":
    main()