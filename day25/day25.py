import os
from itertools import count

from aocd import get_data, submit
from dotenv import load_dotenv

from utils import generate_readme


def get_session() -> str:
    load_dotenv()
    return os.getenv('SESSION_COOKIE')


def calculate(grid):
    h, w = len(grid), len(grid[0])
    steps = 0
    for steps in count(1):
        go_next = []
        for r in range(h):
            for c in range(w):
                new_c = (c + 1) % w
                if grid[r][c] == '>' and grid[r][new_c] == '.':
                    go_next.append((r, c, new_c))
        for r, c, new_c in go_next:
            grid[r][c] = '.'
            grid[r][new_c] = '>'
        horiz_still = not go_next
        go_next = []
        for r in range(h):
            for c in range(w):
                new_r = (r + 1) % h
                if grid[r][c] == 'v' and grid[new_r][c] == '.':
                    go_next.append((r, c, new_r))
        if horiz_still and not go_next:
            break
        for r, c, new_r in go_next:
            grid[r][c] = '.'
            grid[new_r][c] = 'v'
    return steps


def part1(data):
    return calculate(list(map(list, [list(x) for x in [line for line in data]])))


def part2(data):
    return


def run(day: int, year: int, data: str = None, part: int = None):
    if not data:
        if part == 1:
            return part1(get_data(get_session(), day=day, year=year).splitlines())
        else:
            return part2(get_data(get_session(), day=day, year=year).splitlines())
    else:
        if part == 1:
            return part1(data.splitlines())
        else:
            return part2(data.splitlines())


def submit_answer(a_1=None, a_2=None):
    if a_1:
        submit(answer=a_1, session=get_session(), part='a', day=25, year=2021)
    elif a_2:
        submit(answer=a_2, session=get_session(), part='b', day=25, year=2021)
    elif a_1 and a_2:
        submit(answer=a_1, session=get_session(), part='a', day=25, year=2021)
        submit(answer=a_2, session=get_session(), part='b', day=25, year=2021)


if __name__ == '__main__':
    print(f'Part 1: {run(day=25, year=2021, data=None, part=1)}')
    submit_answer(a_1=run(day=25, year=2021, data=None, part=1))
    generate_readme("README", '2021', '25', '../')
