import os
from typing import Any, Tuple

import numpy as np
from aocd import get_data
from dotenv import load_dotenv
from numpy import ndarray

from utils import timeit, generate_readme


def get_session() -> str:
    load_dotenv()
    return os.getenv('SESSION_COOKIE')


def get_inputs(day: int, year: int, data: str = None) -> Tuple[ndarray, ndarray]:
    if data is None:
        data = get_data(get_session(), day=day, year=year)
    data = data.replace("#", "1").replace(".", "0")
    algorithm, input_image = data.split('\n\n')
    algorithm: ndarray = np.array([int(i) for i in algorithm])
    input_img: ndarray = np.array([[int(i) for i in line] for line in input_image.split('\n')])
    return algorithm, input_img


def enhance_image(algo: ndarray, img: ndarray, fill_value: int = 0, times: int = 2) -> ndarray:
    for _ in range(times):
        # Apply the algo 2 times for part 1 and 50 times for part 2
        stride, stride_cols, stride_rows = get_stride(fill_value, img)
        codes = get_codes(stride, stride_cols, stride_rows)
        img: ndarray = algo[codes]
        fill_value = algo[fill_value * 511]
    return img


def get_stride(fill_value: int, img: ndarray) -> tuple[ndarray, int, int]:
    # The strides of an array tell us how many bytes we have to skip in memory to move to the next position along a
    # certain axis.
    img = np.pad(img, 2, constant_values=fill_value)
    r, c = img.shape
    stride_rows: int = r - 2
    stride_cols: int = c - 2
    stride_shape = stride_rows, stride_cols, 3, 3
    stride = np.lib.stride_tricks.as_strided(img, stride_shape, 2 * img.strides)
    stride: ndarray = np.reshape(stride, (stride_rows, stride_cols, 9))
    return stride, stride_cols, stride_rows


def get_codes(stride, stride_cols, stride_rows):
    codes: int | Any = stride[:, :, 0] * 256 + np.packbits(stride[:, :, 1:]).reshape(stride_rows, stride_cols)
    return codes


@timeit
def part1(algo, img):
    return np.sum(enhance_image(algo=algo, img=img, times=2))


@timeit
def part2(algo, img):
    return np.sum(enhance_image(algo=algo, img=img, times=50))


if __name__ == '__main__':
    print(f'Part 1: {part1(*get_inputs(day=20, year=2021))}')
    print(f'Part 2: {part2(*get_inputs(day=20, year=2021))}')
    generate_readme("README", '2021', '20', '../')
