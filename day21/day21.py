import os
from itertools import product

from aocd import get_data
from dotenv import load_dotenv
from functools import lru_cache

from utils import generate_readme


def get_session() -> str:
    load_dotenv()
    return os.getenv('SESSION_COOKIE')


def get_input(day: int, year: int, data: str = None):
    if not data:
        player_starting_positions = [int(line.split()[-1]) for line in
                                     get_data(get_session(), day=day, year=year).splitlines()]
    else:
        player_starting_positions = [int(line.split()[-1]) for line in
                                     data.splitlines()]
    return player_starting_positions


def play(starting_position: int, steps_to_move: int) -> int:
    return (starting_position + steps_to_move - 1) % 10 + 1
    # move x steps and back around to 1 after 10


def play_deterministic_dice(player_starting_positions: list) -> int:
    scores = [0, 0]
    player = 0
    i = 1
    while all(score < 1000 for score in scores):
        i, player = compute(i, player, player_starting_positions, scores)
    current_player_score = scores[player]
    # current player is the loser as the winning player's score is updated last
    rolls = i - 1
    # number of times the die was rolled
    return int(current_player_score * rolls)


def compute(i, player, player_starting_positions, scores):
    rolled_value = get_rolled_value(i)
    i += 3
    player_starting_positions[player] = play(player_starting_positions[player], rolled_value)
    scores[player] += player_starting_positions[player]
    # After each player moves, they increase their score by the value of the space their pawn stopped on.
    # print(f'Score of player {player}: {scores[player]}')
    player = 1 - player  # player is 0 or 1
    return i, player


def get_rolled_value(i):
    return 3 * i + 3


@lru_cache(maxsize=None)
# this stuff makes recursions run super-fast
def play_dirac_dice(p1_pos: int, p2_pos: int, p1_score: int = None, p2_score: int = None) -> tuple:
    p1_wins = 0
    p2_wins = 0
    if p2_score < 21 and p1_score < 21:
        for throws in product((1, 2, 3), repeat=3):
            # universe splits into 27 universes on each throw
            position = play(p1_pos, sum(throws))
            score = p1_score + position
            # After each player moves, they increase their score by
            # the value of the space their pawn stopped on.
            wins2, wins1 = play_dirac_dice(p1_pos=p2_pos,
                                           p2_pos=position,
                                           p1_score=p2_score,
                                           p2_score=score)
            # Neat trick of switching inputs around and play dirac.
            # thanks to StackOverflow !!
            p1_wins += wins1
            p2_wins += wins2
        return p1_wins, p2_wins

    return 0, 1


def part2(wins: tuple) -> int:
    # print(f'Wins: {wins}')
    return int(max(wins))


if __name__ == '__main__':
    print(f'Part 1: {play_deterministic_dice(get_input(day=21, year=2021))}')
    p1, p2 = get_input(day=21, year=2021)
    print(f'Part 2: {part2(play_dirac_dice(p1, p2, 0, 0))}')
    generate_readme("README", '2021', '21', '../')
