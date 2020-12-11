# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 21:34:53 2020

@author: samue
"""

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
    letters = ''.join(line)
    return(letters)

data_tidy = make_tidy_data(data_raw)
data_tidy = [make_tidy_lines(line) for line in data_tidy]
letters = [get_letters(line) for line in data_tidy]
letters = [set(line) for line in letters]
length = [len(line) for line in letters]
total_length = sum(length)
print('part 1 solution: %d' %(total_length))

def get_line_as_set(line):
    line_set = line
    for i in range(len(line)):
        line_set[i] = set(line[i])
    return(line_set)

def get_common_letters(line):
    common_letters = line[0]
    for i in range(1,len(line)):
        common_letters = common_letters.intersection(line[i])
    return(common_letters)

data_set = [get_line_as_set(line) for line in data_tidy]
common_letters = [get_common_letters(line) for line in data_set]
common_letters_sum = sum([len(line) for line in common_letters])
print('part 2 solution: %d' %(common_letters_sum))
