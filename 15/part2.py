"""Day 15: Warehouse Woes, Part 2

This module simulates a robot moving through a warehouse of boxes. As it moves,
it will push boxes into new positions unless it is blocked by a wall, in which
case it will not move. In this part, boxes are now two cells wide and
represented by '[]'.
"""

from sys import stdin
import numpy as np


class Warehouse:
    """Class for the warehouse."""
    def __init__(self, input_string: str):
        self.wh = np.array([list(line) for line in input_string.splitlines()])
        self.robot = tuple(x[0] for x in np.where(self.wh == '@'))
        self.queue: list[tuple[tuple[int, ...], tuple[int, ...]]] = []

    def move(self, coord: tuple[int, ...], direction: str, i: int = 0):
        """Moves a cell in a given direction if the cell is not blocked."""
        offsets = {'>': (0, 1), '^': (-1, 0), '<': (0, -1), 'v': (1, 0)}
        offset = offsets[direction]
        to_coord = tuple(x + y for x, y in zip(coord, offset))

        if self.wh[coord] == '.':
            return
        if self.wh[coord] == '#':
            self.queue.insert(i, (coord, coord))
            return
        if self.wh[coord] in '[]' and direction in '^v':
            box_offsets = {'[': (0, 1), ']': (0, -1)}
            box_offset = box_offsets[self.wh[coord]]
            pair = tuple(x + y for x, y in zip(coord, box_offset))
            to_coord2 = tuple(x + y for x, y in zip(pair, offset))
            # Checks have to be inserted in a breadth-first manner, so that
            # blocked don't overwrite ones that have not moved yet.
            self.queue.insert(i, (coord, to_coord))
            self.queue.insert(i, (pair, to_coord2))
            pos = len(self.queue)
            self.move(to_coord, direction, pos)
            self.move(to_coord2, direction, pos)
            return
        self.queue.insert(i, (coord, to_coord))
        pos = len(self.queue)
        self.move(to_coord, direction, pos)
        if self.wh[coord] == '@':
            if any(x == y for x, y in self.queue):
                self.queue = []
                return
            self.queue = list(dict.fromkeys(self.queue))
            for q, new_q in self.queue[::-1]:
                self.wh[new_q] = self.wh[q]
                self.wh[q] = '.'
            self.robot = to_coord
            self.wh[to_coord] = '@'
            self.wh[coord] = '.'
            self.queue = []
            return
        return

    def calculate_gps(self) -> int:
        """Calculates the GPS coordinates of all boxes in the warehouse, where
        a GPS coordinate is equal to 100 * y + x.
        """
        gps = 0
        for (y, x), value in np.ndenumerate(self.wh):
            if value == '[':
                gps += 100 * y + x
        return gps

    def __str__(self):
        return '\n'.join(''.join(line) for line in self.wh)


def widen_warehouse(input_string: str) -> str:
    """Widens the warehouse by replacing every # with ##, every . with ..,
    every O with [], and the robot @ with @."""
    input_string = input_string.replace('#', '##')
    input_string = input_string.replace('.', '..')
    input_string = input_string.replace('O', '[]')
    input_string = input_string.replace('@', '@.')
    return input_string


def tests():
    """Tests for this module."""
    input_string = '''##########
    #..O..O.O#
    #......O.#
    #.OO..O.O#
    #..O@..O.#
    #O#..O...#
    #O..O..O.#
    #.OO.O.OO#
    #....O...#
    ##########'''.replace(' ', '')
    input_string = widen_warehouse(input_string)

    moves = '''
    <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
    vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
    ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
    <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
    ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
    ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
    >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
    <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
    ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
    v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''

    moves = ''.join(moves.split())

    wh = Warehouse(input_string)
    for move in moves:
        wh.move(wh.robot, move)

    assert wh.calculate_gps() == 9021


def main(input_string: str) -> int:
    """Calculates the GPS value for the given input string."""
    warehouse, moves = input_string.split('\n\n')
    warehouse = widen_warehouse(warehouse)
    moves = ''.join(moves.split())

    wh = Warehouse(warehouse)
    for move in moves:
        wh.move(wh.robot, move)

    return wh.calculate_gps()


if __name__ == '__main__':
    tests()
    print(main(stdin.read()))
