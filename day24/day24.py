import os

from aocd import get_data, submit
from dotenv import load_dotenv

from utils import generate_readme


def get_session() -> str:
    load_dotenv()
    return os.getenv('SESSION_COOKIE')


def alu(commands, inp):
    slices = []
    for i in range(14):  # There are 14 slices of commands
        divide, check, add = map(int, get_divide_check_add(commands, i))
        if divide == 1:
            slices.append((i, add))
        elif divide == 26:
            j, add = slices.pop()
            adjust_inp(add, check, i, inp, j)
    return inp


def adjust_inp(add, check, i, inp, j):
    inp[i] = inp[j] + add + check
    if inp[i] > 9:
        inp[j] -= inp[i] - 9
        inp[i] = 9
    if inp[i] < 1:
        inp[j] += 1 - inp[i]
        inp[i] = 1


def get_divide_check_add(commands, i):
    return [commands[i * 18 + x][-1] for x in [4, 5, 15]]


def part1(data):
    inp = [9] * 14
    return "".join(map(str, alu([line.split() for line in data], inp)))


def part2(data):
    inp = [1] * 14
    return "".join(map(str, alu([line.split() for line in data], inp)))


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


def submit_answer(a_1, a_2):
    submit(answer=a_1, session=get_session(), part='a', day=24, year=2021)
    submit(answer=a_2, session=get_session(), part='b', day=24, year=2021)


if __name__ == '__main__':
    submit_answer(run(day=24, year=2021, data=None, part=1),run(day=24, year=2021, data=None, part=2))
    generate_readme("README", '2021', '24', '../')
