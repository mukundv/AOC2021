import math
import re
from typing import Union

from utils import generate_readme


class SnailNumbers():
    def __init__(self, number: str):
        self.number = number

    def __add__(self, other: Union[str, 'SnailNumbers']):
        if not isinstance(other, SnailNumbers):
            return SnailNumbers(f'[{self.number},{other}]')
        return SnailNumbers(f'[{self.number},{other.number}]')

    def __str__(self):
        return self.number

    def __repr__(self):
        return f'sailfish_number: {self}'

    @property
    def find_next_explosion(self):
        open_bracket_count = 0
        for ix, letter in enumerate(self.number):
            if letter == '[':
                open_bracket_count += 1
            elif letter == ']':
                open_bracket_count -= 1
            if open_bracket_count == 5:
                exploding_pair = re.search(r'\[\d+,\d+]', self.number[ix:]).group()
                return ix, exploding_pair
        return None, None

    @staticmethod
    def split_number(match):
        number = int(match.group())
        if number > 9:
            number_by_two = int(number) / 2
            return f'[{math.floor(number_by_two)},{math.ceil(number_by_two)}]'
        return str(number)

    @staticmethod
    def magnitude_of_pair(match):
        x, y = re.findall(r'\d+', match.group())
        return str(int(x) * 3 + int(y) * 2)

    @property
    def explode(self):
        ix, pair = self.find_next_explosion
        if not pair:
            return False
        (prev, following) = get_number_from_pair(pair)
        number_prev = self.number[:ix]
        number_following = self.number[ix + len(pair):]
        number_prev = re.sub(r'(.*\D)(\d+)',
                             lambda m: m.group(1) + str(int(m.group(2)) + prev), number_prev, count=1)
        number_following = re.sub(r'\d+',
                                  lambda m: str(int(m.group()) + following), number_following, count=1)
        new_number = number_prev + '0' + number_following
        changed = new_number != self.number
        self.number = new_number
        return changed

    @property
    def split(self):
        new_number = re.sub(r"[1-9]\d+", self.split_number, self.number, count=1)
        changed = new_number != self.number
        self.number = new_number
        return changed

    def reduce(self):
        while self.explode or self.split:
            pass

    @property
    def magnitude(self):
        new_number = self.number
        while True:
            new_number = re.sub(r"\[\d+,\d+]", self.magnitude_of_pair, new_number)
            # break if all chars are numbers
            if re.search(r"^\d+$", new_number):
                break
        return new_number


def get_number_from_pair(pair: str) -> tuple:
    return tuple(int(x) for x in re.findall(r"\d+", pair))


def get_input(input_file_name):
    with open(input_file_name, 'r') as f:
        numbers_to_add = f.read().strip().split()
    return numbers_to_add


def part1(numbers):
    snail_number = SnailNumbers(numbers[0])
    for number in numbers[1:]:
        snail_number += number
        snail_number.reduce()
    return snail_number.magnitude


def part2(numbers):
    max_magnitude = 0
    for left in numbers:
        for right in numbers:
            x = SnailNumbers(left) + right
            x.reduce()
            max_magnitude = max(max_magnitude, int(x.magnitude))
    return max_magnitude


if __name__ == '__main__':
    print(f'Part 1: {part1(get_input("day18_input.txt"))}')
    print(f'Part 2: {part2(get_input("day18_input.txt"))}')
    generate_readme("README", '2021', '18', '../')