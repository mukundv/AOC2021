import os
from collections import Counter

from aocd import get_data
from dotenv import load_dotenv


def get_session() -> str:
    load_dotenv()
    return os.getenv('SESSION_COOKIE')


def get_input(day: int, year: int, data: str = None):
    if not data:
        return parse_input(get_data(get_session(), day=day, year=year).splitlines())
    else:
        return parse_input(data.splitlines())


def parse_input(data):
    return get_instructions_cubes(data)


def get_instructions_cubes(data):
    instructions = []
    steps = []

    for lines in data:
        x, y = lines[:3].strip(), [lines.replace("\n", "").replace("on ", "").replace("off ", "")]
        instructions += [x]
        steps += y
    return instructions, get_cubes(steps)


def get_cubes(steps):
    cubes = []
    for i in range(len(steps)):
        x, y, z = steps[i].split(',')
        x1, x2 = x.replace('x=', '').split('..')
        y1, y2 = y.replace('y=', '').split('..')
        z1, z2 = z.replace('z=', '').split('..')
        if int(x1) >= -50 and int(x2) <= 50 and int(y1) >= -50 and int(y2) <= 50 and int(z1) >= -50 and int(
                z2) <= 50:
            cubes += [[[int(x1), int(x2)], [int(y1), int(y2)], [int(z1), int(z2)]]]
        else:
            continue
    return cubes


def part1(instructions, cubes):
    return Counter(initialise(instructions=instructions, cubes=cubes).values())['on']


def initialise(cubes, instructions):
    cuboid = {}
    for i in range(len(cubes)):
        # print(i)
        for x in range(cubes[i][0][0], cubes[i][0][1] + 1, 1):
            # print(cubes[i][0][0], cubes[i][0][1] + 1, 1)
            for y in range(cubes[i][1][0], cubes[i][1][1] + 1, 1):
                # print(cubes[i][1][0], cubes[i][1][1] + 1, 1)
                for z in range(cubes[i][2][0], cubes[i][2][1] + 1, 1):
                    # print(cubes[i][2][0], cubes[i][2][1] + 1, 1)
                    if (x, y, z) not in cuboid:
                        cuboid[x, y, z] = instructions[i]
                    else:
                        if not cuboid[x, y, z] != 'on' and not instructions[i] != 'off':
                            cuboid[x, y, z] = 'off'
                        elif not cuboid[x, y, z] != 'off' and not instructions[i] != 'on':
                            cuboid[x, y, z] = 'on'
    return cuboid


if __name__ == '__main__':
    print(f'Part 1: {part1(*get_input(day=22, year=2021))}')
