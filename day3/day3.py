def get_list(input_file_name):
    with open(input_file_name, "r") as f:
        aoc_input = [line.rstrip() for line in f]
    # print(aoc_input)
    return aoc_input


def get_power_consumption(input_list):
    gamma, epsilon = '', ''
    for i in range(len(input_list[0])):
        counter = {'0': 0, '1': 0}
        for row in input_list:
            counter[row[i]] += 1
        if counter['0'] > counter['1']:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    # print( f'Gamma = {int(gamma, 2)}, Epsilon = {int(epsilon, 2)}, Power Consumption = {int(gamma,
    # 2) * int(epsilon, 2)}')
    return int(gamma, 2) * int(epsilon, 2)


def get_num(input_list, type_of_gas):
    input_list_copy = input_list.copy()

    for i in range(0, len(input_list[0])):
        one, zero = (0, 0)
        bit_positions = [row[i] for row in input_list_copy]
        one = bit_positions.count('1')
        zero = bit_positions.count('0')

        if type_of_gas == 'o2':
            if one >= zero:
                bit = '1'
            else:
                bit = '0'
        else:
            if one >= zero:
                bit = '0'
            else:
                bit = '1'
        req_numbers = [row for row in input_list_copy if row[i] == bit]

        if len(req_numbers) == 1:  # Keep going until we have one
            # print(f'{type_of_gas} = {int(req_numbers[0], 2)}')
            return int(req_numbers[0], 2)
        else:
            input_list_copy = req_numbers


if __name__ == '__main__':
    print(f'Part 1: Power consumption: {get_power_consumption(get_list("day3_input.txt"))}')
    print(
        f'Part 2: Life support rating = {get_num(get_list("day3_input.txt"), "o2") * get_num(get_list("day3_input.txt"), "co2")}')

    # print(f'Part 2: Life Support Rating: {get_life_support_rating(get_list("day3_input.txt"))}')
