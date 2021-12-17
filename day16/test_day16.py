import os
from unittest import TestCase

from .day16 import part1, part2, get_bin_from_hex


class TestDay16(TestCase):
    def setUp(self):
        file = os.getcwd() + "\day16\day16_input.txt"
        return file

    def test_case_1(self):
        answer = part1(get_bin_from_hex("8A004A801A8002F478"))
        self.assertEqual(answer, 16)

    def test_case_2(self):
        answer = part1(get_bin_from_hex("620080001611562C8802118E34"))
        self.assertEqual(answer, 12)

    def test_case_3(self):
        answer = part1(get_bin_from_hex("C0015000016115A2E0802F182340"))
        self.assertEqual(answer, 23)

    def test_case_4(self):
        answer = part1(get_bin_from_hex("A0016C880162017C3686B18A3D4780"))
        self.assertEqual(answer, 31)

    def test_case_5(self):
        answer = part2(get_bin_from_hex("C200B40A82"))
        self.assertEqual(answer, 3)

    def test_case_6(self):
        answer = part2(get_bin_from_hex("04005AC33890"))
        self.assertEqual(answer, 54)

    def test_case_7(self):
        answer = part2(get_bin_from_hex("880086C3E88112"))
        self.assertEqual(answer, 7)

    def test_case_8(self):
        answer = part2(get_bin_from_hex("CE00C43D881120"))
        self.assertEqual(answer, 9)

    def test_case_9(self):
        answer = part2(get_bin_from_hex("D8005AC2A8F0"))
        self.assertEqual(answer, 1)

    def test_case_10(self):
        answer = part2(get_bin_from_hex("F600BC2D8F"))
        self.assertEqual(answer, 0)

    def test_case_11(self):
        answer = part2(get_bin_from_hex("9C005AC2F8F0"))
        self.assertEqual(answer, 0)

    def test_case_12(self):
        answer = part2(get_bin_from_hex("9C0141080250320F1802104A08"))
        self.assertEqual(answer, 1)
