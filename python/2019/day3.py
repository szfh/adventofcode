import sys
import os
sys.path.append(os.path.abspath("../scripts"))
from aoc_functions import *
import re

def make_tidy_data(data_raw):
    data_splitlines = data_raw.splitlines()
    path1 = [(dir, int(dist)) for (dir, dist) in re.findall(r'([UDLR])(\d+)', data_splitlines[0])]
    path2 = [(dir, int(dist)) for (dir, dist) in re.findall(r'([UDLR])(\d+)', data_splitlines[1])]
    return(path1, path2)

def move(x, y, dir, dist):
    path = []
    for n in range(dist):
        if dir == "R":
            x+=1
        elif dir == "L":
            x-=1
        elif dir == "U":
            y+=1
        elif dir == "D":
            y-=1
        path.append((x,y))
    return(x, y, path)

def get_path(path):
    x,y = 0,0
    whole_path = []
    for (dir, dist) in path:
        x, y, path = move(x, y, dir, dist)
        whole_path += path
    return(whole_path)

def shortest_intersection(path1, path2):
    intersections =  set(path1) & set(path2)
    manhattan_distances = [abs(x)+abs(y) for (x, y) in intersections]
    return(min(manhattan_distances))

def shortest_path(path1, path2):
    intersections = set(path1) & set(path2)
    index = [(path1.index(intersection), path2.index(intersection)) for intersection in intersections]
    path_lengths = [abs(x)+1 + abs(y)+1 for (x, y) in index]
    return (min(path_lengths))


def part1(data):
    path1 = get_path(data[0])
    path2 = get_path(data[1])
    distance = shortest_intersection(path1, path2)
    return(distance)

def part2(data):
    path1 = get_path(data[0])
    path2 = get_path(data[1])
    distance = shortest_path(path1, path2)
    return(distance)

def main():
    file = os.path.abspath("../../data/2019/day3.txt")

    with open(file,'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)
    print('part 1 solution: %d' %part1(data))
    print('part 2 solution: %d' %part2(data))

if __name__ == "__main__":
    main()
