from itertools import takewhile
from typing import Tuple


def _read_file(filename: str) -> [str]:
    with open(filename) as file:
        return [line.rstrip() for line in file]


def _create_matrix(file_content: [str]) -> [[]]:
    assert file_content, "file content has no elements"
    number_of_rows, number_of_columns = len(file_content), len(file_content[0])
    return [[file_content[row][column] for column in range(number_of_columns)] for row in range(number_of_rows)]


"""
max recursion depth to puzzle input :(
"""
# def _collect_numbers_adjacent_to_symbols(numbers: [[]], numbers_adjacent_to_symbols: [int], row: int = 0, column: int = 0):
#     if row >= len(numbers):
#         return numbers_adjacent_to_symbols
#
#     if column >= len(numbers[row]):
#         return _collect_numbers_adjacent_to_symbols(numbers, numbers_adjacent_to_symbols, row + 1, 0)
#
#     if numbers[row][column].isdigit():
#         number_tuple: [Tuple[int, bool]] = _get_indices_of_number(numbers, row, column)
#         if any([tup[1] for tup in number_tuple]):
#             sliced_number: [str] = numbers[row][number_tuple[0][0]:number_tuple[-1][0]+1]
#             numbers_adjacent_to_symbols = numbers_adjacent_to_symbols + [int("".join(sliced_number))]
#             return _collect_numbers_adjacent_to_symbols(numbers, numbers_adjacent_to_symbols, row, column + len(number_tuple))
#
#     return _collect_numbers_adjacent_to_symbols(numbers, numbers_adjacent_to_symbols, row, column + 1)


def _collect_numbers_adjacent_to_symbols(numbers: [[]], numbers_adjacent_to_symbols: [int]):
    row = 0
    column = 0

    while row < len(numbers):
        while column < len(numbers[row]):
            if numbers[row][column].isdigit():
                number_tuple: [Tuple[int, bool]] = _get_indices_of_number(numbers, row, column)
                if any([tup[1] for tup in number_tuple]):
                    sliced_number: [str] = numbers[row][number_tuple[0][0]:number_tuple[-1][0] + 1]
                    numbers_adjacent_to_symbols = numbers_adjacent_to_symbols + [int("".join(sliced_number))]

                column += len(number_tuple)
            else:
                column += 1
        row += 1
        column = 0

    return numbers_adjacent_to_symbols


def _get_indices_of_number(numbers: [[]], row_number: int, number_starting_column: int) -> [int]:
    return [(tup[0], _determine_adjacent_symbols(numbers, row_number, tup[0]))
            for tup in takewhile(lambda y: y[1].isdigit(), enumerate(numbers[row_number][number_starting_column:], number_starting_column))]


def _determine_adjacent_symbols(numbers: [[]], row: int, column: int) -> bool:
    return any([
        _is_symbol(numbers, row, column + 1),
        _is_symbol(numbers, row + 1, column + 1),
        _is_symbol(numbers, row + 1, column),
        _is_symbol(numbers, row + 1, column - 1),
        _is_symbol(numbers, row, column - 1),
        _is_symbol(numbers, row - 1, column - 1),
        _is_symbol(numbers, row - 1, column),
        _is_symbol(numbers, row - 1, column + 1),
    ])


def _is_symbol(numbers: [[]], row: int, column: int) -> bool:
    if row < 0 or row >= len(numbers):
        return False
    if column < 0 or column >= len(numbers[row]):
        return False

    return numbers[row][column].isdigit() is False and numbers[row][column] != "."


print(sum(_collect_numbers_adjacent_to_symbols(_create_matrix(_read_file("input.txt")), [])))
