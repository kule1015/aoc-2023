import re

input_filename: str = "input.txt"


def handle(number: int, number_mapper):
    mapped_number: [int] = [new + (number - start) for start, end, new in number_mapper if start <= number <= end]
    if len(mapped_number) == 1:
        return mapped_number[0]
    elif len(mapped_number) >= 1:
        raise Exception("invalid state")
    else:
        return number


with open(input_filename) as file:
    current_numbers: [int] = []
    current_number_mapper = []

    for line in file:
        if re.compile("seeds:.*").match(line):
            current_numbers = [int(number.group()) for number in re.finditer(r"\d+", line)]
        elif re.compile("[a-z- ]+:").match(line):
            current_number_mapper = []
        elif not line.strip():
            current_numbers = [handle(number, current_number_mapper) for number in current_numbers]
        else:
            m: [int] = [int(x.group()) for x in re.finditer("\d+", line)]
            assert len(m) == 3
            current_number_mapper = current_number_mapper + [(m[1], m[1]+(m[2]-1), m[0])]
    current_numbers = [handle(number, current_number_mapper) for number in current_numbers]

    print(min(current_numbers))
