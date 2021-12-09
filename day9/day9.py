import numpy as np
from utils import timeit,generate_readme


def get_input(input_file_name):
    return np.genfromtxt(input_file_name, delimiter=1, dtype=int)


def get_neighbours(array, x, y):
    if x > 0:
        yield array[x - 1][y]
    if x < len(array) - 1:
        yield array[x + 1][y]
    if y > 0:
        yield array[x][y - 1]
    if y < len(array[x]) - 1:
        yield array[x][y + 1]


def get_coordinates(array, x, y):
    if x > 0:
        yield x - 1, y
    if x < len(array) - 1:
        yield x + 1, y
    if y > 0:
        yield x, y - 1
    if y < len(array[x]) - 1:
        yield x, y + 1


def basins(array, x, y):
    points = {(x, y)}
    data = [(x1, y1) for (x1, y1) in get_coordinates(array, x, y) if array[x1][y1] != 9]
    while data:
        x1, y1 = data.pop()
        if (x1, y1) not in points:
            points.add((x1, y1))
            for x2, y2 in get_coordinates(array, x1, y1):
                if array[x2][y2] != 9:
                    data.append((x2, y2))
    return len(points)

@timeit
def part1(array):
    low_points = []
    for (x, y), value in np.ndenumerate(array):
        if all(value < neighbour for neighbour in get_neighbours(array, x, y)):
            low_points.append([x, y, value])
    return low_points

@timeit
def part2(array):
    a = np.array([basins(array, x, y) for x, y, _ in part1(array)])
    return a[np.argsort(a)[-3:]]


if __name__ == '__main__':
    print(f'Part1: {sum(value + 1 for [_, _, value] in part1(get_input("day9_input.txt")))}')
    print(f'Part2: {np.prod(part2(get_input("day9_input.txt")))}')
    generate_readme("README", '2021', '9', '../')
