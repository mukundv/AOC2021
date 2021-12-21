import os
import typing

import numpy as np
from aocd import get_data
from dotenv import load_dotenv

from utils import timeit


def get_session() -> str:
    load_dotenv()
    return os.getenv('SESSION_COOKIE')


def get_list(data: str = None, day: int = None, year: int = None) -> typing.List:
    if not data:
        aoc_input = [int(x) for x in get_data(get_session(), day=day, year=year).split(',')]
    else:
        aoc_input = [int(x) for x in data.split(',')]
    return aoc_input


# This method works for 80 days and does not scale for 256 days
@timeit
def part1(aoc_input: typing.List, days: int) -> int:
    aoc_input_copy = []
    aoc_input_copy = flash(aoc_input, aoc_input_copy, days)
    return int(len(aoc_input_copy))


def flash(aoc_input: list, aoc_input_copy: typing.List, days: int) -> typing.List:
    for day in range(days):
        aoc_input_copy = []
        for timer in aoc_input:
            if timer == 0:  # Each day 0 becomes a 6 and adds a new 8 to the end of the list
                aoc_input_copy.append(6)
                aoc_input_copy.append(8)
            else:
                aoc_input_copy.append(timer - 1)  # Decrease the timer of each fish after each day
        aoc_input = aoc_input_copy
    return aoc_input_copy


@timeit
def part2(aoc_input: typing.List, days: int) -> int:
    np_array = np.zeros(9, dtype=np.float64)  # Get a 1D array of 0's
    for x in aoc_input:
        np_array[x] += 1  # Count the timers
    for day in range(days):
        np_array = np.roll(np_array, -1)
        # np.roll is awesome.
        # Saves inserting, deleting, shifting
        np_array[6] += np_array[8]
    return int(np.sum(np_array))


if __name__ == '__main__':
    print(f'Part 1: {part1(get_list(data=None, day=6, year=2021), 80)}')
    print(f'Part 2: {part2(get_list(data=None, day=6, year=2021), 256)}')
