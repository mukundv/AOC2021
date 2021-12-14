import numpy as np

from utils import generate_readme


def get_inputs(path):
    with open(path) as f:
        inputs = f.read()
        dots, instructions = inputs.split("\n\n")
    return [[int(i) for i in i.strip().split(",") if i != ""] for i in dots.split("\n")], instructions.split("\n")


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


def fold_y(paper, coord):
    copy = np.zeros((coord, paper.shape[1]))
    dist = paper.shape[0] - coord - 1
    copy[-dist:, :] = paper[coord - dist:coord, :] + np.flipud(paper[coord + 1:, :])
    copy[:-dist, :] = paper[:coord - dist, :]
    return np.minimum(1, copy)


def fold_x(paper, coord):
    copy = np.zeros((paper.shape[0], coord))
    dist = paper.shape[1] - coord - 1
    copy[:, -dist:] = paper[:, coord - dist:coord] + np.fliplr(paper[:, coord + 1:])
    copy[:, :-dist] = paper[:, :coord - dist]
    return np.minimum(1, copy)


def part1(input_file_name):
    dots, instructions = get_inputs(input_file_name)
    dots = np.array(dots)
    paper = np.zeros((dots[:, 1].max() + 1, dots[:, 0].max() + 1))
    paper[dots[:, 1], dots[:, 0]] = 1
    for i, instruction in enumerate(instructions):
        val = instruction.split(" ")[-1]
        axis, coord = val.split("=")
        coord = int(coord)
        if i == 0:
            print(int(paper.sum()))

        if axis == 'x':
            paper = fold_x(paper, coord)
        else:
            paper = fold_y(paper, coord)

    paper = np.char.mod('%d', paper)
    x = ["".join(paper[i, :]) for i in range(paper.shape[0])]
    print("\n".join(x).replace("1", "#").replace("0", " "))
    print(x)


if __name__ == '__main__':
    print(f'Part1: {part1("day13_input.txt")}')
    generate_readme("README", '2021', '13', '../')
