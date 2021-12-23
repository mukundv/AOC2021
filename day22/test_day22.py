import os

from .day22 import run

data1 = open(os.getcwd() + '//day22//day22_example1.txt').read()
data2 = open(os.getcwd() + '//day22//day22_example2.txt').read()
data3 = open(os.getcwd() + '//day22//day22_example3.txt').read()


class TestDay22:

    def test_part1_example_1(self):
        ans = run(data=data1, day=22, year=2021, part=1)
        assert ans == 39

    def test_part1_example_2(self):
        ans = run(data=data2, day=22, year=2021, part=1)
        assert ans == 590784

    def test_part2_example_1(self):
        ans = run(data=data3, day=22, year=2021, part=2)
        assert ans == 2758514936282235

    def test_part1(self):
        ans = run(data=None, day=22, year=2021, part=1)
        assert ans == 583636

    def test_part2(self):
        ans = run(data=None, day=22, year=2021, part=2)
        assert ans == 1294137045134837
