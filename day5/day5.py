import numpy as np
import re


def get_list(input_file_name):
    aoc_input = []
    for line in open(input_file_name).read().strip().splitlines():
        s = re.findall(r'-?[0-9]+', line)  # should've done this in earlier puzzles.
        n = [int(n) for n in s]
        aoc_input.append(n)
    return aoc_input


def get_overlap(aoc_input, diag):
    matrix = np.zeros((np.max(aoc_input), np.max(aoc_input)), dtype=int)
    for x0, y0, x1, y1 in aoc_input:
        if x0 == x1 or y0 == y1:
            matrix[min(y0, y1):max(y0, y1) + 1, min(x0, x1):max(x0, x1) + 1] += 1
        elif diag:
            for i, j in zip(build_range(x0, x1), build_range(y0, y1)):
                matrix[i, j] += 1
    return (matrix >= 2).sum().sum()


def build_range(x, y):
    if y > x:
        return list(range(x, y + 1))
    else:
        return list(range(x, y - 1, -1))


#
# def part1(aoc_input):
#     matrix = np.zeros((np.max(aoc_input), np.max(aoc_input)), dtype=int)
#     for x0, y0, x1, y1 in aoc_input:
#         if x0 == x1 or y0 == y1:
#             matrix[min(y0, y1):max(y0, y1) + 1, min(x0, x1):max(x0, x1) + 1] += 1
#     return (matrix >= 2).sum().sum()
#
#
# def part2(aoc_input):
#     matrix = np.zeros((np.max(aoc_input), np.max(aoc_input)), dtype=int)
#     for x0, y0, x1, y1 in aoc_input:
#         if x0 == x1 or y0 == y1:
#             matrix[min(y0, y1):max(y0, y1) + 1, min(x0, x1):max(x0, x1) + 1] += 1
#         elif True:
#
#     return (matrix >= 2).sum().sum()
#
#

if __name__ == '__main__':
    print(f'Part 1: {get_overlap(get_list("day5_input.txt"),False)}')
    print(f'Part 2: {get_overlap(get_list("day5_input.txt"),True)}')

