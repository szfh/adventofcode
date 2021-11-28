from copy import deepcopy

def make_tidy_data(data_raw):
    data_split = data_raw.split("\n")
    data_tidy = [line.split(" ") for line in data_split]
    return(data_tidy)

def run_instructions(data_tidy):
    i = 0
    accumulator = 0
    terminated = False
    visited = [False for _ in data_tidy]
    while True:

        if i == (len(data_tidy)):
            terminated = True
            return (accumulator, terminated)
        elif visited[i]:
            return(accumulator, terminated)
        else:
            visited[i] = True

        operation = data_tidy[i][0]
        argument = int(data_tidy[i][1])

        if operation == "acc":
            accumulator = accumulator + argument
            i += 1
        elif operation == "jmp":
            i = i + argument
        elif operation == "nop":
            i += 1

def part1(data_tidy):
    accumulator, _ = (run_instructions(data_tidy))
    return(accumulator)

def part2(data_tidy):
    while True:
        for i, instruction in enumerate(data_tidy):
            data_changed = deepcopy(data_tidy)
            operation = data_tidy[i][0]
            argument = int(data_tidy[i][1])
            if operation == "jmp":
                data_changed[i][0] = "nop"
            elif operation == "nop":
                data_changed[i][0] = "jmp"

            accumulator, terminated = (run_instructions(data_changed))

            if terminated:
                return(accumulator)

def main():
    file = "H:\\Projects\\adventofcode\\data\\2020\\day8.txt"

    with open(file,'r') as f:
        data_raw = f.read()
        data_tidy = make_tidy_data(data_raw)

        print('part 1 solution: %d' %part1(data_tidy))
        print('part 2 solution: %d' %part2(data_tidy))

if __name__ == "__main__":
    main()