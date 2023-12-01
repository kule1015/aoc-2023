def _read_file(filename: str) -> [str]:
    with open(filename) as file:
        return [line.rstrip() for line in file]


def _extract_calibration_value(line: str) -> int:
    line_numbers = list(filter(lambda character: character.isdigit(), line))
    assert len(line_numbers) >= 1, "at least on number must exist per line"

    calibration_value: str = "%s%s" % (line_numbers[0], line_numbers[0]) if len(line_numbers) == 1 else "%s%s" % (line_numbers[0], line_numbers[-1])
    return int(calibration_value)


print(sum([_extract_calibration_value(line) for line in _read_file("input.txt")]))
