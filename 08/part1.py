"""Day 8: Resonant Collinearity, Part 1
"""

import sys
from itertools import combinations


def parse(input_string: str) -> dict[str, list[tuple[int, int]]]:
    """Takes an input string and returns a dictionary of all antennae and their
    coordinates.

    >>> input_string = '''\\
    ... ............
    ... ........0...
    ... .....0......
    ... .......0....
    ... ....0.......
    ... ......A.....
    ... ............
    ... ............
    ... ........A...
    ... .........A..
    ... ............
    ... ............'''

    >>> parse(input_string)
    {'0': [(1, 8), (2, 5), (3, 7), (4, 4)], 'A': [(5, 6), (8, 8), (9, 9)]}
    """
    antennae: dict[str, list[tuple[int, int]]] = {}
    for i, line in enumerate(input_string.split('\n')):
        for j, char in enumerate(line):
            if char != '.':
                antennae[char] = antennae.get(char, []) + [(i, j)]
    return antennae


def main(input_string: str) -> int:
    """Calculates the number of antinodes in a grid given a string of antennae
    locations. Antinodes are always the same distance outside either antenna as
    each antenna is from its pair.

    >>> input_string = '''\\
    ... ............
    ... ........0...
    ... .....0......
    ... .......0....
    ... ....0.......
    ... ......A.....
    ... ............
    ... ............
    ... ........A...
    ... .........A..
    ... ............
    ... ............'''

    >>> main(input_string)
    14
    """
    width = len(input_string.split('\n')[0])
    height = len([x for x in input_string.split('\n') if x != ''])
    antennae_dict = parse(input_string)

    antinodes = set()

    for antennae in antennae_dict.values():
        for a1, a2 in combinations(antennae, 2):
            rise, run = a2[0] - a1[0], a2[1] - a1[1]
            antinode1 = (a2[0] + rise, a2[1] + run)
            antinode2 = (a1[0] - rise, a1[1] - run)

            for antinode in (antinode1, antinode2):
                if 0 <= antinode[0] < height and 0 <= antinode[1] < width:
                    antinodes.add(antinode)

    return len(antinodes)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(main(sys.stdin.read()))
