import os

from .day21 import play_deterministic_dice, play_dirac_dice, get_input, part2

data = open(os.getcwd() + '//day21//day21_example.txt').read()


class TestDay21:

    def test_part1_example(self):
        ans = play_deterministic_dice(get_input(data=data, day=21, year=2021))
        assert ans == 739785

    def test_part2_example(self):
        p1, p2 = get_input(data=data, day=21, year=2021)
        ans = part2(play_dirac_dice(p1, p2, 0, 0))
        assert ans == 444356092776315

    def test_part1(self):
        ans = play_deterministic_dice(get_input(data=None, day=21, year=2021))
        assert ans == 734820

    def test_part2(self):
        p1, p2 = get_input(data=None, day=21, year=2021)
        ans = part2(play_dirac_dice(p1, p2, 0, 0))
        assert ans == 193170338541590
