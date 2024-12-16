import os
import re
import math
import itertools

def make_tidy_data(data_raw: str) -> list:
    data_split = data_raw.split('\n\n')
    order_rules_str = [re.findall('[0-9]+', line) for line in data_split[0].splitlines()]
    order_rules = [[int(x) for x in line] for line in order_rules_str]
    
    updates_str = [re.findall('[0-9]+', line) for line in data_split[1].splitlines()]
    updates = [[int(x) for x in line] for line in updates_str]

    return(order_rules, updates)

def check_update(update, order_rules) -> bool:
    for n, page in enumerate(update):
        page_check = check_page(page, update[n+1:], order_rules)
        if page_check == False:
            return(False)
    return(True)

def check_page(page, update, order_rules) -> bool:
    for next_page in update:
        for o1, o2 in order_rules:
            if (page == o2) & (next_page == o1):
                return(False)
    return(True)

def calculate_score(updates, valid) -> int:
    score = 0
    for x, mask in enumerate(valid):
        if mask == True:
            score += updates[x][(len(updates[x])//2)]
    return(score)

def part1(order_rules: list, updates: list) -> int:
    valid = []
    for n, update in enumerate(updates):
        valid.append(check_update(update, order_rules))
    score = calculate_score(updates, valid)
    return(score)

def main():
    file = os.path.abspath("./data/2024/day5.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    order_rules, updates = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(order_rules, updates))

if __name__ == "__main__":
    main()