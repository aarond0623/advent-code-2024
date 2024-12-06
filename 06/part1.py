"""Day 6: Guard Gallivant, Part 1

Implements a Guard class, that calculates movements by calculating straight
lines in the direction of movement, then adding the position tuples to a map.
If the guard visits a position he has visited before (in the same direction) or
exits the field, the Guard will stop moving.
"""

import sys


class Guard:
    """Class for the guard with methods for automatically moving as far as
    possible."""
    def __init__(self,
                 width: int,
                 height: int,
                 position: tuple[int, int],
                 obstacles: list[tuple[int, int]]):
        self.width = width
        self.height = height
        self.pos = position
        self.obstacles = obstacles

        self.visits: dict[str, set[tuple[int, int]]] = {'right': set(),
                                                        'up': set(),
                                                        'left': set(),
                                                        'down': set()}
        self.go = True

    def move(self, direction: str):
        """Moves the guard as far as possible in the specified direction, until
        the guard leaves the field or visits a position already visited."""
        # Stop if we return to a position we've been before
        if self.pos in self.visits[direction]:
            self.go = False
            return
        # Variables for different directions
        var = {'right': (1, 0, 1, self.width),
               'up': (0, 1, -1, -1),
               'left': (1, 0, -1, -1),
               'down': (0, 1, 1, self.height)}[direction]

        cur_obs = [x for x in self.obstacles if x[var[0]] == self.pos[var[0]]
                   and x[var[1]] * var[2] > self.pos[var[1]] * var[2]]
        cur_obs.sort(key=lambda x: x[var[1]] * var[2])
        if len(cur_obs) == 0:  # Guard will pass out of the area.
            stop = var[3]
            self.go = False
        else:
            stop = cur_obs[0][var[1]]
        # Add the new visits
        if direction == 'right':
            new = set((x, self.pos[1]) for x in range(self.pos[0], stop))
            self.pos = (stop - 1, self.pos[1])
        elif direction == 'up':
            new = set((self.pos[0], x) for x in range(self.pos[1], stop, -1))
            self.pos = (self.pos[0], stop + 1)
        elif direction == 'left':
            new = set((x, self.pos[1]) for x in range(self.pos[0], stop, -1))
            self.pos = (stop + 1, self.pos[1])
        else:
            new = set((self.pos[0], x) for x in range(self.pos[1], stop))
            self.pos = (self.pos[0], stop - 1)

        self.visits[direction] = self.visits[direction].union(new)

    def route(self, starting_direction: str):
        """Moves the guard in a starting direction and then rotates clockwise
        until the guard cannot move any further."""
        directions = ['right', 'down', 'left', 'up']
        i = directions.index(starting_direction)
        while self.go:
            self.move(directions[i])
            i = (i + 1) % len(directions)

    def get_visits(self) -> set[tuple[int, int]]:
        return self.visits['right'].union(self.visits['up'],
                                          self.visits['left'],
                                          self.visits['down'])


def parse(input_string: str) -> tuple[int,
                                      int,
                                      tuple[int, int],
                                      list[tuple[int, int]]]:
    """Parser for the input text."""
    lines = [line for line in input_string.split('\n') if line != '']
    height = len(lines)
    width = len(lines[0])
    obstacles = []
    pos = (0, 0)
    for i, line in enumerate(lines):
        for j, character in enumerate(line):
            if character == '#':
                obstacles.append((j, i))
            elif character == '^':
                pos = (j, i)
    return width, height, pos, obstacles


def main(input_string: str) -> int:
    """Runs the guard class route method."""
    width, height, pos, obstacles = parse(input_string)
    guard = Guard(width, height, pos, obstacles)
    guard.route('up')
    return len(guard.get_visits())


if __name__ == '__main__':
    print(main(sys.stdin.read()))
