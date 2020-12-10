# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 21:34:53 2020

@author: samue
"""

import numpy as np

file = "H:\\Projects\\adventofcode\\data\\day6.txt"

with open(file,'r') as f:
    data_raw = f.read()

def make_tidy_data(data):
    data_tidy = data.split('\n\n')
    return(data_tidy)

def make_tidy_lines(line):
    line_tidy = line
    line_tidy = line_tidy.split('\n')
    return(line_tidy)

def get_letters(line):
    # letters = []
    letters = ''.join(line)
    # for word in line:
    #     for l in word:
    #         if l in letters:
    #             letters.append(l)
    return(letters)

data_tidy = make_tidy_data(data_raw)
data_tidy = [make_tidy_lines(line) for line in data_tidy]
letters = [get_letters(line) for line in data_tidy]
letters = [set(line) for line in letters]
length = [len(line) for line in letters]
total_length = sum(length)
print('part 1 solution: %d' %(total_length))

def get_common_letters(line):
    word0 = line[0]
    for letter in word0:
        # for word in line[1:]:
            if letter in line[1:]:
                print(letter)
    #letters in all elements of list
    # return(line)

common_letters = [get_common_letters(line) for line in data_tidy[:1]]

# triples_sum = list(filter(sums_to_2020, triples))

# np.concatenate(data_tidy[0])
# ''.join(data_tidy[0])
# set(data_tidy[1][:])
# def get_id(line):
#     row = \
#         int(line[0])*64 +\
#         int(line[1])*32 +\
#         int(line[2])*16 +\
#         int(line[3])*8 +\
#         int(line[4])*4 +\
#         int(line[5])*2 +\
#         int(line[6])*1
    
#     col = \
#         int(line[7])*4 +\
#         int(line[8])*2 +\
#         int(line[9])*1
    
#     # print(row, col)
    
#     id = row*8 + col
#     return(id)


# ids = [get_id(line) for line in data_tidy]
# min_id = min(ids)
# max_id = max(ids)
# print('part 1 solution: %d' %(max_id))

# for i in range(min_id,max_id):
#     if (i > min_id) and (i < max_id):
#         if not (i in ids):
#             missing_seat = i
#             break

# print('part 2 solution: %d' %(missing_seat))
