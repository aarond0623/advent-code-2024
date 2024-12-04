"""Day 4: Ceres Search, Part 2

This module takes input from stdin and performs a word search in the diagonal
directions, then returns how many instances of the word were found in an X
pattern.
"""

import sys
import numpy as np
from numpy.typing import NDArray
from part1 import parse


def np_xstrings(array: NDArray[np.str_], i: int, j: int, l: int) -> list[str]:
    """Returns the diagonal substrings of a given length from a Numpy array
    with the northwest corner at (i, j).

    >>> array = np.array([\\
    ... ['A', 'B', 'C', 'D'],
    ... ['E', 'F', 'G', 'H'],
    ... ['I', 'J', 'K', 'L']])

    >>> np_xstrings(array, 1, 1, 2)
    ['FK', 'GJ', 'KF', 'JG']

    >>> np_xstrings(array, 1, 3, 2)
    []
    """

    height, width = array.shape

    if i + l > width or j + l > height:
        return []

    subarray = array[i:i+l, j:j+l]
    diag1 = ''.join(subarray.diagonal())
    diag2 = ''.join(np.fliplr(subarray).diagonal())

    return [diag1, diag2, diag1[::-1], diag2[::-1]]


def main(input_string: str, substring: str) -> int:
    """Counts the number of times a substring appears in a string in an X
    formation, i.e. diagonally, either forwards or backwards, crossing each
    other.

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

    >>> main(input_string, 'MAS')
    9
    """

    array = parse(input_string)
    height, width = array.shape
    length = len(substring)

    total = 0

    for i in range(0, height - length + 1):
        for j in range(0, width - length + 1):
            if array[i, j] != substring[0] and array[i, j] != substring[-1]:
                continue
            substrings = np_xstrings(array, i, j, length)
            # An X will have at least 2 counts (4 if word is a palindrome)
            if substrings.count(substring) >= 2:
                total += 1
    return total


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(main(sys.stdin.read(), 'MAS'))
