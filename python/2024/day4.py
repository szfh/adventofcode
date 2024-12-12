import os
import itertools

def make_tidy_data(data_raw):
    data_split = data_raw.splitlines()
    return data_split

def get_x_positions(data: list) -> list:
    x_positions = []
    for a, b in itertools.product(range(len(data)),range(len(data[0]))):
        if data[a][b] == 'X':
            x_positions.append((a,b))
    return(x_positions)

def get_cardinal_directions() -> list:
    return([(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)])

def check_for_xmas(data: list, position: list, direction: list) -> bool:
    for n, letter in zip(range(4),'XMAS'):
        try:
            if position[0]+n*direction[0] < 0:
                return(False)
            elif position[0]+n*direction[0] > len(data):
                return(False)
            elif position[1]+n*direction[1] < 0:
                return(False)
            elif position[1]+n*direction[1] > len(data[0]):
                return(False)
            if data[position[0]+n*direction[0]][position[1]+n*direction[1]] != letter:
                return(False)
        except:
            return(False)
        if n == 3:
           print('n = ', n, ' | letter = ', letter, ' | position = ', position, ' | direction = ', direction)
    return(True)

def part1(data: list) -> int:
    answers = 0
    directions = get_cardinal_directions()
    positions = itertools.product(range(len(data)),range(len(data[0])))

    for position, direction in itertools.product(positions, directions):
        if check_for_xmas(data, position, direction):
            answers += 1

    return(answers)

def main():
    file = os.path.abspath("./data/2024/day4.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))

if __name__ == "__main__":
    main()