import os
import re
from collections import Counter

from aocd import get_data
from dotenv import load_dotenv

from utils import generate_readme


def get_session() -> str:
    load_dotenv()
    return os.getenv('SESSION_COOKIE')


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


def overlap(values, x, y):
    if len(values) == 0 or values[-1] < x or values[0] > y:
        return range(-1)
    return range(min(max(values[0], x), y), min(max(values[-1], x), y) + 1)


def part2(data):
    cubes = get_cubes(data)
    ret = 0
    for i, (instruction, x, y, z) in enumerate(cubes):
        if instruction == 'on':
            ret += count_within_range(x, y, z, cubes[i + 1:])
    return ret


def get_cubes(data):
    cubes = []
    reg = re.compile(r"^(on|off) x=(-?[0-9]+)\.\.(-?[0-9]+),y=(-?[0-9]+)\.\.(-?[0-9]+),z=(-?[0-9]+)\.\.(-?[0-9]+)$")
    # https://regex101.com/r/GKuwQm/1
    for line in data:
        _ = reg.search(line)
        cubes.append((
            _.group(1),
            range(int(_.group(2)), int(_.group(3)) + 1),
            range(int(_.group(4)), int(_.group(5)) + 1),
            range(int(_.group(6)), int(_.group(7)) + 1),
        ))
    return cubes


def count_within_range(x, y, z, remaining):
    if len(x) == 0 or len(y) == 0 or len(z) == 0:
        return 0
    ret = len(x) * len(y) * len(z)
    temp = []

    for instruction, i, j, k in remaining:
        overlap_x = overlap(i, x[0], x[-1])
        if len(overlap_x) > 0:
            overlap_y = overlap(j, y[0], y[-1])
            if len(overlap_y) > 0:
                overlap_z = overlap(k, z[0], z[-1])
                if len(overlap_z) > 0:
                    temp.append((instruction, overlap_x, overlap_y, overlap_z))

    for i, (instruction, x, y, z) in enumerate(temp):
        ret -= count_within_range(x, y, z, temp[i + 1:])

    return ret


def get_instructions_cubes(data):
    instructions = []
    steps = []
    for lines in data:
        x, y = lines[:3].strip(), [lines.replace("\n", "").replace("on ", "").replace("off ", "")]
        instructions += [x]
        steps += y
    return instructions, get_cubes_from_steps(steps)


def get_cubes_from_steps(steps):
    cubes = []
    for i in range(len(steps)):
        x1, x2 = steps[i].split(',')[0].replace('x=', '').split('..')
        y1, y2 = steps[i].split(',')[1].replace('y=', '').split('..')
        z1, z2 = steps[i].split(',')[2].replace('z=', '').split('..')
        if less_than_fifty(x1, x2, y1, y2, z1, z2):
            cubes += [[[int(x1), int(x2)], [int(y1), int(y2)], [int(z1), int(z2)]]]
    return cubes


def part1(data):
    instructions, cubes = get_instructions_cubes(data)
    return Counter(initialise(instructions=instructions, cubes=cubes).values())['on']


def initialise(cubes, instructions):
    cuboid = {}
    for i in range(len(cubes)):
        for x in range(cubes[i][0][0], cubes[i][0][1] + 1, 1):
            for y in range(cubes[i][1][0], cubes[i][1][1] + 1, 1):
                for z in range(cubes[i][2][0], cubes[i][2][1] + 1, 1):
                    if (x, y, z) not in cuboid:
                        cuboid[x, y, z] = instructions[i]
                    else:
                        if not cuboid[x, y, z] != 'on' and not instructions[i] != 'off':
                            cuboid[x, y, z] = 'off'
                        elif not cuboid[x, y, z] != 'off' and not instructions[i] != 'on':
                            cuboid[x, y, z] = 'on'
    return cuboid


def less_than_fifty(x1, x2, y1, y2, z1, z2):
    if int(x1) >= -50 and int(x2) <= 50 and int(y1) >= -50 and int(y2) <= 50 and int(z1) >= -50 and int(
            z2) <= 50:
        return True


if __name__ == '__main__':
    print(f' Part 1: {run(data=None, day=22, year=2021, part=1)}')
    print(f' Part 2: {run(data=None, day=22, year=2021, part=2)}')
    generate_readme("README", '2021', '22', '../')
