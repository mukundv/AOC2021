from collections import defaultdict
from utils import generate_readme

aoc_input = defaultdict(list)


def get_input(input_file_name):
    for line in open(input_file_name).read().strip().splitlines():
        x, y = line.split('-')
        aoc_input[x].append(y)
        aoc_input[y].append(x)
    return aoc_input


def count(path, caves, twice=False):
    c = 0
    if path[-1] == 'end':
        return 1
    for i in caves[path[-1]]:
        if i.isupper() or i not in path:
            c += count(path + [i], caves,twice)
        elif twice and i not in ["start", "end"]:
            c += count(path + [i], caves, False)
    return c


if __name__ == '__main__':
    aoc_input = get_input("day12_input.txt")
    print(f'Part1: {count(["start"], aoc_input)}')
    print(f'Part2: {count(["start"], aoc_input, twice=True)}')
    generate_readme("README", '2021', '12', '../')
