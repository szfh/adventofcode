# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 12:12:37 2020

@author: samue
"""

# import numpy as np

file = "H:\\Projects\\adventofcode\\data\\2021\\day3.txt"

with open(file,'r') as f:
    data = f.read().splitlines()

def toboggan(data, x, y):
    
    if(data[y][x] == '#'):
        tree = True
    else:
        tree = False
    
    new_x = x + 3
    new_y = y + 1
    
    return(tree, new_x, new_y)


def move(x, y):
    new_x = x
    new_y = y
    return(new_x, new_y)

length = len(data)
width = len(data[0])

x = 0
y = 0
trees = 0

while y < length:
    [tree, x, y] = toboggan(data, x, y)
    if(tree):
        trees += 1
    x = x % width

print('part 1 solution: %d' %(trees))

def toboggan_general(data, x, y, x_add, y_add):
    
    if(data[y][x] == '#'):
        tree = True
    else:
        tree = False
    
    new_x = x + x_add
    new_y = y + y_add
    
    return(tree, new_x, new_y)

def run_toboggan(data, x_add, y_add):
    length = len(data)
    width = len(data[0])
    x = 0
    y = 0
    trees2 = 0

    while y < length:
        [tree, x, y] = toboggan_general(data, x, y, x_add, y_add)
        if(tree):
            trees2 += 1
        x = x % width
    
    return(trees2)

trees2 = 1
for (x_add, y_add) in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    trees2 *= run_toboggan(data, x_add, y_add)

print('part 2 solution: %d' %(trees2))