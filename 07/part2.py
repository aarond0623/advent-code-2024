"""Day 7: Bridge Repair, Part 2
"""

import sys
from part1 import parse


def is_valid(n: int, to_test: list[int]) -> bool:
    """A recursive function to test if a list of integers can equate to n using
    either multiplication, addition, or concatenation. For this calculation,
    the order of operations is ignored and calculated left to right.

    >>> is_valid(190, [10, 19])
    True
    >>> is_valid(3267, [81, 40, 27])
    True
    >>> is_valid(83, [17, 5])
    False
    >>> is_valid(156, [15, 6])
    True
    >>> is_valid(7290, [6, 8, 6, 15])
    True
    >>> is_valid(161011, [16, 10, 13])
    False
    >>> is_valid(192, [17, 8, 14])
    True
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

    if n < 0:
        return False

    tests = []
    current_number = to_test[-1]
    to_test = to_test[:-1]

    # Test multiplication
    if n % current_number == 0:
        tests.append((n // current_number, to_test))

    # Test concatenation
    stop = len(str(n)) - len(str(current_number))
    if stop > 0 and str(n)[stop:] == str(current_number):
        tests.append((int(str(n)[:stop]), to_test))
    tests.append((n - current_number, to_test))
    return any(is_valid(*x) for x in tests)


def main(input_string: str) -> int:
    """Returns the sum of all valid numbers."""
    return sum(x[0] for x in parse(input_string) if is_valid(*x))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(main(sys.stdin.read()))
