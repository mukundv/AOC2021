from aocd import get_data


def get_input(input_file_name):
    data = get_data(day=19, year=2021)
    with open(input_file_name) as f:
        return f.readlines()


if __name__ == '__main__':
    print(get_input("day19_input.txt"))
