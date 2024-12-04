"""Day 4: Ceres Search, Part 1

This module takes input from stdin and performs a word search in all
directions, then returns how many instances of the word were found in the
search.
"""

import sys
import numpy as np
from numpy.typing import NDArray


def parse(input_string: str) -> NDArray[np.str_]:
    """Parses a block of text into a 2D Numpy array of characters.

    >>> input_string = '''\\
    ... ABCD
    ... EFGH
    ... IJKL'''

    >>> parse(input_string)
    array([['A', 'B', 'C', 'D'],
           ['E', 'F', 'G', 'H'],
           ['I', 'J', 'K', 'L']], dtype='<U1')
    """
    return np.array([list(x) for x in input_string.split('\n') if x != ''])


def np_strings(array: NDArray[np.str_], i: int, j: int, l: int) -> list[str]:
    """Returns all substrings of a given length from a Numpy array, starting at
    position (i, j), in 8 cardinal directions (like a word search).

    >>> array = np.array([\\
    ... ['A', 'B', 'C', 'D'],
    ... ['E', 'F', 'G', 'H'],
    ... ['I', 'J', 'K', 'L']])

    >>> np_strings(array, 1, 1, 2)
    ['FG', 'FK', 'FJ', 'FI', 'FE', 'FA', 'FB', 'FC']

    >>> np_strings(array, 1, 3, 2)
    ['HL', 'HK', 'HG', 'HC', 'HD']

    >>> np_strings(array, 1, 1, 3)
    ['FGH']
    """

    s = []

    height, width = array.shape

    # East
    if j + l <= width:
        s.append(''.join(array[i, j:j+l]))
    # Southeast
    if i + l <= height and j + l <= width:
        s.append(''.join(array[i:i+l, j:j+l].diagonal()))
    # South
    if i + l <= height:
        s.append(''.join(array[i:i+l, j]))
    # Southwest
    if i + l <= height and j - l >= -1:
        s.append(''.join(np.fliplr(array[i:i+l, j-l+1:j+1]).diagonal()))
    # West
    if j - l >= -1:
        s.append(''.join(array[i, j-l+1:j+1])[::-1])
    # Northwest
    if i - l >= -1 and j - l >= -1:
        s.append(''.join(array[i-l+1:i+1, j-l+1:j+1].diagonal())[::-1])
    # North
    if i - l >= -1:
        s.append(''.join(array[i-l+1:i+1, j])[::-1])
    # Northeast
    if i - l >= -1 and j + l <= width:
        s.append(''.join(np.flipud(array[i-l+1:i+1, j:j+l]).diagonal()))

    return s


def main(input_string: str, substring: str) -> int:
    """Caunts the number of times a substring appears in a string either down,
    across, or diagonally (like a word search).

    >>> input_string = '''\\
    ... MMMSXXMASM
    ... MSAMXMSMSA
    ... AMXSXMAAMM
    ... MSAMASMSMX
    ... XMASAMXAMM
    ... XXAMMXXAMA
    ... SMSMSASXSS
    ... SAXAMASAAA
    ... MAMMMXMMMM
    ... MXMXAXMASX'''

    >>> main(input_string, 'XMAS')
    18
    """

    array = parse(input_string)
    height, width = array.shape
    length = len(substring)

    total = 0

    for i in (range(0, height)):
        for j in range(0, width):
            if array[i, j] != substring[0] and array[i, j] != substring[-1]:
                continue
            substrings = np_strings(array, i, j, length)
            total += substrings.count(substring)

    return total


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(main(sys.stdin.read(), 'XMAS'))
