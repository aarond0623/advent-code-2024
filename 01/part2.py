"""Day 1: Historian Hysteria

This module takes input from stdin in the form of two lists of integers,
formatted vertically. It then calculates the sum of the "similiarity scores"
for list1, defined as the sum of:

list1[i] * list2.count(list1[i])

for each element in list1.
"""

import sys
from part1 import parse


def generate_counts(id_list: list[int]) -> dict[int, int]:
    """Generates a dictionary of the counts of each element in list1."""
    counts: dict[int, int] = {}
    for number in id_list:
        counts[number] = counts.get(number, 0) + 1
    return counts


def main(input_string: str) -> int:
    """Calculates the sum of similarities scores between two lists.

    >>> input_test = '''3   4
    ... 4   3
    ... 2   5
    ... 1   3
    ... 3   9
    ... 3   3'''
    >>> main(input_test)
    31
    """
    list1, list2 = parse(input_string)
    counts = generate_counts(list2)
    return sum(x * counts.get(x, 0) for x in list1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(main(sys.stdin.read()))
