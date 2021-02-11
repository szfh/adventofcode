def make_tidy_data(data_raw):
    data_split = data_raw.split("\n")
    data_tidy = [line.split(" ") for line in data_split]
    return(data_tidy)

def part1(data_tidy):
    i = 0
    accumulator = 0
    visited = [False for _ in data_tidy]
    while True:
        operation = data_tidy[i][0]
        argument = int(data_tidy[i][1])

        if visited[i]:
            return(accumulator)
        else:
            visited[i] = True

        if operation == "acc":
            accumulator = accumulator + argument
            i += 1
        elif operation == "jmp":
            i = i + argument
        elif operation == "nop":
            i += 1


def main():
    file = "H:\\Projects\\adventofcode\\data\\day8test1.txt"

    with open(file,'r') as f:
        data_raw = f.read()
        data_tidy = make_tidy_data(data_raw)

        print('part 1 solution: %d' %part1(data_tidy))
        # print('part 2 solution: %d' %part2(data_tidy))
        breakpoint()

if __name__ == "__main__":
    main()