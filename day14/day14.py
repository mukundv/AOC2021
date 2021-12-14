from collections import Counter

from utils import timeit, generate_readme


def get_inputs(input_file_name):
    with open(input_file_name, 'r') as f:
        lines = f.readlines()
    return lines


def run(lines, times):
    rules = get_rules(lines)
    state = get_state(lines)
    for _ in range(times):
        new_state = Counter()
        for pair, count in state.items():
            for match in rules[pair]:
                new_state[match] += count
        state = new_state
    counts = get_counts(lines)
    update_counts(counts, state)
    return get_final_value(counts)


def get_final_value(counts):
    return (max(counts.values()) - min(counts.values())) // 2


def update_counts(counts, state):
    for pair, count in state.items():
        for c in pair:
            counts[c] += count


def get_counts(lines):
    counts = Counter(lines[0][0] + lines[0].rstrip()[-1])
    return counts


def get_state(lines):
    state = Counter(a + b for a, b in zip(lines[0], lines[0][1:].rstrip()))
    return state


def get_rules(lines):
    rules = {
        line[:2]: (line[0] + line[-1], line[-1] + line[1])
        for line in map(str.strip, lines[2:])
    }
    return rules


@timeit
def part1(lines):
    return run(lines, 10)


@timeit
def part2(lines):
    return run(lines, 40)


if __name__ == '__main__':
    print(f'part1: {part1(get_inputs("day14_input.txt"))}')
    print(f'part2: {part2(get_inputs("day14_input.txt"))}')
    generate_readme("README", '2021', '14', '../')
