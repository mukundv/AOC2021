import os

from aocd import get_data
from dotenv import load_dotenv


def get_session() -> str:
    load_dotenv()
    return os.getenv('SESSION_COOKIE')


def get_list(data=None, day=None, year=None):
    aoc_input = []
    if not data:
        aoc_input = [int(i) for i in get_data(get_session(), day=day, year=year).split('\n')]
    else:
        aoc_input = [int(i) for i in data.split('\n')]
    return aoc_input


# Part 1
def compare_list(input_list):
    greater = 0
    for i, v in enumerate(input_list):
        if i == 0:
            continue
        if v > input_list[i - 1]:
            greater += 1
    return greater


# Part 2
def sliding_window(input_list):
    part2list = []
    for i in range(len(input_list)):
        window = input_list[i:i + 3]
        # print(window)
        if len(window) < 3:
            break
        part2list.append(sum(window))
    return part2list


if __name__ == '__main__':
    print(f'greater = {compare_list(get_list(data=None, day=1, year=2021))}')
    print(f'sliding window = {compare_list(sliding_window(get_list()))}')
