import re

allowed_number_of_cubeds: dict[str, int] = {
    "red": 12,
    "green": 13,
    "blue": 14
}

game_information_regex: str = r"Game\s([0-9]+):( [0-9]+ (blue|red|green))+"
cube_regex: str = r"([0-9]+)(blue|red|green)"


def _read_file(filename: str) -> [str]:
    with open(filename) as file:
        return [line.rstrip() for line in file]


def _is_game_valid(allowed_cubes: dict[str, int], game_information: str):
    assert re.compile(game_information_regex).match(game_information), "game information '%s' is invalid" % game_information
    return all([_is_game_part_possible(_parse_cubes_of_game_set(e), allowed_cubes) for e in _parse_cube_sets(game_information)])


def _is_game_part_possible(cubes_of_game: [str, int], allowed_cubes_of_games: [str, int]) -> bool:
    return all([int(cubes_of_game[cube]) <= int(allowed_cubes_of_games[cube]) for cube in cubes_of_game.keys()])


def _parse_cubes_of_game_set(game_set: str) -> dict[str, int]:
    return {cube.split()[1]: int(cube.split()[0]) for cube in game_set.split(",")}


def _parse_cube_sets(game_information: str) -> [str]:
    return game_information.split(":")[1].split(";")


print(sum([index + 1 for index, game_information in enumerate(_read_file("input.txt")) if _is_game_valid(allowed_number_of_cubeds, game_information)]))

# reading helps, stupido!!
