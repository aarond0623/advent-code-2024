"""Day 1: Historian Hysteria

This module takes input from stdin in the form of two lists of integers,
formatted vertically. It then sorts the lists, calculates the absolute value of
the difference between each pair of integers, and prints the sum of those
differences.
"""

import sys


def parse(input_string: str) -> tuple[list[int], list[int]]:
    """Parses a string of integers into two lists of integers."""
    list1 = []
    list2 = []
    for line in input_string.splitlines():
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))
    return list1, list2


def main(input_string: str) -> int:
    """Calculates the sum of differences between two lists of integers.

    >>> input_test = '''3   4
    ... 4   3
    ... 2   5
    ... 1   3
    ... 3   9
    ... 3   3'''
    >>> main(input_test)
    11
    """
    list1, list2 = parse(input_string)
    list1.sort()
    list2.sort()
    total = 0
    for i, j in zip(list1, list2):
        total += abs(i - j)
    return total


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(main(sys.stdin.read()))
