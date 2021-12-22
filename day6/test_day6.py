import os

from .day6 import part1, part2, get_list

data = open(os.getcwd() + '\\day6\\day6_example.txt').read()


class TestDay6:
    def test_part1_example(self):
        assert part1(get_list(data=data, day=6, year=2021), 80) == 5934

    def test_part2_example(self):
        assert part2(get_list(data=data, day=6, year=2021), 256) == 26984457539

    def test_part1(self):
        assert part1(get_list(data=None, day=6, year=2021), 80) == 391671

    def test_part2(self):
        assert part2(get_list(data=None, day=6, year=2021), 256) == 1754000560399
