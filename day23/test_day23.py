import os

from .day23 import run

data = open(os.getcwd() + '//day23//day23_example.txt').read()


class TestDay23:

    def test_part1_example(self):
        assert run(data=data, day=23, year=2021, part=1) == 12521

    def test_part2_example(self):
        assert run(data=data, day=23, year=2021, part=2) == 44169

    def test_part1(self):
        assert run(data=None, day=23, year=2021, part=1) == 11536

    def test_part2(self):
        assert run(data=None, day=23, year=2021, part=2) == 55136
