written_numbers: dict[str, int] = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def _read_file(filename: str) -> [str]:
    with open(filename) as file:
        return [line.rstrip() for line in file]


def _parse_numbers_in_line(line: str, numbers_within_line: [int]) -> [int]:
    if not line:
        return numbers_within_line

    if line[0].isdigit():
        return _parse_numbers_in_line(line[1:], numbers_within_line + [int(line[0])])
    elif line[:3] in written_numbers.keys():
        return _parse_numbers_in_line(line[2:], numbers_within_line + [written_numbers[line[:3]]])
    elif line[:4] in written_numbers.keys():
        return _parse_numbers_in_line(line[3:], numbers_within_line + [written_numbers[line[:4]]])
    elif line[:5] in written_numbers.keys():
        return _parse_numbers_in_line(line[4:], numbers_within_line + [written_numbers[line[:5]]])
    else:
        return _parse_numbers_in_line(line[1:], numbers_within_line)


def _extract_calibration_values(line: str) -> int:
    line_numbers = _parse_numbers_in_line(line, [])
    assert len(line_numbers) >= 1, "at least on number must exist per line"

    return int("%s%s" % (line_numbers[0], line_numbers[0])) if len(line_numbers) == 1 else int("%s%s" % (line_numbers[0], line_numbers[-1]))


print(sum([_extract_calibration_values(line) for line in _read_file("input.txt")]))
