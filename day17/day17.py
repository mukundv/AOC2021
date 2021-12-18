from typing import Tuple, Union, Any
from utils import generate_readme


def get_input(input_file_name: str) -> tuple[int, int, int, int]:
    with open(input_file_name) as f:
        line = f.readline()[13:]
        line = line.split(",")
        r1, r2 = line[0].replace("x=", "").split("..")
        c1, c2 = line[1].replace("y=", "").split("..")
        return int(r1), int(r2), int(c1), int(c2)


def walk(vel_x: int, vel_y: int, x: int, y: int) -> tuple[int, int, int, int]:
    x += vel_x
    y += vel_y
    if vel_x > 0:
        vel_x -= 1
    elif vel_x < 0:
        vel_x += 1
    vel_y -= 1
    return vel_x, vel_y, x, y


def trick_shot(x1: int, x2: int, y1: int, y2: int) -> tuple[Union[int, Any], int]:
    print(f'Input: x1:{x1},x2:{x2},y1:{y1},y2:{y2}')
    total = 0
    best_y = 0
    for i in range(0, x2 + 1):
        for j in range(y1, 1000):
            x, y, max_y = 0, 0, 0
            vel_x = i
            vel_y = j
            while x <= x2 and y >= y1:
                vel_x, vel_y, x, y = walk(vel_x, vel_y, x, y)
                if y > max_y:
                    max_y = y
                if x1 <= x <= x2 and y1 <= y <= y2:
                    total += 1
                    if max_y > best_y:
                        best_y = max_y
                    break
                if vel_x == 0 and x < x1:
                    break
    return best_y, total


if __name__ == '__main__':
    x1, x2, y1, y2 = get_input("day17_input.txt")
    answer = trick_shot(x1, x2, y1, y2)
    print(f'Part 1: {answer[0]}')
    print(f'Part 2: {answer[1]}')
    generate_readme("README", '2021', '17', '../')
