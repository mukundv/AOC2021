import itertools as it
import os
from collections import Counter
from typing import Any

from aocd import get_data
from dotenv import load_dotenv

from utils import timeit, generate_readme


def get_session() -> str:
    load_dotenv()
    return os.getenv('SESSION_COOKIE')


def get_input(day: int, year: int) -> list[list[tuple[int, ...]]]:
    return get_scanners(get_data(session=get_session(), day=day, year=year))


def get_scanners(data: str) -> list[list[tuple[int, ...]]]:
    scanners: list[list[tuple[int, ...]]] = []
    current = None
    lines = data.splitlines()
    for line in lines:
        if line == "":
            continue
        elif line[0:3] == "---":
            current = []
            scanners.append(current)
        else:
            current.append(tuple(map(int, line.split(','))))
    return scanners


def align(aligned: list, candidate: list) -> tuple[list[tuple[Any, Any, Any]], list[Any]] | None:
    # global c
    return_list: list[list[Any]] = []
    dl = []
    dp = dpp = None
    i = []
    for _ in range(3):
        x = [position[_] for position in aligned]
        for (d, s) in [(0, 1), (1, 1), (2, 1), (0, -1), (1, -1), (2, -1)]:
            if d != dp and d != dpp:
                i = [pos[d] * s for pos in candidate]
                j = [b - a for (a, b) in it.product(x, i)]
                c: list[tuple[Any, int]] = Counter(j).most_common(1)
                if c[0][1] >= 12:
                    break
        if c[0][1] >= 12:
            (dpp, dp) = (dp, d)
            return_list.append([v - c[0][0] for v in i])
            dl.append(c[0][0])
            continue
        return None
    return list(zip(return_list[0], return_list[1], return_list[2])), dl


def run(scanners: list[list[tuple[int, ...]]]) -> tuple[int, list[tuple[int, int, int]]]:
    fin = set()
    next_scanner = [scanners[0]]
    remaining = scanners[1:]
    shifts = [(0, 0, 0)]
    while next_scanner:
        aligned: list[tuple[int, ...]] | list[tuple[Any, Any, Any]] = next_scanner.pop()
        temp = []
        process_candidate(aligned, next_scanner, remaining, shifts, temp)
        remaining = temp
        fin.update(aligned)
    return int(len(fin)), shifts


def process_candidate(aligned, next_scanner, remaining, shifts, temp):
    for candidate in remaining:
        r = align(aligned, candidate)
        if r:
            (updated, shift) = r
            shifts.append(shift)
            next_scanner.append(updated)
        else:
            temp.append(candidate)


@timeit
def part1(scanners: list[list[tuple[int, ...]]]) -> int:
    no_beacons = run(scanners)[0]
    return no_beacons


@timeit
def part2(scanners: list[list[tuple[int, ...]]]) -> int:
    x = run(scanners)[1]
    y = it.product(x, x)
    md = max(sum(abs(a - b) for (a, b) in zip(i, j)) for i, j in y)
    return int(md)


if __name__ == '__main__':
    print(f'Part 1: {part1(get_input(day=19, year=2021))}')
    print(f'Part 2: {part2(get_input(day=19, year=2021))}')
    generate_readme("README", '2021', '19', '../')
