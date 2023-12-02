import re
from functools import reduce
from toolz import compose


game_information_regex: str = r"Game\s([0-9]+):( [0-9]+ (blue|red|green))+"


def _read_file(filename: str) -> [str]:
    with open(filename) as file:
        return [line.rstrip() for line in file]


def _determine_fewest_number_of_cubes(game_information: str) -> dict[str, int]:
    assert re.compile(game_information_regex).match(game_information), "game information '%s' is invalid" % game_information
    return _determine_max_cubes_per_color([_parse_cubes_of_game_part(e) for e in _parse_cube_sets(game_information)], {})


def _determine_max_cubes_per_color(game_parts: [dict[str, int]], max_cubes_per_color: dict[str, int]) -> dict[str, int]:
    if not game_parts:
        return max_cubes_per_color

    current_game_part: dict[str, int] = game_parts[0]
    for color in current_game_part.keys():
        max_cubes_per_color[color] = max(current_game_part[color], max_cubes_per_color.get(color, 0))

    return _determine_max_cubes_per_color(game_parts[1:], max_cubes_per_color)


def _parse_cubes_of_game_part(game_set: str) -> dict[str, int]:
    return {cube.split()[1]: int(cube.split()[0]) for cube in game_set.split(",")}


def _parse_cube_sets(game_information: str) -> [str]:
    return game_information.split(":")[1].split(";")


def _calculate_power_of_cubes(cubes: dict[str, int]) -> int:
    # the applicative order reduction greets you
    return reduce(lambda x, y: x*y, cubes.values())


print(sum([compose(_calculate_power_of_cubes, _determine_fewest_number_of_cubes)(game_information)
           for index, game_information in enumerate(_read_file("input.txt"))]))
