"""Day 13: Claw Contraptions, Part 1

The question in today's problem is a trick question. It asks to find the
minimum tokens to move the claw to the prize, but there is in fact only one
solution for each claw machine. The A and B button moves can be set up as a
system of equations:

    Ax * i + Bx * j = Px
    Ay * i + By * j = Py

Where i and j are the number of times the A and B buttons are pressed, Ax, Ay,
Bx, and By are the distances the claw moves in the x and y directions, and Px
and Py are the coordinates of the prize.

Multiplying the first equation by Ay and the second by Ax gives:

    Ax * Ay * i + Ay * Bx * j = Ay * Px
  - Ax * Ay * i + Ax * By * j = Ax * Py
    -----------------------------------
    Ay * Bx * j - Ax * By * j = Ay * Px - Ax * Py
    (Ay * Bx - Ax * By) * j = Ay * Px - Ax * Py
    j = (Ay * Px - Ax * Py) / (Ay * Bx - Ax * By)

Once j is known, i can be found by plugging it into the first equation:

    i = (Px - Bx * j) / Ax
"""

import re
from sys import stdin


def parse(input_string: str) -> tuple[tuple[int, int],
                                      tuple[int, int],
                                      tuple[int, int]]:
    """Parses the input string in the following form into a tuple of tuples of
    integers:

    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400

    Returns (94, 34, 22, 67, 8400, 5400)
    """

    a_regex = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
    b_regex = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
    p_regex = re.compile(r"Prize: X=(\d+), Y=(\d+)")

    a_match = a_regex.search(input_string)
    b_match = b_regex.search(input_string)
    p_match = p_regex.search(input_string)
    if a_match is None or b_match is None or p_match is None:
        raise ValueError("Invalid input string")
    button_a = (int(a_match.group(1)), int(a_match.group(2)))
    button_b = (int(b_match.group(1)), int(b_match.group(2)))
    prize = (int(p_match.group(1)), int(p_match.group(2)))

    return button_a, button_b, prize


def solve(button_a: tuple[int, int],
          button_b: tuple[int, int],
          prize: tuple[int, int]) -> int:
    """Returns the cost to the prize using jumps of A and B, where jumping A
    costs 3 tokens and jumping B costs 1 token.
    """
    a_x, a_y = button_a
    b_x, b_y = button_b
    p_x, p_y = prize
    j = (a_y * p_x - a_x * p_y) / (a_y * b_x - a_x * b_y)
    i = (p_x - b_x * j) / a_x

    # If i and j are not integers, the claw cannot reach the prize.
    if i % 1 != 0 or j % 1 != 0:
        return 0
    return int(3 * i + j)


def tests():
    """Tests for this module."""
    button_a, button_b, prize = (94, 34), (22, 67), (8400, 5400)
    assert solve(button_a, button_b, prize) == 280

    button_a, button_b, prize = (26, 66), (67, 21), (12748, 12176)
    assert solve(button_a, button_b, prize) == 0

    button_a, button_b, prize = (17, 86), (84, 37), (7870, 6450)
    assert solve(button_a, button_b, prize) == 200

    button_a, button_b, prize = (69, 23), (27, 71), (18641, 10279)
    assert solve(button_a, button_b, prize) == 0


def main(input_string: str) -> int:
    """Solves all puzzle inputs in a string"""
    total_cost = 0
    lines = input_string.splitlines()
    for i in range(0, len(lines), 4):
        button_a, button_b, prize = parse('\n'.join(lines[i:i+4]))
        total_cost += solve(button_a, button_b, prize)
    return total_cost


if __name__ == '__main__':
    tests()
    print(main(stdin.read()))
