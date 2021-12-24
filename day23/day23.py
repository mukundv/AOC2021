import os
import typing
from functools import lru_cache

from aocd import get_data, submit
from dotenv import load_dotenv

from utils import generate_readme, profile


def get_session() -> str:
    load_dotenv()
    return os.getenv('SESSION_COOKIE')


type_cost = {'A': 1,
             'B': 10,
             'C': 100,
             'D': 1000
             }

rooms = {'A': 3,
         'B': 5,
         'C': 7,
         'D': 9
         }

cache = {}


def run(day: int, year: int, data: str = None, part: int = None):
    if not data:
        if part == 1:
            return part1(get_data(get_session(), day=day, year=year).splitlines())
        else:
            return part2(get_data(get_session(), day=day, year=year).splitlines())
    else:
        if part == 1:
            return part1(data.splitlines())
        else:
            return part2(data.splitlines())


def get_lines(data: list) -> typing.Tuple:
    lines = (*((*line,) for line in data),)
    return lines


@profile
def part1(data: list) -> int:
    return int(check_state(get_lines(data)))


@profile
def part2(data: list) -> int:
    return int(check_state(extend(get_lines(data))))


def extend(data):
    return *data[:3], (*"  #D#C#B#A#",), (*"  #D#B#A#C#",), *data[3:],


def room_size(data):
    return int(len(data) - 3)


@lru_cache(maxsize=None)
def get_field(data, x, y):
    return data[y][x]


@lru_cache(maxsize=None)
def stoppable(data):
    return tuple(i for i in range(1, len(data[0]) - 1) if i not in rooms.values())


def is_in_own_room(data, x, y):
    if not is_amphipod(data, x, y):
        return False
    if x == rooms[get_field(data, x, y)]:
        return True
    return False


def is_in_any_room(data, x, y):
    return y > 1


def is_room_complete(data, x):
    for y in range(2, 2 + room_size(data)):
        if not is_in_own_room(data, x, y):
            return False
    return True


def are_rooms_complete(data):
    return is_room_complete(data, 3) and is_room_complete(data, 5) and is_room_complete(data, 7) and is_room_complete(
        data, 9)


def is_amphipod(data, x, y):
    val = get_field(data, x, y)
    return val if val in rooms.keys() else False


def is_empty(data, x, y):
    return get_field(data, x, y) == '.'


def is_room_empty(data, x):
    for y in range(2, 2 + room_size(data)):
        if not is_empty(data, x, y):
            return False
    return True


def is_blocking_room(data, x, y):
    for j in range(y + 1, 2 + room_size(data)):
        if is_amphipod(data, x, j) and not is_in_own_room(data, x, j):
            return True
    return False


def has_room_available(data, x, y):
    amphipod = get_field(data, x, y)
    room = rooms[amphipod]
    if is_room_empty(data, room): return True
    for y in range(2, 2 + room_size(data)):
        if not is_empty(data, room, y) and not is_in_own_room(data, room, y):
            return False
    return True


def is_path_empty(data, x, target_x):
    while x != target_x:
        if x > target_x:
            x -= 1
        if x < target_x:
            x += 1
        if not is_empty(data, x, 1):
            return False
    return True


def is_blocked_in_room(data, x, y):
    if y < 3: return False
    return not is_empty(data, x, y - 1)


def move_in_pos(data, room):
    for y in range(1 + room_size(data), 1, -1):
        if is_empty(data, room, y):
            return y


def can_move(data, x, y):
    return (not is_in_own_room(data, x, y) or is_blocking_room(data, x, y)) and not is_blocked_in_room(data, x, y)


def get_move_cost(data, x, y, i, j):
    return ((y - 1) + abs(x - i) + (j - 1)) * type_cost[get_field(data, x, y)]


def do_move(d, x, y, i, j):
    new_data = (
        *(
            (
                *(((get_field(d, a, b), get_field(d, x, y))[a == i and b == j], get_field(d, i, j))[a == x and b == y]
                  for a
                  in
                  range(len(d[b]))),) for b in range(len(d))),)
    return new_data, get_move_cost(d, x, y, i, j)


@lru_cache(maxsize=None)
def check_state(data):
    cached = cache.get(data)
    if cached is not None:
        return cached
    if are_rooms_complete(data):
        return 0
    costs = []
    for y in range(1, len(data)):
        for x in range(1, len(data[y])):
            amphipod = is_amphipod(data, x, y)
            if not amphipod:
                continue
            if can_move(data, x, y):
                room = rooms[amphipod]
                if has_room_available(data, x, y) and is_path_empty(data, x, room):
                    d, c = do_move(data, x, y, room, move_in_pos(data, room))
                    cost = check_state(d)
                    if cost >= 0:
                        costs.append(c + cost)
                elif is_in_any_room(data, x, y):
                    for i in stoppable(data):
                        if not is_path_empty(data, x, i):
                            continue
                        d, c = do_move(data, x, y, i, 1)
                        cost = check_state(d)
                        if cost >= 0:
                            costs.append(c + cost)
    result = -1
    if costs:
        result = min(costs)
    cache[data] = result
    return result


def submit_answer(a_1, a_2):
    submit(answer=a_1, session=get_session(), part='a', day=23, year=2021)
    submit(answer=a_2, session=get_session(), part='b', day=23, year=2021)


if __name__ == '__main__':
    submit_answer(run(data=None, day=23, year=2021, part=1), run(data=None, day=23, year=2021, part=2))
    generate_readme("README", '2021', '23', '../')
