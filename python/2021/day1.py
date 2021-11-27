# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 09:52:44 2020

@author: samue
"""

import numpy as np
from itertools import combinations

file = "H:\\Projects\\adventofcode\\data\\2021\\day1.txt"

with open(file,'r') as f:
    data = f.read().splitlines()

data = [int(string) for string in data]

def sums_to_2020(data):
    return sum(data) == 2020

pairs = combinations(data,2)

pairs_sum = list(filter(sums_to_2020, pairs))
pairs_product = np.prod(pairs_sum)
print('part 1 solution: %d' %(pairs_product))

triples = combinations(data,3)

triples_sum = list(filter(sums_to_2020, triples))
triples_product = np.prod(triples_sum)
print('part 2 solution: %d' %(triples_product))
