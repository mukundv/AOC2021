from utils import generate_readme
pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

close = [")", "]", "}", ">"]

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

completion_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

error = []
scores = []


def get_input(input_file_name):
    aoc_input = open(input_file_name).read().strip().split('\n')
    return aoc_input


def get_error_scores(aoc_input):
    closed = []
    score = 0
    for i in aoc_input:
        for character in i:
            if character not in close:
                closed.append(character)
            else:
                if character == pairs[closed[-1]]:
                    closed.pop()
                else:
                    error.append(points[character])
                    closed = []
                    break
        if closed:
            for p in [pairs[i] for i in closed[::-1]]:
                score = (score * 5) + completion_points[p]
            scores.append(score)
    return error, scores


def part2(s):
    return sorted(s)[len(s)//2]


if __name__ == '__main__':
    print(f'Part1: {sum(get_error_scores(get_input("day10_input.txt"))[0])}')
    print(f'Part2: {part2(get_error_scores(get_input("day10_input.txt"))[1])}')
    generate_readme("README", '2021', '10', '../')
