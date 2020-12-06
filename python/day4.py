# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 16:45:44 2020

@author: samue
"""

import re

file = "H:\\Projects\\adventofcode\\data\\day4.txt"

with open(file,'r') as f:
    data_raw = f.read()

def make_tidy_data(data):
    data_tidy = data.split('\n\n')
    return(data_tidy)

def make_tidy_lines(line):
    line_tidy = line
    line_tidy = line_tidy.replace('\n',' ')
    line_tidy = line_tidy.split(' ')
    return(line_tidy)

def make_dict(line):
    line_dict = {}
    
    for i in range(len(line)):
        line_dict[line[i].split(':')[0]] = line[i].split(':')[1]
    
    return line_dict

def is_valid_passport(line):
    if(len(line)==8):
        return(True)
    elif(len(line)==7 and 'cid' not in line.keys()):
        return(True)
    else:
        return(False)

data_tidy = make_tidy_data(data_raw)
data_tidy = [make_tidy_lines(line) for line in data_tidy]
data_dict = [make_dict(line) for line in data_tidy]
valid = [is_valid_passport(line) for line in data_dict]
print('part 1 solution: %d' %(sum(valid)))

def is_valid_passport2(line):
    if(not is_valid_passport(line)):
        return(False)
    elif(not (1920 <= int(line['byr']) <= 2002)):
        return(False)
    elif(not (2010 <= int(line['iyr']) <= 2020)):
        return(False)
    elif(not (2020 <= int(line['eyr']) <= 2030)):
        return(False)
    elif(not re.search('^(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))$',line['hgt'])):
        return(False)
    elif(not re.search('^#([0-9]|[a-f]){6}$',line['hcl'])):
        return(False)
    elif(not line['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')):
        return(False)
    elif(not re.search('^[0-9]{9}$',line['pid'])):
        return(False)
    else:
        return(True)

valid2 = [is_valid_passport2(line) for line in data_dict]
print('part 2 solution: %d' %(sum(valid2)))
