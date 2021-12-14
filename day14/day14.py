from collections import defaultdict

pairs = []


def get_inputs(input_file_name):
    rules = []
    for i, value in enumerate(open(input_file_name).read().splitlines()):
        if i == 0:
            polymer_template = value
        elif value:
            rules.append(value)
    return rules, polymer_template


def get_pairs(rules):
    for line in rules:
        pairs.append(line.split(' -> '))
    return pairs


def get_counts(polymer):
    element_count = defaultdict(int)
    pair_count = defaultdict(int)

    for i in range(len(polymer) - 1):
        element_count[polymer[i]] += 1
        pair_count[polymer[i:i + 2]] += 1
    element_count[polymer[-1]] += 1

    return element_count, pair_count


def insert_polymer_pairs(pair_count, element_count,pair):
    for pair, count in pair_count.copy().items():
        pair_count[pair] -= count
        # # add = pairs[pair]
        # element_count[add] += count
        # pair_count[pair[0] + add] += count
        # pair_count[add + pair[1]] += count


def run(rules, polymer_template, part):
    p = get_pairs(rules)
    element_count, pair_count = get_counts(polymer_template)
    for i in range(10):
        insert_polymer_pairs(pair_count, element_count)


if __name__ == '__main__':
    get_inputs("day14_example.txt")