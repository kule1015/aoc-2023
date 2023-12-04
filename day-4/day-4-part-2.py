import re
from collections import defaultdict

import numpy as np


def _read_file(filename: str) -> [str]:
    with open(filename) as file:
        return [line.rstrip() for line in file]


def _process_games(file_name: str) -> [int, int]:
    card_win_per_game: dict[int, int] = defaultdict(int)

    for index, line in enumerate(_read_file(file_name)):
        number_of_wins: int = _calculate_game_score(line)
        card_win_per_game[index] += 1
        for index_further_wins in range(index + 1, index + number_of_wins + 1):
            card_win_per_game[index_further_wins] += card_win_per_game[index]

    return card_win_per_game


def _calculate_game_score(game: str) -> int:
    winning_numbers, my_numbers = _parse_winning_and_your_numbers(game)
    return len(np.intersect1d(np.array(winning_numbers), np.array(my_numbers)))


def _parse_winning_and_your_numbers(game: str) -> tuple[list[int], list[int]]:
    return _parse_number(game.split(":")[1], 0), _parse_number(game, 1)


def _parse_number(game: str, group_number: int) -> [int]:
    return [int(item.group()) for item in re.finditer(r"\d+", game.split("|")[group_number])]


print(sum(_process_games("input.txt").values()))
