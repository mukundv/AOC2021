import numpy as np

from utils import profile


def get_list(input_file_name):
    aoc_input = []
    for x in open(input_file_name).read().split(','):
        aoc_input.append(int(x))
    return aoc_input


# This method works for 80 days and does not scale for 256 days
@profile
def get_total_fish(aoc_input, days):
    for day in range(days):
        aoc_input_copy = []
        for timer in aoc_input:
            if timer == 0:  # Each day 0 becomes a 6 and adds a new 8 to the end of the list
                aoc_input_copy.append(6)
                aoc_input_copy.append(8)
            else:
                aoc_input_copy.append(timer - 1)  # Decrease the timer of each fish after each day
        aoc_input = aoc_input_copy
    return len(aoc_input_copy)


# np.roll is awesome. Saves inserting, deleting, shifting
@profile
def part2(aoc_input, days):
    np_array = np.zeros(9, dtype=int)  # Get a 1D array of 0's
    for x in aoc_input:
        np_array[x] += 1  # Count the timers
    for day in range(days):
        np_array = np.roll(np_array, -1)
        np_array[6] += np_array[8]
    return np.sum(np_array)


if __name__ == '__main__':
    print(f'Part 1: {get_total_fish(get_list("day6_input.txt"), 80)}')
    print(f'Part 2: {part2(get_list("day6_input.txt"), 256)}')
