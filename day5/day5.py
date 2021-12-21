import os
import re

import numpy as np
from aocd import get_data
from dotenv import load_dotenv


def get_session() -> str:
    load_dotenv()
    return os.getenv('SESSION_COOKIE')


def get_list(data=None, day=None, year=None):
    if not data:
        aoc_input = get_input(get_data(get_session(), day=day, year=year))
    else:
        aoc_input = get_input(data)
    return aoc_input


def get_input(data):
    aoc_input = []
    for line in data.strip().splitlines():
        n = [int(n) for n in re.findall(r'-?[0-9]+', line)]
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


if __name__ == '__main__':
    print(f'Part 1: {get_overlap(get_list(data=None, day=5, year=2021), False)}')
    print(f'Part 2: {get_overlap(get_list(data=None, day=5, year=2021), True)}')
