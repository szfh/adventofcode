# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 10:55:56 2020

@author: samue
"""

file = "H:\\Projects\\adventofcode\\data\\day2.txt"

with open(file,'r') as f:
    data = f.read().splitlines()

def make_tidy_lines(line):
    line_tidy = line
    line_tidy = line_tidy.replace(':','')
    line_tidy = line_tidy.replace('-',' ')
    line_tidy = line_tidy.split(' ')
    return(line_tidy)

data_tidy = [make_tidy_lines(line) for line in data]

def check_password1(line): 
    min_use = int(line[0])
    max_use = int(line[1])
    letter = line[2]
    pw = line[3]
        
    count = pw.count(letter)
    
    if(count >= min_use and count <= max_use):
        return(True)
    else:
        return(False)
    
valid_passwords1 = list(filter(check_password1, data_tidy))
n_valid1 = len(valid_passwords1)
print('part 1 solution: %d' %(n_valid1))

def check_password2(line): 
    l1 = int(line[0])-1
    l2 = int(line[1])-1
    letter = line[2]
    pw = line[3]
        
    if(pw[l1] == letter and pw[l2] != letter):
        return(True)
    elif(pw[l1] != letter and pw[l2] == letter):
        return(True)
    else:
        return(False)

valid_passwords2 = list(filter(check_password2, data_tidy))
n_valid2 = len(valid_passwords2)
print('part 2 solution: %d' %(n_valid2))
