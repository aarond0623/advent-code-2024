"""Day 11: Plutonian Pebbles, Part 1
"""

from sys import stdin


def init_pebbles(input_string: str) -> dict[int, int]:
    """Returns a map of integers and counts from a string of integers."""
    numbers = [int(x) for x in input_string.split()]
    pebbles: dict[int, int] = {}
    for n in numbers:
        pebbles[n] = pebbles.get(n, 0) + 1
    return pebbles


def blink(pebble: int) -> list[int]:
    """Transforms a pebble according to the following rules:

    if pebble = 0, return [1]
    if pebble has even digits, return [first half, second half]
    else, return pebble * 2024
    """
    if pebble == 0:
        return [1]
    length = len(str(pebble))
    if length % 2 == 0:
        length //= 2
        return [int(str(pebble)[:length]), int(str(pebble)[length:])]
    return [pebble * 2024]


def blink_all_pebbles(pebbles: dict[int, int]) -> dict[int, int]:
    """Performs the blink operating for all pebbles in a map."""
    new_pebbles: dict[int, int] = {}
    for n in pebbles.keys():
        for blinked in blink(n):
            new_pebbles[blinked] = new_pebbles.get(blinked, 0) + pebbles[n]
    return new_pebbles


def tests():
    """Tests for this module."""
    input_test = "0 1 10 99 999"
    pebbles = init_pebbles(input_test)
    pebbles = blink_all_pebbles(pebbles)
    assert sum(pebbles.values()) == 7

    input_test = "125 17"
    pebbles = init_pebbles(input_test)
    for _ in range(6):
        pebbles = blink_all_pebbles(pebbles)
    assert sum(pebbles.values()) == 22


def main(input_string: str, count: int) -> int:
    """Solution for Day 11, Part 1"""
    pebbles = init_pebbles(input_string)
    for _ in range(count):
        pebbles = blink_all_pebbles(pebbles)
    return sum(pebbles.values())


if __name__ == '__main__':
    tests()
    print(main(stdin.read().splitlines()[0], 25))
