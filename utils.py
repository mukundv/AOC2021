import cProfile
import io
import os
import pstats
from datetime import datetime
from functools import wraps
from time import time

import requests
import snakemd
from bs4 import BeautifulSoup
from colorama import Fore, Style
from dotenv import load_dotenv


## Profiling functions

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


## Markdown generator functions

def fetch_puzzle_name(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}"
    return \
        BeautifulSoup(requests.get(url).text.strip(), "html.parser").article.contents[0].contents[0].strip().split(':')[
            1].strip()[:-4]


def get_table_body(year, upto):
    base_url = "https://github.com/mukundv/AOC2021/"
    body = []
    for i in range(1, int(upto) + 1):
        puzzle = snakemd.InlineText(fetch_puzzle_name(year, i), url=f"{base_url}blob/master/day{i}/day{i}.md")
        aoc_input = snakemd.InlineText(f"day{i}_input.txt", url=f"{base_url}blob/master/day{i}/day{i}_input.txt")
        solution = snakemd.InlineText(f"day{i}.py", url=f"{base_url}blob/master/day{i}/day{i}.py")
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


## AOC UTILS
# modified from https://github.com/loganmeetsworld/advent-of-code-utils

load_dotenv()
CURRENT_DIR = os.getcwd()
SESSION_COOKIE = os.getenv('SESSION_COOKIE')
HEADERS = {"cookie": f"session={SESSION_COOKIE}", }


def request_content(year, day, content_type):
    url = ""
    if content_type == 'input':
        url = f"https://adventofcode.com/{year}/day/{day}/input"
    elif content_type == 'problem':
        url = f"https://adventofcode.com/{year}/day/{day}"

    response = requests.get(url, headers=HEADERS)
    handle_error_status(response.status_code)
    return response.text.strip()


def fetch(year, day, content_type):
    content = request_content(year, day, content_type)
    if content_type == 'input':
        return content
    elif content_type == 'problem':
        soup = BeautifulSoup(content, "html.parser")
        return '\n\n\n'.join([a.text for a in soup.select('article')])


def save(year, day, content_type):
    content = fetch(year, day, content_type)
    if content_type == "input":
        with open(f"{CURRENT_DIR}/day{day}_{content_type}.txt", "w") as text_file:
            text_file.write(content)
    elif content_type == "problem":
        with open(f"{CURRENT_DIR}/day{day}.md", "w") as text_file:
            text_file.write(content)
    return content


def fetch_and_save(year, day):
    if os.path.exists(f"{CURRENT_DIR}/day{day}_input.txt"):
        print("\n🛷  Found input locally, using saved input 🛷 \n")
        with open(f"{CURRENT_DIR}/day{day}_input.txt") as file:
            return file.read()
    else:
        print("\n🛷  Input not found, fetching 🛷 \n")
        problem_text = save(year, day, content_type="problem")
        print(f"\n{problem_text}\n")
        return save(year, day, content_type="input")


def submit(answer, level, year, day):
    print(f"\nFor Day {day}, Part {level}, we are submitting answer: {answer}\n")
    data = {"level": str(level), "answer": str(answer)}
    response = requests.post(f"https://adventofcode.com/{year}/day/{day}/answer", headers=HEADERS, data=data)
    soup = BeautifulSoup(response.text, "html.parser")
    message = soup.article.text

    if "that's the right answer" in message.lower():
        print(f"\n{Fore.GREEN}Correct! ⭐️{Style.RESET_ALL}")
        star_path = os.getcwd()
        with open(f"{star_path}/stars.txt", "w+") as text_file:
            print("Writing '*' to star file...")
            if level == 1:
                text_file.write('*')
            elif level == 2:
                text_file.write('**')

        if level == 1:
            print("Updated problem with part 2:\n\n")
            print(save(year, day, 'problem'))
    elif "not the right answer" in message.lower():
        print(f"\n{Fore.RED}Wrong answer 🎅🏾🙅🏼‍♀️! For details:\n{Style.RESET_ALL}")
        print(message)
    elif "answer too recently" in message.lower():
        print(f"\n{Fore.YELLOW}You gave an answer too recently{Style.RESET_ALL}")
    elif "already complete it" in message.lower():
        print(
            f"\n{Fore.YELLOW}You have already solved this. Make sure a local stars.txt file is present that reflects "
            f"your stars for this problem.{Style.RESET_ALL}")


def test(answer_func, cases):
    all_passed = True

    if not cases:
        print("Livin' on the edge! No test cases defined.")
        return all_passed

    for tc in cases:
        answer = answer_func(tc['input'], tc['level'], test=True)
        if str(tc['output']) == str(answer):
            print(
                f"{Fore.GREEN}🎄 Test passed {Style.RESET_ALL}[Part {tc['level']}] Input: '{tc['input']}'; Output: '{tc['output']}'")
        else:
            all_passed = False
            print(
                f"{Fore.RED}🔥 Test failed {Style.RESET_ALL}[Part {tc['level']}] Input: '{tc['input']}'; Submitted: '{answer}'; Correct: '{tc['output']}'")

    return all_passed


def check_stars():
    star_path = os.getcwd()
    star_file = f"{star_path}/stars.txt"
    if os.path.exists(star_file):
        with open(star_file, 'r') as file:
            stars = file.read().strip()
            return len(stars)


def handle_error_status(code):
    if code == 404:
        print(f"{Fore.RED}{code}: This day is not available yet!{Style.RESET_ALL}")
        quit()
    elif code == 400:
        print(f"{Fore.RED}{code}: Bad credentials!{Style.RESET_ALL}")
        quit()
    elif code > 400:
        print(f"{Fore.RED}{code}: General error!{Style.RESET_ALL}")
        quit()


def run(answer_func, test_cases=None, year=None, day=None):
    if not year and not day:
        year, day = CURRENT_DIR.split('/')[-2:]

    problem_input = fetch_and_save(year, day)

    if test(answer_func, test_cases):
        print("\n🍾 Now looking to submit your answers 🍾\n")
        stars = check_stars()
        if not stars:
            level = 1
            answer = answer_func(problem_input, level)
            print(
                f"🙇‍♀️ You are submitting your answer to part 1 of this puzzle. \nDo you want to submit part 1 ("
                f"y/n)? P1: {answer}")
            submit_answer = input()
            if submit_answer == 'y':
                submit(answer, level, year, day)
        elif stars == 1:
            level = 2
            answer = answer_func(problem_input, level)
            print(
                f"👯‍♀️  It seems we've been here before and you've submitted one answer ⭐️ \nDo you want to submit "
                f"part 2 (y/n)? P2: {answer}")
            submit_answer = input()
            if submit_answer == 'y':
                submit(answer, level, year, day)
        else:
            print("It seems we've been here before and you've submitted both answers! ⭐️⭐️\n")
    else:
        print("\n🤷‍♀️ You know the rules. Tests don't pass, YOU don't pass.\n")

# if __name__ == '__main__':
# request_content('2021','7','problem')
# generate_readme("README", '2021', '7')
