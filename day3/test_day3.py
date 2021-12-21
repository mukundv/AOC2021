import os

from .day3 import get_power_consumption, get_num, get_list

data = open(os.getcwd() + '\\day3\\day3_example.txt').read()


class TestDay3:

    def test_part1_example(self):
        assert get_power_consumption(get_list(data=data, day=3, year=2021)) == 198

    def test_part2_example(self):
        assert get_num(get_list(data=data, day=3, year=2021), "o2") * \
               get_num(get_list(data=data, day=3, year=2021), "co2") == 230

    def test_part1(self):
        assert get_power_consumption(get_list(data=None, day=3, year=2021)) == 841526

    def test_part2(self):
        assert get_num(get_list(data=None, day=3, year=2021), "o2") * \
               get_num(get_list(data=None, day=3, year=2021), "co2") == 4790390
