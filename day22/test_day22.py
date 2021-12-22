import os

from .day22 import part1, get_input

data1 = open(os.getcwd() + '//day22//day22_example1.txt').read()
data2 = open(os.getcwd() + '//day22//day22_example2.txt').read()
data3 = open(os.getcwd() + '//day22//day22_example2.txt').read()


class TestDay22:

    def test_part1_example_1(self):
        ans = part1(*get_input(data=data1, day=21, year=2021))
        assert ans == 39

    def test_part1_example_2(self):
        ans = part1(*get_input(data=data2, day=21, year=2021))
        assert ans == 590784

    # def test_part1_example_3(self):
    #     ans = part1(*get_input(data=data3, day=21, year=2021))
    #     assert ans == 2758514936282235
    # def test_part2_example(self):
    #     p1, p2 = get_input(data=data, day=21, year=2021)
    #     ans = part2(play_dirac_dice(p1, p2, 0, 0))
    #     assert ans == 444356092776315
    #
    # def test_part1(self):
    #     ans = play_deterministic_dice(get_input(data=None, day=21, year=2021))
    #     assert ans == 734820
    #
    # def test_part2(self):
    #     p1, p2 = get_input(data=None, day=21, year=2021)
    #     ans = part2(play_dirac_dice(p1, p2, 0, 0))
    #     assert ans == 193170338541590
