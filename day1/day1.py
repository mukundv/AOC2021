def get_list():
    aoc_input = []
    with open("day1_input.txt", "r") as f:
        while line := f.readline().rstrip():
            aoc_input.append(int(line))
    return aoc_input


# Part 1
def compare_list(input_list):
    greater = 0
    for i, v in enumerate(input_list):
        if i == 0:
            continue
        if v > input_list[i - 1]:
            greater += 1
    return greater


# Part 2
def sliding_window(input_list):
    part2list = []
    for i in range(len(input_list)):
        window = input_list[i:i + 3]
        # print(window)
        if len(window) < 3:
            break
        part2list.append(sum(window))
    return part2list


if __name__ == '__main__':
    print(f'greater = {compare_list(get_list())}')
    print(f'sliding window = {compare_list(sliding_window(get_list()))}')
