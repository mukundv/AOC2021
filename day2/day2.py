import os

from aocd import get_data
from dotenv import load_dotenv


def get_session() -> str:
    load_dotenv()
    return os.getenv('SESSION_COOKIE')


def get_list(data=None, day=None, year=None):
    aoc_input = []
    if not data:
        aoc_input = [line.rstrip() for line in get_data(get_session(), day=day, year=year).splitlines()]
    else:
        aoc_input = [line.rstrip() for line in data.splitlines()]
    return aoc_input


# Part 1
def compare_list(input_list):
    horizontal_position, depth = 0, 0
    for input_line in input_list:
        direction, number = input_line.strip().split()
        number = int(number)
        if direction == 'forward':  # Add number to horizontal position
            horizontal_position += number
        elif direction == 'up':  # Subtract number from depth
            depth -= number
        elif direction == 'down':  # Add number to depth
            depth += number
        else:
            print(f"{direction} is unknown")
    print(f'Final is {horizontal_position} * {depth} = {horizontal_position * depth}')
    return horizontal_position * depth


# Part 2

def get_aim(input_list):
    horizontal_position, depth, aim = 0, 0, 0
    for input_line in input_list:
        direction, number = input_line.strip().split()
        number = int(number)
        if direction == 'forward':
            horizontal_position += number  # Add number to horizontal position
            depth += aim * number  # Increase depth by aim * number
        elif direction == 'up':
            aim -= number  # Decrease aim by number
        elif direction == 'down':
            aim += number  # Increase aim by number
        else:
            print(f"{direction} is unknown")
    print(f'Final is {horizontal_position} * {depth} = {horizontal_position * depth}')
    return horizontal_position * depth


if __name__ == '__main__':
    print(f'Part 1: Horizontal Position * depth = {compare_list(get_list(data=None, day=2, year=2021))}')
    print(f'Part 2: Horizontal Position * depth = {get_aim(get_list(data=None, day=2, year=2021))}')
