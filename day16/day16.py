from math import prod

from utils import generate_readme


def get_input(input_file_name) -> str:
    return get_bin_from_hex(open(input_file_name).read().strip())


def get_bin_from_hex(s) -> str:
    return format(int("1" + s, 16), "0b")[1:]


def get_decoded_packet(s):
    version = get_version(s)
    type_id = get_type_id(s)
    if type_id == 4:
        return get_literal(s, type_id, version)
    if get_type_of_type_id(s):
        return process_sub_packets(s, type_id, version)
    else:
        n = get_number_of_sub_packets(s)
        sub_packets = s[18:]
        packets = []
        while n > 0:
            sv, st, sb, sub_packets = get_decoded_packet(sub_packets)
            packets.append((sv, st, sb))
            n -= 1
        return version, type_id, packets, sub_packets


def get_version(s: str) -> int:
    return int(s[:3], 2)


def get_type_id(s: str) -> int:
    return int(s[3:6], 2)


def get_type_of_type_id(s: str) -> bool:
    if s[6] == '0':
        return True
    else:
        return False


def get_number_of_sub_packets(s: str) -> int:
    return int(s[7:18], 2)


def get_sum_of_versions(packet: tuple) -> int:
    match packet:
        case int(v), 4, int(n):
            return v
        case int(v), int(_), list(sub):
            return v + sum(get_sum_of_versions(p) for p in sub)


def process_sub_packets(s, type_id, version):
    bits = get_bits(s)
    sub_packets = s[22: 22 + bits]
    packets = []
    while sub_packets:
        sv, st, sb, sub_packets = get_decoded_packet(sub_packets)
        packets.append((sv, st, sb))
    return version, type_id, packets, s[22 + bits:]


def get_bits(s: str) -> int:
    return int(s[7:22], 2)


def get_literal(s, type_id, version):
    n = 0
    pos = 6
    while s[pos] == "1":
        n = n * 16 + int(s[pos + 1: pos + 5], 2)
        pos += 5
    n = n * 16 + int(s[pos + 1: pos + 5], 2)
    return version, type_id, n, s[pos + 5:]


def calc(packet: tuple) -> int:
    # 0: Sum
    # 1: Product
    # 2: Minimum
    # 3: Maximum
    # 4: single number
    # 5: Greater Than
    # 6: Lesser Than
    # 7: Equal
    match packet:
        case v, 0, list(packets):
            return sum(calc(p) for p in packets)
        case v, 1, list(packets):
            return prod(calc(p) for p in packets)
        case v, 2, list(packets):
            return min(calc(p) for p in packets)
        case v, 3, list(packets):
            return max(calc(p) for p in packets)
        case v, 4, int(number):
            return number
        case v, 5, [tuple(a), tuple(b)]:
            return calc(a) > calc(a)
        case v, 6, [tuple(a), tuple(b)]:
            return calc(a) < calc(b)
        case v, 7, [tuple(a), tuple(b)]:
            return calc(a) == calc(b)


def part1(s: str) -> int:
    return int(get_sum_of_versions(get_decoded_packet(s)[:3]))


def part2(s: str) -> int:
    return int(calc(get_decoded_packet(s)[:3]))


if __name__ == '__main__':
    print(f'Part 1: {part1(get_input("day16_input.txt"))}')
    print(f'Part 2: {part2(get_input("day16_input.txt"))}')
    generate_readme("README", '2021', '16', '../')
