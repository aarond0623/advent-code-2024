"""Day 14: Restroom Redoubt, Part 1"""

from sys import stdin
import re


def parse(line: str) -> tuple[complex, complex]:
    """Parses a line of input into a tuple of two complex numbers, the robot's
    current position and velocity.
    """
    match = re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
    if match is None:
        raise ValueError("Invalid input string")
    p = complex(int(match.group(1)), int(match.group(2)))
    v = complex(int(match.group(3)), int(match.group(4)))
    return p, v


def move(robot: tuple[complex, complex],
         width: int,
         height: int) -> tuple[complex, complex]:
    """Moves the robot one step in the direction of its velocity, while
    wrapping to the opposite wall if it reaches a border.
    """
    p = robot[0] + robot[1]
    x = p.real % width
    y = p.imag % height

    return (complex(x, y), robot[1])


def tests():
    """Tests for this module."""
    robot = (2 + 4j, 2 - 3j)
    assert move(robot, 11, 7) == ((4 + 1j), (2 - 3j))
    assert move(move(robot, 11, 7), 11, 7) == ((6 + 5j), (2 - 3j))

    input_string = """p=0,4 v=3,-3
    p=6,3 v=-1,-3
    p=10,3 v=-1,2
    p=2,0 v=2,-1
    p=0,0 v=1,3
    p=3,0 v=-2,-2
    p=7,6 v=-1,-3
    p=3,0 v=-1,-2
    p=9,3 v=2,3
    p=7,3 v=-1,2
    p=2,4 v=2,-3
    p=9,5 v=-3,-3"""
    width, height = 11, 7
    robots = [parse(line) for line in input_string.splitlines()]
    for _ in range(100):
        robots = [move(robot, width, height) for robot in robots]

    x = width // 2
    y = height // 2

    q1 = sum(1 for robot in robots if robot[0].real < x and robot[0].imag < y)
    q2 = sum(1 for robot in robots if robot[0].real > x and robot[0].imag < y)
    q3 = sum(1 for robot in robots if robot[0].real < x and robot[0].imag > y)
    q4 = sum(1 for robot in robots if robot[0].real > x and robot[0].imag > y)

    assert q1 == 1
    assert q2 == 3
    assert q3 == 4
    assert q4 == 1


def main(input_string: str) -> int:
    """Calculates the "safety factor" after 100 moves by multiplying the number
    of robots in each quadrant.
    """
    width, height = 101, 103
    robots = [parse(line) for line in input_string.splitlines()]
    for _ in range(100):
        robots = [move(robot, width, height) for robot in robots]

    x = width // 2
    y = height // 2

    q1 = sum(1 for robot in robots if robot[0].real < x and robot[0].imag < y)
    q2 = sum(1 for robot in robots if robot[0].real > x and robot[0].imag < y)
    q3 = sum(1 for robot in robots if robot[0].real < x and robot[0].imag > y)
    q4 = sum(1 for robot in robots if robot[0].real > x and robot[0].imag > y)

    return q1 * q2 * q3 * q4


if __name__ == '__main__':
    tests()
    print(main(stdin.read()))
