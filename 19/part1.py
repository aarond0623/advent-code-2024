"""Day 19, Part 1: Linen Layout"""

from sys import stdin
from functools import cache

PATTERNS: list[str] = []
MAXLEN = 0


def parse(input_string: str) -> tuple[list[str], list[str]]:
    """Parses the input into lists of available towels and needed patterns."""
    lines = input_string.splitlines()
    patterns = lines[0].split(', ')
    designs = lines[2:]
    return patterns, designs


@cache
def possible(design: str) -> bool:
    """Determins if a design is possible to make out of the provided patterns.
    """
    if design == "":
        return True
    for i in range(min(len(design), MAXLEN) + 1):
        if design[:i] in PATTERNS and possible(design[i:]):
            return True
    return False


def tests():
    """Tests for this module."""
    input_string = '''\
    r, wr, b, g, bwu, rb, gb, br

    brwrr
    bggr
    gbbr
    rrbgbr
    ubwu
    bwurrg
    brgr
    bbrgwb
    '''.replace('    ','')

    global PATTERNS, MAXLEN
    PATTERNS, designs = parse(input_string)
    assert PATTERNS == ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br']
    assert designs == ['brwrr', 'bggr', 'gbbr', 'rrbgbr',
                       'ubwu', 'bwurrg', 'brgr', 'bbrgwb']

    MAXLEN = max(map(len, PATTERNS))
    check = [possible(x) for x in designs]
    assert check == [True, True, True, True, False, True, True, False]


def main(input_string: str) -> int:
    """Finds how many patterns are possible."""
    global PATTERNS, MAXLEN
    PATTERNS, designs = parse(input_string)
    MAXLEN = max(map(len, PATTERNS))
    return sum(1 if possible(x) else 0 for x in designs)


if __name__ == '__main__':
    tests()
    print(main(stdin.read()))
