import numpy as np


def get_inputs(input_file_name):
    instructions = []
    dots = []
    for line in open(input_file_name).read().strip().splitlines():
        if line[:1] == 'f':
            line = line.replace('fold along ', '')
            instructions.append([line.split('=')[0], line.split('=')[1]])
        else:
            if len(line) > 0:
                dots.append(line)
    return dots, instructions


def find_max(array):
    x = []
    y = []
    for line in array:
        x.append(int(line.split(',')[0]))
        y.append(int(line.split(',')[1]))
    return [max(x), max(y)]


def get_paper(dots):
    array_size = find_max(dots)
    paper = np.zeros((array_size[1] + 1, array_size[0] + 1), dtype=int)
    for line in dots:
        x, y = line.split(',')
        paper[int(y), int(x)] = 1
    return paper


def fold(paper, instructions):
    axis = instructions[0]
    position = int(instructions[1])
    if axis == 'y':
        top_paper = paper[0:position, :]
        bottom_paper = paper[position + 1:, :]
        y = top_paper | np.flipud(bottom_paper)
        return np.minimum(1, top_paper + np.flipud(bottom_paper))
    elif axis == 'x':
        left_paper = paper[:, 0:position]
        right_paper = paper[:, position + 1:]
        x = left_paper | np.fliplr(right_paper)
        return np.minimum(1, left_paper + np.fliplr(right_paper))


def part1(paper, instructions):
    return fold(paper, instructions).sum()


def part2(paper, instructions):
    for i, j in instructions:
        matrix = fold(paper, [i, j])
    print(matrix)


if __name__ == '__main__':
    print(f'Part1: {part1(get_paper(get_inputs("day13_input.txt")[0]), get_inputs("day13_input.txt")[1][0])}')
    print(f'Part2: {part2(get_paper(get_inputs("day13_input.txt")[0]), get_inputs("day13_input.txt")[1])}')
    # print((get_inputs("day13_example.txt")))
