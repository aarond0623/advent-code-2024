"""Day 3: Mull It Over, Part 2

This module takes input from stdin and finds valid multiplication commands in
the form of mul(x,y), but ignores all commands following a don't() command
until a corresponding do() command. It then multiplies x and y for all commands
and returns the sum of the products.
"""


import sys
import re


def main(input_string: str) -> int:
    """Calculates the sum of mul() multiplication commands in a string, unless
    disabled by a don't()-do() span.

    >>> main("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
    48

    mul(5,5) and mul(11,8) are disabled by don't(). mul(2,4) is counted, and
    the mul(8,5) following do() is also counted. 2 * 4 + 8 * 5 = 48.
    """

    # Capture either do(), don't(), or mul(x, y)
    pattern = r"do\(\)|don't\(\)|(mul)\((\d+),(\d+)\)"
    results = re.finditer(pattern, input_string)

    total = 0

    # Whether or not to count a product
    do = True
    for result in results:
        if result.group(0) == "don't()":
            do = False
        elif result.group(0) == 'do()':
            do = True
        # We should never be able to get here without a group(1)
        elif result.group(1) == 'mul' and do:
            total += int(result.group(2)) * int(result.group(3))

    return total


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(main(sys.stdin.read()))
