"""Day 8: Resonant Collinearity, Part 2
"""

import sys
from itertools import combinations
from part1 import parse


def main(input_string: str) -> int:
    """Calculates the number of antinodes in a grid given a string of antennae
    locations. Antinodes are always a multiple of the distance between pairs of
    antennae, and antennae also count as antinodes.

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
    34
    """
    width = len(input_string.split('\n')[0])
    height = len([x for x in input_string.split('\n') if x != ''])
    antennae_dict = parse(input_string)

    antinodes = set()

    for antennae in antennae_dict.values():
        for a1, a2 in combinations(antennae, 2):
            rise, run = a2[0] - a1[0], a2[1] - a1[1]
            new_antinodes = []
            i, j = a1
            while 0 <= i < height and 0 <= j < width:
                new_antinodes.append((i, j))
                i += rise
                j += run
            i, j = a1
            i -= rise
            j -= run
            while 0 <= i < height and 0 <= j < width:
                new_antinodes.append((i, j))
                i -= rise
                j -= run

            antinodes.update(new_antinodes)

    return len(antinodes)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(main(sys.stdin.read()))
