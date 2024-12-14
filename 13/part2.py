"""Day 13: Claw Contraptions, Part 2"""

from sys import stdin
from part1 import parse, solve


def tests():
    """Tests for this module."""
    button_a, button_b = (94, 34), (22, 67)
    prize = (10000000008400, 10000000005400)
    assert solve(button_a, button_b, prize) == 0

    button_a, button_b = (26, 66), (67, 21)
    prize = (10000000012748, 10000000012176)
    assert solve(button_a, button_b, prize) > 0

    button_a, button_b = (17, 86), (84, 37)
    prize = (10000000007870, 10000000006450)
    assert solve(button_a, button_b, prize) == 0

    button_a, button_b = (69, 23), (27, 71)
    prize = (10000000018641, 10000000010279)
    assert solve(button_a, button_b, prize) > 0


def main(input_string: str) -> int:
    """Solves all puzzle inputs in a string"""
    total_cost = 0
    lines = input_string.splitlines()
    for i in range(0, len(lines), 4):
        button_a, button_b, prize = parse('\n'.join(lines[i:i+4]))
        prize = (10000000000000 + prize[0], 10000000000000 + prize[1])
        total_cost += solve(button_a, button_b, prize)
    return total_cost


if __name__ == '__main__':
    tests()
    print(main(stdin.read()))
