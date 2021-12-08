import numpy as np

from utils import timeit, generate_readme


def get_lists(input_file_name):
    patterns = []
    outputs = []
    for line in open(input_file_name).readlines():
        patterns.append(line.split(' | ')[0])
        outputs.append(line.split(' | ')[1].replace('\n', ''))
    return patterns, outputs

@timeit
def get_test(input_file_name):
    with open(input_file_name) as f:
        out = [[d.split(" ") for d in i.split(" | ")] for i in f.read().splitlines()]
    print(out)


@timeit
def part1(outputs):
    out = []
    count = 0
    interested_lengths = [2, 3, 4, 7]
    for i in outputs:
        j = i.split(' ')
        for k in j:
            out.append(k)
    arr = np.array(out)
    sizes = np.char.str_len(arr)

    for i in interested_lengths:
        count += len(sizes[sizes == i])
    return count

@timeit
def part2(input_file_name):
    lines = [line.strip() for line in open(input_file_name) if line.strip()]
    parts = [line.partition(" | ") for line in lines]
    data = [(patterns.split(), outputs.split()) for patterns, _, outputs in parts]
    value = [decode(p, o) for p, o in data]
    return sum(value)


def decode(patterns, outputs):
    known = {}
    for i in patterns:
        if len(i) == 2:
            known[1] = set(i)
        if len(i) == 3:
            known[7] = set(i)
        if len(i) == 4:
            known[4] = set(i)
        if len(i) == 7:
            known[8] = set(i)
    for i in patterns:
        if len(i) == 6:
            if len(set(i).intersection(known[1])) == 1:
                known[6] = set(i)
            elif len(set(i).intersection(known[4])) == 4:
                known[9] = set(i)
            else:
                known[0] = set(i)
    for i in patterns:
        if len(i) == 5:
            if len(set(i).intersection(known[1])) == 2:
                known[3] = set(i)
            elif len(set(i).intersection(known[6])) == 5:
                known[5] = set(i)
            else:
                known[2] = set(i)
    decoded = []
    for o in outputs:
        for p in known:
            if known[p] == set(o):
                decoded.append(p)
    return decoded[0] * 1000 + decoded[1] * 100 + decoded[2] * 10 + decoded[3]


if __name__ == '__main__':
    # fetch_and_save('2021', '8')
    print(f'Part1: {part1(get_lists("day8_input.txt")[1])}')
    print(f'Part2: {part2("day8_input.txt")}')
    generate_readme("README", '2021','8')
