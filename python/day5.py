# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 10:09:34 2020

@author: samue
"""

file = "H:\\Projects\\adventofcode\\data\\day5.txt"

with open(file,'r') as f:
    data_raw = f.read()

def make_tidy_data(data):
    data_tidy = data.split('\n')
    return(data_tidy)

def make_tidy_lines(line):
    line_tidy = line
    line_tidy = line_tidy.replace('F','0')
    line_tidy = line_tidy.replace('B','1')
    line_tidy = line_tidy.replace('L','0')
    line_tidy = line_tidy.replace('R','1')
    # line_tidy = line_tidy.replace('\n',' ')
    # line_tidy = line_tidy.split(' ')
    return(line_tidy)

def get_id(line):
    row = \
        int(line[0])*64 +\
        int(line[1])*32 +\
        int(line[2])*16 +\
        int(line[3])*8 +\
        int(line[4])*4 +\
        int(line[5])*2 +\
        int(line[6])*1
    
    col = \
        int(line[7])*4 +\
        int(line[8])*2 +\
        int(line[9])*1
    
    # print(row, col)
    
    id = row*8 + col
    return(id)

data_tidy = make_tidy_data(data_raw)
data_tidy = [make_tidy_lines(line) for line in data_tidy]
ids = [get_id(line) for line in data_tidy]
min_id = min(ids)
max_id = max(ids)
print('part 1 solution: %d' %(max_id))

for i in range(min_id,max_id):
    if (i > min_id) and (i < max_id):
        if not (i in ids):
            missing_seat = i
            break

print('part 2 solution: %d' %(missing_seat))
