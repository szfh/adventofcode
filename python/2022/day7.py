import os
import sys
import copy

sys.path.append(os.path.abspath("../scripts"))


def make_tidy_data(data_raw):
    data_tidy = data_raw.splitlines()
    data_split = [line.split(' ') for line in data_tidy]
    return data_split


def create_file_structure(line, current_path, all_paths, files):
    match line[0]:
        case '$':
            match line[1]:
                case 'cd':
                    match line[2]:
                        case '..':
                            current_path.pop()
                        case _:
                            current_path.append(line[2])
                case 'ls':
                    pass
        case 'dir':
            all_paths.add(tuple(current_path + list(line[1:2])))
        case _:
            files.append(copy.deepcopy({'name': line[1], 'size': int(line[0]), 'path': current_path}))
    return (line, current_path, all_paths, files)


def get_folder_sizes(folder_sizes, folder_path, files):
    size = 0
    for file in files:
        if file['path'][0:len(folder_path)] == list(folder_path):
            size += file['size']
    folder_sizes.append(copy.deepcopy({'path': folder_path, 'size': size}))
    return (folder_sizes, folder_path)


def part1(data):
    current_path = []
    all_paths = set()
    all_paths.add(tuple('/'))
    files = []

    for line in data:
        line, current_path, all_paths, files = create_file_structure(line, current_path, all_paths, files)

    folder_sizes = []
    for folder_path in list(all_paths):
        get_folder_sizes(folder_sizes, folder_path, files)

    total_file_size, max_folder_size = 0, 100000
    for f in folder_sizes:
        if f['size'] <= max_folder_size:
            total_file_size += f['size']

    return total_file_size


def part2(data):
    return 2


def main():
    file = os.path.abspath("../../data/2022/day7.txt")

    with open(file, 'r') as f:
        data_raw = f.read()

    data = make_tidy_data(data_raw)

    print('part 1 solution: %d' % part1(data))
    print('part 2 solution: %d' % part2(data))


if __name__ == "__main__":
    main()
