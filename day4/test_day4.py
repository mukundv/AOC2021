import os

from .day4 import get_lists, get_winning_number, get_last_winning_board_score

data = open(os.getcwd() + '\\day4\\day4_example.txt').read()


class TestDay4:
    def test_part1_example(self):
        assert get_winning_number(*get_lists(data=data, day=4, year=2021)) == 4512

    def test_part2_example(self):
        assert get_last_winning_board_score(*get_lists(data=data, day=4, year=2021)) == 1924

    def test_part1(self):
        assert get_winning_number(*get_lists(data=None, day=4, year=2021)) == 60368

    def test_part2(self):
        assert get_last_winning_board_score(*get_lists(data=None, day=4, year=2021)) == 17435
