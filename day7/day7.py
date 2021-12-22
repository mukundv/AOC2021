import os

import numpy as np
from aocd import get_data
from dotenv import load_dotenv


def get_session() -> str:
    load_dotenv()
    return os.getenv('SESSION_COOKIE')


def get_list(data: str = None, day: int = None, year: int = None):
    if not data:
        numbers = [int(x) for x in get_data(get_session(), day=day, year=year).split(',')]
    else:
        numbers = [int(x) for x in data.split(',')]
    return numbers


def part1(numbers):
    return get_part1_fuel(get_crabs(numbers), get_median(numbers))


def part2(numbers):
    return get_part2_fuel(get_crabs(numbers), get_mean(numbers))


def get_part2_fuel(crabs, position):
    for crab in crabs:
        crab["fuel"] = get_cheapest_fuel(crab, position)
    return sum([crab["fuel"] for crab in crabs])


def get_cheapest_fuel(crab, position):
    return sum(range(abs(crab["position"] - position) + 1))


def get_part1_fuel(crabs, position):
    for crab in crabs:
        crab["fuel"] = get_horizontal_position(crab, position)
    return sum([crab["fuel"] for crab in crabs])


def get_horizontal_position(crab, position):
    return abs(crab["position"] - position)


def get_crabs(numbers):
    return [{"position": int(i), "fuel": 0} for i in numbers]


def get_median(numbers):
    return round(int(np.median(numbers)))


def get_mean(numbers):
    return round(int(np.mean(numbers)))


print(f"Part 1: {part1(get_list(data=None, day=7, year=2021))}")
print(f"Part 2: {part2(get_list(data=None, day=7, year=2021))}")
