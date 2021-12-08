import numpy as np

from utils import timeit


def get_lists(input_file_name):
    patterns = []
    outputs = []
    for line in open(input_file_name).readlines():
        patterns.append(line.split(' | ')[0])
        outputs.append(line.split(' | ')[1].replace('\n', ''))
    return patterns, outputs


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


if __name__ == '__main__':
    # fetch_and_save('2021', '8')
    print(part1(get_lists("day8_input.txt")[1]))
