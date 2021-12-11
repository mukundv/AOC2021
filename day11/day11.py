import numpy as np
from utils import timeit, generate_readme


def get_input(input_file_name):
    return np.genfromtxt(input_file_name, delimiter=1, dtype=int)


def get_neighbours(x):
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                pass
            elif (x[0] + i) < 0 or (x[1] + j) < 0 or (x[0] + i) > 9 or (x[1] + j) > 9:
                pass
            else:
                neighbours.append([x[0] + i, x[1] + j])
    return neighbours


def flash(array, sync):
    count = 0
    for i in range(1, array.size * 10):
        array += 1
        while array.max() > 9:
            x = np.argwhere(array > 9)
            for y in x:
                array[y[0], y[1]] = 0
                for neighbour in get_neighbours(y):
                    if array[neighbour[0], neighbour[1]] != 0:
                        array[neighbour[0], neighbour[1]] += 1 # increase energy of octo
        count += np.count_nonzero(array == 0) # increase count
        if np.count_nonzero(array == 0) == array.size:
            return i
        if i == array.size and not sync:
            return count

@timeit
def part1(array, sync):
    return flash(array, sync)

@timeit
def part2(array, sync):
    return flash(array, sync)


if __name__ == '__main__':
    print(f'Part1: {part1(get_input("day11_input.txt"), False)}')
    print(f'Part2: {part2(get_input("day11_input.txt"), True)}')
    generate_readme("README", '2021', '11', '../')
