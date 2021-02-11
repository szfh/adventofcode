import itertools

def make_tidy_data(data_raw):
    data_split = data_raw.split("\n")
    data_tidy = [int(n) for n in data_split]
    return(data_tidy)

def part1(data_tidy, preamble=25):
    i = preamble
    while i < len(data_tidy):
        combinations = itertools.combinations(data_tidy[i-preamble:i], 2)
        n = data_tidy[i]
        valid = False
        for a, b in combinations:
            print(a, b)
            if n == (a+b):
                valid = True
                i += 1
                break
        if valid == False:
            return(n)

def main():
    file = "H:\\Projects\\adventofcode\\data\\day9.txt"

    with open(file,'r') as f:
        data_raw = f.read()
        data_tidy = make_tidy_data(data_raw)

        print('part 1 solution: %d' %part1(data_tidy))
        # print('part 2 solution: %d' %part2(data_tidy))

if __name__ == "__main__":
    main()