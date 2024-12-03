"""Day 3: Mull It Over, Part 1

This module takes input from stdin and finds valid multiplication commands in
the form of mul(x,y). It then multiplies x and y for all commands and returns
the sum of the products.
"""

import sys
import re


def main(input_string: str) -> int:
    """Calculates the sum of mul() multiplication commands in a string.

    >>> main('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))')
    161

    (2 * 4 + 5 * 5 + 11 * 8 + 8 * 5)
    """
    total = 0
    results = re.findall(r'mul\((\d+),(\d+)\)', input_string)
    for result in results:
        total += (int(result[0]) * int(result[1]))

    return total


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(main(sys.stdin.read()))
