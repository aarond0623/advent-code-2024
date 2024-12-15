"""Day 15: Warehouse Woes, Part 1

This module simulates a robot moving through a warehouse of boxes. As it moves,
it will push boxes into new positions unless it is blocked by a wall, in which
case it will not move.
"""

from sys import stdin
import numpy as np


class Warehouse:
    """Class for the warehouse."""
    def __init__(self, input_string: str):
        self.wh = np.array([list(line) for line in input_string.splitlines()])
        self.robot = tuple(x[0] for x in np.where(self.wh == '@'))

    def move(self, coord: tuple[int, ...], direction: str) -> tuple[int, ...]:
        """Moves a cell in a given direction if the cell is not blocked."""
        offsets = {'>': (0, 1), '^': (-1, 0), '<': (0, -1), 'v': (1, 0)}
        offset = offsets[direction]

        if self.wh[coord] == '.':
            return coord
        if self.wh[coord] == '#':
            return tuple(x - y for x, y in zip(coord, offset))
        new_coord = self.move(tuple(x + y for x, y in zip(coord, offset)),
                              direction)
        if new_coord != coord:
            if self.wh[coord] == '@':
                self.robot = new_coord
            self.wh[new_coord] = self.wh[coord]
            self.wh[coord] = '.'
            return coord
        return tuple(x - y for x, y in zip(coord, offset))

    def calculate_gps(self) -> int:
        """Calculates the GPS coordinates of all boxes in the warehouse, where
        a GPS coordinate is equal to 100 * y + x.
        """
        gps = 0
        for (y, x), value in np.ndenumerate(self.wh):
            if value == 'O':
                gps += 100 * y + x
        return gps


def tests():
    """Tests for this module."""
    input_string = '''########
    #..O.O.#
    ##@.O..#
    #...O..#
    #.#.O..#
    #...O..#
    #......#
    ########'''.replace(' ', '')

    moves = '<^^>>>vv<v>>v<<'

    wh = Warehouse(input_string)
    for move in moves:
        wh.move(wh.robot, move)

    assert wh.calculate_gps() == 2028

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

    assert wh.calculate_gps() == 10092


def main(input_string: str) -> int:
    """Calculates the GPS value for the given input string."""
    warehouse, moves = input_string.split('\n\n')
    moves = ''.join(moves.split())

    wh = Warehouse(warehouse)
    for move in moves:
        wh.move(wh.robot, move)
    return wh.calculate_gps()


if __name__ == '__main__':
    tests()
    print(main(stdin.read()))
