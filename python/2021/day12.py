import os

def make_tidy_data(data_raw):
    data_split = data_raw.splitlines()
    data_split = [(line[:1], int(line[1:])) for line in data_split]
    return data_split

def move1(x, y, action, value, direction):
    if action == "N":
        y = y + value
    elif action == "E":
        x = x + value
    elif action == "S":
        y = y - value
    elif action == "W":
        x = x - value
    elif action == "L":
        direction = int((direction - (value/90)) % 4)
    elif action == "R":
        direction = int((direction + (value/90)) % 4)
    elif (action == "F") & (compass[direction] == "N"):
        y = y + value
    elif (action == "F") & (compass[direction] == "E"):
        x = x + value
    elif (action == "F") & (compass[direction] == "S"):
        y = y - value
    elif (action == "F") & (compass[direction] == "W"):
        x = x - value
    return(x, y, direction)

def move2(x, y, waypoint_x, waypoint_y, action, value):
    if action == "N":
        waypoint_y = waypoint_y + value
    elif action == "E":
        waypoint_x = waypoint_x + value
    elif action == "S":
        waypoint_y = waypoint_y - value
    elif action == "W":
        waypoint_x = waypoint_x - value
    elif action == "L":
        for r in range(int(value/90)):
            waypoint_x, waypoint_y = -waypoint_y, waypoint_x
    elif action == "R":
        for r in range(int(value/90)):
            waypoint_x, waypoint_y = waypoint_y, -waypoint_x
    elif action == "F":
        x += (waypoint_x * value)
        y += (waypoint_y * value)
    return (x, y, waypoint_x, waypoint_y)

def find_manhattan_distance(x, y):
    return(abs(x) + abs(y))

def part1(data):
    global compass
    compass = ["N", "E", "S", "W"]
    x, y, direction = 0, 0, 1
    for action, value in data:
        x, y, direction = move1(x, y, action, value, direction)
    return(find_manhattan_distance(x, y))

def part2(data):
    x, y, waypoint_x, waypoint_y = 0, 0, 10, 1
    for action, value in data:
        x, y, waypoint_x, waypoint_y = move2(x, y, waypoint_x, waypoint_y, action, value)
    return(find_manhattan_distance(x, y))

def main():
    file = os.path.abspath("../data/day12.txt")

    with open(file,'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' %part1(data))
    print('part 2 solution: %d' %part2(data))

if __name__ == "__main__":
    main()