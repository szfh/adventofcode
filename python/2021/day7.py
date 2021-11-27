def make_tidy_lines(line):
    line_tidy = line
    line_tidy = line_tidy.split(' contain ')
    return(line_tidy)

def make_bag_tuple(c) -> [int, str]:
    number = int(c.split(" ")[0])
    colour = " ".join(c.split(" ")[1:])
    return(number, colour)

def make_bag_dict(data_tidy):
    bag_dict = {}
    for line in data_tidy:
        bag = " ".join(line[0].split(" ")[:2]).replace("bags", "").replace("bag", "")
        if "no other bags" in line[1]:
            contains = []
        else:
            contains = line[1].replace(".", "").replace("bags", "").replace("bag", "")
            contains = contains.split(",")
            contains = [c.strip() for c in contains]
            # contains = [" ".join(c.split(" ")[:-1]) for c in contains]
            contains = [make_bag_tuple(c) for c in contains]
        bag_dict.update({bag: contains})
    return(bag_dict)


def invert_relationship(contains):
    contained_by = {}
    for key in contains.keys():
        for number, colour in contains[key]:
            if colour not in contained_by:
                contained_by[colour] = []
            contained_by[colour].append((number, key))
    return(contained_by)

def part1(data_tidy):
    bag_dict = make_bag_dict(data_tidy)
    contained_by = invert_relationship(bag_dict)
    visited_bags = {"shiny gold"}
    colour_queue = ["shiny gold"]
    n = 0

    while n < len(colour_queue):
        if colour_queue[n] in contained_by:
            for _, colour in contained_by[colour_queue[n]]:
                if colour not in visited_bags:
                    colour_queue.append(colour)
                    visited_bags.add(colour)
        n += 1

    return(len(colour_queue)-1)

def part2(data_tidy):
    bag_dict = make_bag_dict(data_tidy)
    colour_queue = ["shiny gold"]
    multiplier_queue = [1]
    count = 0
    n = 0

    while n < len(colour_queue):
        if colour_queue[n] in bag_dict:
            for number, colour in bag_dict[colour_queue[n]]:
                colour_queue.append(colour)
                multiplier_queue.append(multiplier_queue[n] * number)
                count += multiplier_queue[n] * number
        n += 1

    return count

def main():
    file = "H:\\Projects\\adventofcode\\data\\2021\\day7.txt"

    with open(file,'r') as f:
        data_raw = f.read()
        data_split = [line.rstrip() for line in data_raw.splitlines()]
        data_tidy = [make_tidy_lines(line) for line in data_split]

        print('part 1 solution: %d' %part1(data_tidy))
        print('part 2 solution: %d' %part2(data_tidy))

if __name__ == "__main__":
    main()