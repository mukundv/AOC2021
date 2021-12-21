import os

from .day20 import part1, part2, get_inputs

data = open(os.getcwd() + '\\day20\\day20_example.txt').read()


class TestDay20:
    def test_part1_example(self):
        assert part1(*get_inputs(data=data, day=20, year=2021)) == 35

    def test_part2_example(self):
        assert part2(*get_inputs(data=data, day=20, year=2021)) == 3351
