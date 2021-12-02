def get_list(input_file_name):
    aoc_input = []
    with open(input_file_name, "r") as f:
        aoc_input = [line.rstrip() for line in f]
    return aoc_input


# Part 1
def compare_list(input_list):
    horizontal_position, depth = 0, 0
    for input_line in input_list:
        direction, number = input_line.strip().split()
        number = int(number)
        if direction == 'forward':  # Add number to horizontal position
            horizontal_position += number
        elif direction == 'up':  # Subtract number from depth
            depth -= number
        elif direction == 'down':  # Add number to depth
            depth += number
        else:
            print(f"{direction} is unknown")
    print(f'Final is {horizontal_position} * {depth} = {horizontal_position * depth}')
    return horizontal_position * depth


# Part 2

def get_aim(input_list):
    horizontal_position, depth, aim = 0, 0, 0
    for input_line in input_list:
        direction, number = input_line.strip().split()
        number = int(number)
        if direction == 'forward':
            horizontal_position += number  # Add number to horizontal position
            depth += aim * number  # Increase depth by aim * number
        elif direction == 'up':
            aim -= number  # Decrease aim by number
        elif direction == 'down':
            aim += number  # Increase aim by number
        else:
            print(f"{direction} is unknown")
    print(f'Final is {horizontal_position} * {depth} = {horizontal_position * depth}')
    return horizontal_position * depth


if __name__ == '__main__':
    print(f'Part 1: Horizontal Position * depth = {compare_list(get_list("day2_input.txt"))}')
    print(f'Part 2: Horizontal Position * depth = {get_aim(get_list("day2_input.txt"))}')
