import re

import numpy as np


def _read_file(filename: str) -> [str]:
    with open(filename) as file:
        return [line.rstrip() for line in file]


def _calculate_game_score(game_information: tuple[list[int], list[int]]) -> int:
    winning_numbers, my_numbers = game_information
    number_matching_numbers: int = len(np.intersect1d(np.array(winning_numbers), np.array(my_numbers)))
    return pow(2,  number_matching_numbers - 1) if number_matching_numbers >= 1 else 0


def _parse_winning_and_your_numbers(line: str) -> tuple[list[int], list[int]]:
    return _parse_number(line.split(":")[1], 0), _parse_number(line, 1)


def _parse_number(line: str, group_number: int) -> [int]:
    return [int(item.group()) for item in re.finditer(r"\d+", line.split("|")[group_number])]


print(sum([_calculate_game_score(_parse_winning_and_your_numbers(line)) for line in _read_file("input.txt")]))
