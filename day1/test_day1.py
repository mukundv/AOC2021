import os

from .day1 import compare_list, sliding_window, get_list

data = open(os.getcwd() + '\\day1\\day1_example.txt').read()


class TestDay1:

    def test_part1_example(self):
        assert compare_list(get_list(data=data, day=1, year=2021)) == 7

    def test_part2_example(self):
        assert compare_list(sliding_window(get_list(data=data, day=1, year=2021))) == 5

    def test_part1(self):
        assert compare_list(get_list(data=None, day=1, year=2021)) == 1374

    def test_part2(self):
        assert compare_list(sliding_window(get_list(data=None, day=1, year=2021))) == 1418
