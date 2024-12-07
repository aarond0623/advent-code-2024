"""Day 7: Bridge Repair, Part 1

Oh boy, here I go recursin' again.
"""

import sys
import re
from typing import Iterator


def parse(input_string: str) -> Iterator[tuple[int, list[int]]]:
    """Parses the input and returns a generator function for the result and the
    list of integers.
    """
    lines = re.finditer(r'(\d+): ([\d ]+)', input_string)
    for line in lines:
        n = int(line.group(1))
        to_test = [int(x) for x in line.group(2).split()]
        yield n, to_test


def is_valid(n: int, to_test: list[int]) -> bool:
    """A recursive function to test if a list of integers can equate to n using
    either multiplication or addition. For this calculation, the order of
    operations is ignored and calculated left to right.

    >>> is_valid(190, [10, 19])
    True
    >>> is_valid(3267, [81, 40, 27])
    True
    >>> is_valid(83, [17, 5])
    False
    >>> is_valid(156, [15, 6])
    False
    >>> is_valid(7290, [6, 8, 6, 15])
    False
    >>> is_valid(161011, [16, 10, 13])
    False
    >>> is_valid(192, [17, 8, 14])
    False
    >>> is_valid(21037, [9, 7, 18, 13])
    False
    >>> is_valid(292, [11, 6, 16, 20])
    True
    """

    # BASE CASE
    if len(to_test) == 1:
        if n == to_test[0]:
            return True
        return False

    result = False
    if n % to_test[-1] == 0:
        result = is_valid(n // to_test[-1], to_test[:-1])
    return result or is_valid(n - to_test[-1], to_test[:-1])


def main(input_string: str) -> int:
    """Returns the sum of all valid numbers."""
    return sum(x[0] for x in parse(input_string) if is_valid(*x))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(main(sys.stdin.read()))
