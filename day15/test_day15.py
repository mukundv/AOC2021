import os
from unittest import TestCase

from .day15 import dijkstra, get_input, get_bigger_matrix


class TestDay15(TestCase):
    def setUp(self):
        file = os.getcwd() + "\day15\day15_example.txt"
        return file

    def test_part1_example(self):
        answer = dijkstra(get_input(self.setUp()))
        self.assertEqual(answer, 40)

    def test_part2_example(self):
        file = self.setUp().replace('example', 'part2_example')
        answer = dijkstra(get_input(file))
        self.assertEqual(answer, 315)

    def test_part1_input(self):
        file = self.setUp().replace('example', 'input')
        answer = dijkstra(get_input(file))
        self.assertEqual(answer, 748)

    def test_part2_input(self):
        file = self.setUp().replace('example', 'input')
        answer = dijkstra(get_bigger_matrix(get_input(file)))
        self.assertEqual(answer, 3045)
