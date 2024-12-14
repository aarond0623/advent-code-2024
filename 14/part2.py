"""Day 14: Restroom Redoubt, Part 2"""

from sys import stdin
from time import sleep
from part1 import parse, move


def print_robots(robots: list[tuple[complex, complex]],
                 width: int,
                 height: int) -> list[list[str]]:
    """Prints the positions of the robot as a series of *s and .s."""
    grid = [['  ' for _ in range(width)] for _ in range(height)]
    for robot in robots:
        grid[int(robot[0].imag)][int(robot[0].real)] = '██'

    return grid


def main(input_string: str):
    """Prints the robots to the screen."""
    width, height = 101, 103
    robots = [parse(line) for line in input_string.splitlines()]
    i = 0
    while True:
        grid = print_robots(robots, width, height)

        if any(row.count('██') > 20 for row in grid):
            print('\n'.join(''.join(row) for row in grid))
            print(i)
            sleep(0.5)

        robots = [move(robot, width, height) for robot in robots]
        i += 1


if __name__ == '__main__':
    main(stdin.read())
