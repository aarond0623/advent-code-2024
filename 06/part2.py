"""Day 6: Guard Gallivant, Part 2

Uses the Guard class from Part 1 in order to see what in what positions we can
places a new obstacle to create loops.
"""

import sys
from part1 import Guard, parse


def main(input_string: str) -> int:
    """Finds how many positions in the input we can put a new obstacle and
    create a looping guard.
    """
    width, height, pos, obstacles = parse(input_string)

    # Get every position visited by the guard normally; these are the only
    # positions that will effect a change on the path.
    guard = Guard(width, height, pos, obstacles)
    guard.route('up')
    obstacles_to_check = guard.get_visits()

    # Total number of obstacles we can place to get loops
    total = 0
    for obstacle in obstacles_to_check:
        new_obstacles = obstacles + [obstacle]
        guard = Guard(width, height, pos, new_obstacles)

        # Re-implementation of Guard.route because we need to keep track of
        # what direction the guard ends on to see if this is a loop or an
        # exit.
        directions = ['up', 'right', 'down', 'left']
        i = -1
        while guard.go:
            i = (i + 1) % len(directions)
            guard.move(directions[i])
        if ((directions[i], guard.pos[1]) != ('up', 0) and
                (directions[i], guard.pos[0]) != ('right', width - 1) and
                (directions[i], guard.pos[1]) != ('down', height - 1) and
                (directions[i], guard.pos[0]) != ('left', 0)):
            total += 1
    return total


if __name__ == '__main__':
    print(main(sys.stdin.read()))
