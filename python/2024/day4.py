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
    return(True)

def check_adjacent_letter(data,x,y,x_offset,y_offset) -> str:
    if x+x_offset < 0:
        return('error')
    elif x+x_offset >= len(data):
        return('error')
    elif y+y_offset < 0:
        return('error')
    elif y+y_offset >= len(data[0]):
        return('error')
    else:
        return(data[y+y_offset][x+x_offset])

def part1(data: list) -> int:
    answers = 0
    directions = get_cardinal_directions()
    positions = itertools.product(range(len(data)),range(len(data[0])))

    for position, direction in itertools.product(positions, directions):
        if check_for_xmas(data, position, direction):
            answers += 1

    return(answers)

def part2(data: list) -> int:
    answers = 0
    for y, line in enumerate(data):
        for x, letter in enumerate(line):
            nw_letter = check_adjacent_letter(data,x,y,x_offset=-1,y_offset=-1)
            ne_letter = check_adjacent_letter(data,x,y,x_offset=1,y_offset=-1)
            sw_letter = check_adjacent_letter(data,x,y,x_offset=-1,y_offset=1)
            se_letter = check_adjacent_letter(data,x,y,x_offset=1,y_offset=1)
            if (letter == 'A') & (((ne_letter == 'M') & (sw_letter == 'S')) | ((ne_letter == 'S') & (sw_letter == 'M'))) & (((nw_letter == 'M') & (se_letter == 'S')) | ((nw_letter == 'S') & (se_letter == 'M'))):
                answers+=1
    return(answers)

def main():
    file = os.path.abspath("./data/2024/day4.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))

if __name__ == "__main__":
    main()