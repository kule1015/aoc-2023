import re


def _read_file(filename: str) -> [str]:
    with open(filename) as file:
        return [line.rstrip() for line in file]


def _create_matrix(file_content: [str]) -> [[]]:
    assert file_content, "file content has no elements"
    number_of_rows, number_of_columns = len(file_content), len(file_content[0])
    return [[file_content[row][column] for column in range(number_of_columns)] for row in range(number_of_rows)]


def _collect_numbers_adjacent_to_symbols(numbers: [[]], numbers_adjacent_to_symbols: [int]):
    for row in range(len(numbers)):
        for column in range(len(numbers[0])):
            if numbers[row][column] == "*":
                adjacent_numbers = _determine_adjacent_numbers(numbers, row, column)
                if len(adjacent_numbers) == 2:
                    numbers_adjacent_to_symbols.append(adjacent_numbers[0]*adjacent_numbers[1])

    return numbers_adjacent_to_symbols


def _determine_adjacent_numbers(numbers: [[]], row: int, column: int):
    return list(set(filter(lambda x: isinstance(x, int), [
        _is_number_adjacent(numbers, row, column + 1),
        _is_number_adjacent(numbers, row + 1, column + 1),
        _is_number_adjacent(numbers, row + 1, column),
        _is_number_adjacent(numbers, row + 1, column - 1),
        _is_number_adjacent(numbers, row, column - 1),
        _is_number_adjacent(numbers, row - 1, column - 1),
        _is_number_adjacent(numbers, row - 1, column),
        _is_number_adjacent(numbers, row - 1, column + 1),
    ])))


def _is_number_adjacent(numbers: [[]], row: int, column: int) -> int | None:
    if row < 0 or row >= len(numbers):
        return
    if column < 0 or column >= len(numbers[row]):
        return

    if numbers[row][column].isdigit():
        return [int(number.group()) for number in re.finditer(r"\d+", "".join(numbers[row])) if number.start() <= column <= number.end()][0]

    return


print(sum(_collect_numbers_adjacent_to_symbols(_create_matrix(_read_file("input.txt")), [])))
