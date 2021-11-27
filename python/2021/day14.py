import sys
import os

def make_tidy_data(data_raw):
    data_split = data_raw.splitlines()
    data_tidy = [(line.split(" = ")[0], (line.split(" = ")[1])) for line in data_split]
    return(data_tidy)

def dec2bin(n,l):
    nb = bin(n)[2:]
    nbz = nb.zfill(l)
    return(nbz)

def bin2dec(l):
    sum = 0
    power = len(l)-1
    for element in l:
        sum += int(element)*(2**power)
        power -= 1
    return(sum)

def update_value(value, mask):
    value_bin = dec2bin(value,len(mask))
    output = []
    for i in range(len(value_bin)):
        if mask[i]!="X":
            output.append(mask[i])
        else:
            output.append(value_bin[i])
    output_dec = bin2dec(output)
    return(output_dec)

def part1(data):
    memory = {}
    mask = "X"*35
    for k, a in data:
        if k == "mask":
            mask = a
        else:
            location = int(k.replace("mem[","").replace("]",""))
            value = int(a)
            output_value = update_value(value, mask)
            memory.update({location: output_value})
    total = sum(memory.values())
    return(total)

def part2(data):
    return(2)

def main():
    file = os.path.abspath("../../data/2021/day14.txt")

    with open(file,'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' %part1(data))
    print('part 2 solution: %d' %part2(data))

if __name__ == "__main__":
    main()