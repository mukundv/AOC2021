import cProfile
import io
import pstats
from datetime import datetime
from functools import wraps
from time import time

import requests
import snakemd
from bs4 import BeautifulSoup


# from https://towardsdatascience.com/bite-sized-python-recipes-52cde45f1489

def timeit(func):
    """
    :param func: Decorated function
    :return: Execution time for the decorated function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Timeit: {func.__name__} executed in {end - start:.6f} seconds')
        return result

    return wrapper


def profile(func):
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sort_by = pstats.SortKey.CUMULATIVE  # 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sort_by)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return wrapper


## Markdown generator

def fetch_puzzle_name(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}"
    return \
        BeautifulSoup(requests.get(url).text.strip(), "html.parser").article.contents[0].contents[0].strip().split(':')[
            1].strip()[:-4]


def get_table_body(year, upto):
    base_url = "https://github.com/mukundv/AOC2021/"
    body = []
    for i in range(1, int(upto) + 1):
        puzzle = snakemd.InlineText(fetch_puzzle_name(year, i), url=f"{base_url}blob/master/day{i}/day{i}/day{i}.md")
        aoc_input = snakemd.InlineText(f"day{i}.md", url=f"{base_url}blob/master/day{i}/day{i}/day{i}_input.txt")
        solution = snakemd.InlineText(f"day{i}.py", url=f"{base_url}blob/master/day{i}/day{i}/day{i}.py")
        if int(upto) <= 9:
            tag = snakemd.InlineText(f"day0{i}", url=f"{base_url}releases/tag/day0{i}")
        else:
            tag = snakemd.InlineText(f"day{i}", url=f"{base_url}releases/tag/day{i}")
        body.append([puzzle, aoc_input, solution, tag])
    return body


def generate_readme(name, year, day):
    readme = snakemd.Document(name)
    readme.add_header("AOC 2021")
    readme.add_paragraph("Fun with Python :snake: - aoc 2021") \
        .insert_link("aoc 2021", "https://adventofcode.com/2021/")
    header = ["Day", "PuzzleInput", "Solution", "Tag"]
    readme.add_element(snakemd.Table(header=header, body=get_table_body(year, day)))
    now = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
    readme.add_paragraph(f"This document was automatically rendered on {now}")
    readme.output_page()


if __name__ == '__main__':
    generate_readme("README", '2021', '7')
