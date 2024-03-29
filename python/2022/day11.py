import os
import sys
import re

sys.path.append(os.path.abspath("../scripts"))


def make_tidy_data(data_raw):
    monkeys = []
    data_split = data_raw.split('\n\n')
    for m in data_split:
        m_strip = [m.strip() for m in m.split('\n')]
        monkeys.append({
            'number': [int(x) for x in re.findall('[0-9]+', m_strip[0])],
            'items': [int(x) for x in re.findall('[0-9]+', m_strip[1])],
            'operation': m_strip[2].split(':')[1].strip(),
            'test': m_strip[3].split(':')[1].strip(),
            'true': m_strip[4].split(':')[1].strip(),
            'false': m_strip[5].split(':')[1].strip(),
            'count': 0
        })
    return monkeys


def perform_operation(value, operation, mode, lcm):
    if operation == 'new = old * old':
        new_value = value * value
    else:
        operator = operation.split(' ')[3]
        operand = int(operation.split(' ')[4])
        match operator:
            case '+':
                new_value = value + operand
            case '*':
                new_value = value * operand
    if mode == 'div_three':
        return new_value // 3
    elif mode == 'mod':
        return new_value % lcm
    else:
        return new_value


def test_divisible(value, test):
    divisor = int(test.split(' ')[-1])
    if value % divisor == 0:
        return True
    else:
        return False


def throw_item(throw):
    monkey = int(throw.split(' ')[-1])
    return monkey


def get_multiplier(monkeys):
    multiplier = 1
    for m in monkeys:
        multiplier *= int(m['test'].split(' ')[-1])
    return multiplier


def part1(monkeys):
    for turn in range(20):
        for m in monkeys:
            while len(m['items']) > 0:
                m['items'][0] = perform_operation(m['items'][0], m['operation'], 'div_three', 0)
                if test_divisible(m['items'][0], m['test']):
                    new_monkey = throw_item(m['true'])
                    item = m['items'].pop(0)
                    monkeys[new_monkey]['items'].append(item)
                else:
                    new_monkey = throw_item(m['false'])
                    item = m['items'].pop(0)
                    monkeys[new_monkey]['items'].append(item)
                m['count'] += 1
    counts = [m['count'] for m in monkeys]
    counts.sort(reverse=True)
    return counts[0] * counts[1]


def part2(monkeys):
    lcm = get_multiplier(monkeys)
    for turn in range(10000):
        for m in monkeys:
            while len(m['items']) > 0:
                m['items'][0] = perform_operation(m['items'][0], m['operation'], 'mod', lcm)
                if test_divisible(m['items'][0], m['test']):
                    new_monkey = throw_item(m['true'])
                    item = m['items'].pop(0)
                    monkeys[new_monkey]['items'].append(item)
                else:
                    new_monkey = throw_item(m['false'])
                    item = m['items'].pop(0)
                    monkeys[new_monkey]['items'].append(item)
                m['count'] += 1
    counts = [m['count'] for m in monkeys]
    counts.sort(reverse=True)
    return counts[0] * counts[1]


def main():
    file = os.path.abspath("../../data/2022/day11.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    monkeys = make_tidy_data(data_raw)
    print('part 1 solution: %d' % part1(monkeys))
    monkeys = make_tidy_data(data_raw)
    print('part 2 solution: %d' % part2(monkeys))


if __name__ == "__main__":
    main()
