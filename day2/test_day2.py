import os

from .day2 import compare_list, get_aim, get_list

data = open(os.getcwd() + '\\day2\\day2_example.txt').read()


class TestDay1:

    def test_part1_example(self):
        assert compare_list(get_list(data=data, day=2, year=2021)) == 150

    def test_part2_example(self):
        assert get_aim(get_list(data=data, day=2, year=2021)) == 900

    def test_part1(self):
        assert compare_list(get_list(data=None, day=2, year=2021)) == 1746616

    def test_part2(self):
        assert get_aim(get_list(data=None, day=2, year=2021)) == 1741971043
