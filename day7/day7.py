from utils import timeit


def get_list(input_file_name):
    aoc_input = []
    for x in open(input_file_name).read().split(','):
        aoc_input.append(int(x))
    pos = range(min(aoc_input), max(aoc_input) + 1)
    return aoc_input, pos


@timeit
def part1(aoc_input, pos):
    cost = []
    for i in pos:
        k = sum(abs(i - j) for j in aoc_input)
        cost.append(k)
    return min(cost)


@timeit
def part2(aoc_input, pos):
    x = None
    for i in pos:
        j = sum(sum(range(abs(k - i) + 1)) for k in aoc_input)
        if x is None or x > j:
            x = j
    return x


if __name__ == '__main__':
    print(part1(*get_list("day7_input.txt")))
    print(part2(*get_list("day7_input.txt")))
