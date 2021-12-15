import os
from unittest import TestCase

from .day14 import part1, part2, get_inputs


class TestDay14(TestCase):
    def setUp(self):
        file = os.getcwd() + "\day14\day14_example.txt"
        return file

    def test_part1_example(self):
        answer = part1(get_inputs(self.setUp()))
        self.assertEqual(answer, 1588)

    def test_part2_example(self):
        answer = part2(get_inputs(self.setUp()))
        self.assertEqual(answer, 2188189693529)

    def test_part1_input(self):
        file = self.setUp().replace('example', 'input')
        answer = part1(get_inputs(file))
        self.assertEqual(answer, 3058)

    def test_part2_input(self):
        file = self.setUp().replace('example', 'input')
        answer = part2(get_inputs(file))
        self.assertEqual(answer, 3447389044530)
