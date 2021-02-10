def make_tidy_lines(line):
    line_tidy = line
    line_tidy = line_tidy.split(' contain ')
    return(line_tidy)

def make_bag_tuple(c) -> [int, str]:
    number = int(c.split(" ")[0])
    colour = " ".join(c.split(" ")[1:])
    return(number, colour)

def invert_relationship(contains):
    contained_by = {}
    for key in contains.keys():
        for number, colour in contains[key]:
            if colour not in contained_by:
                contained_by[colour] = []
            contained_by[colour].append((number, key))
    return(contained_by)

def part1(data_tidy):
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

    contained_by = invert_relationship(bag_dict)
    visited_bags = {"shiny gold"}
    colour_queue = ["shiny gold"]
    ix = 0

    while ix < len(colour_queue):
        if colour_queue[ix] in contained_by:
            for _number, colour in contained_by[colour_queue[ix]]:
                if colour not in visited_bags:
                    colour_queue.append(colour)
                    visited_bags.add(colour)
        ix += 1

    return(len(colour_queue)-1)


def main():
    file = "H:\\Projects\\adventofcode\\data\\day7.txt"

    with open(file,'r') as f:
        data_raw = f.read()
        data_split = [line.rstrip() for line in data_raw.splitlines()]
        data_tidy = [make_tidy_lines(line) for line in data_split]

        print(part1(data_tidy))

        breakpoint()

        # bag_dict = {}
        # for line in data_tidy:
        #     bag = " ".join(line[0].split(" ")[:2]).replace("bags", "").replace("bag", "")
        #     if "no other bags" in line[1]:
        #         contains = []
        #     else:
        #         contains = line[1].replace(".", "").replace("bags", "").replace("bag", "")
        #         contains = contains.split(",")
        #         contains = [c.strip() for c in contains]
        #         # contains = [" ".join(c.split(" ")[:-1]) for c in contains]
        #         contains = [make_bag_tuple(c) for c in contains]
        #     bag_dict.update({bag: contains})
        #
        # SHINY_GOLD = "shiny gold"
        #
        # contained_by = invert_relationship(bag_dict)
        # visited_bags = {"shiny gold"}
        # colour_queue = ["shiny gold"]
        # ix = 0
        #
        # breakpoint()
        #
        # while ix < len(colour_queue):
        #     if colour_queue[ix] in contained_by:
        #         for _number, colour in contained_by[colour_queue[ix]]:
        #             if colour not in visited_bags:
        #                 colour_queue.append(colour)
        #                 visited_bags.add(colour)
        #     ix += 1
        # print(len(colour_queue)-1)
        breakpoint()






    # # breakpoint()
    # bags_tuple = [get_bags(line) for line in data_tidy]
    # bags_list, contains_list = zip(*bags_tuple)
    #
    # bag_types = []
    # bags = {}
    # for i in range(len(bags_list)):
    #     if bags_list[i] not in bag_types:
    #         bag_types.append(bags_list[i])
    #     if bags.get(bags_list[i]):
    #         print(bags_list[i])
    #         # contains_list[i].update(bags)
    #     bags[bags_list[i]] = contains_list[i]
        
    # bags_gold = 0
    # bag_type = "shiny gold"
    
    

    # print("end")

    # def check_bag(bags, my_bag, current_bag):
    #     if current_bag==my_bag:
    #         return 1
    #     if bags.get(current_bag) is None:
    #         return 0
    #     else:
    #         counts = []
    #         for k, v in bags[current_bag].items():
    #             counts.append(check_bag(bags, my_bag, k))
    #         return max(counts)

    # bag_types = []
    # all_bags = {}
    # for line in lines:
    #     mbag = " ".join(line.split(" ")[:2])
    #     contains = line[line.index("contain ")+8:-1]
    #     each_contain = contains.split(",")
    #     each_contain = [cnt.lstrip() for cnt in each_contain]
    #     each_contain = [" ".join(cont.split(" ")[:-1]) for cont in each_contain]
    #     print(each_contain)
    #     each_contain = {" ".join(cont.split(" ")[1:]):cont.split(" ")[0] for cont in each_contain}
    #     print(each_contain)
    #     if mbag not in bag_types:
    #         bag_types.append(mbag)
    #     if all_bags.get(mbag):
    #         each_contain.update(all_bags[mbag]) 
    #     all_bags[mbag] = each_contain


    # found_bags = 0
    # my_bag = "shiny gold"
    # for k, v in all_bags.items():
    #     if k != my_bag:
    #         found_bags+=check_bag(all_bags, my_bag, k)
    #         print(f"{found_bags} bags can contain {my_bag} bag.")

    # print("the end")

def get_bags(line):
    contains_dict2 = {}
    bag = " ".join(line[0].split(" ")[:2]).replace("bags","").replace("bag","")
    contains = line[1].replace(".","").replace("bags","").replace("bag","")
    contains = contains.split(",")
    contains = [c.strip() for c in contains]
    contains = [" ".join(c.split(" ")[:-1]) for c in contains]
    contains_dict = {" ".join(c.split(" ")[1:]):c.split(" ")[0] for c in contains}
    # contains_dict2 = {" ".join(c.split(" ")[1:]):c.split(" ")[0] for c in contains_dict}

    print(bag, contains_dict)
    return(bag, contains_dict)
    # return(contains_dict)

if __name__ == "__main__":
    main()