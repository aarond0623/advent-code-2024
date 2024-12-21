"""Day 16: Reindeer Maze, Part 1

Implements Dijkstra's algortihm to find the most cost-effective path.
"""

from sys import stdin
from heapq import heappush, heappop
import numpy as np
from numpy.typing import NDArray


def parse(input_string: str) -> tuple[NDArray[np.str_],
                                      tuple[int, int],
                                      tuple[int, int]]:
    """Parses the input string into a maze and its start and end coordinates.
    """
    maze = np.array([list(line) for line in input_string.splitlines()])
    start, end = (0, 0), (0, 0)
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == 'S':
                start = (r, c)
            elif cell == 'E':
                end = (r, c)
    return maze, start, end


def dijkstra(maze: NDArray[np.str_],
             start: tuple[int, int],
             end: tuple[int, int]) -> int:
    """Finds the most cost-effective path in the maze and returns that cost."""
    height, width = maze.shape
    # Queue contains cost, position, and offset (i.e. direction)
    queue: list[tuple[int, tuple[int, int], tuple[int, int]]] = []
    visited = set()

    # Initial position and direction:
    heappush(queue, (0, start, (0, 1)))

    while queue:
        cost, coord, offset = heappop(queue)

        if coord == end:
            return cost

        if (coord, offset) in visited:
            continue
        visited.add((coord, offset))

        # For any offset (x, y), 90 degree turns are (y, -x) and (-y, x)
        for new_offset in [offset,
                           (offset[1], -offset[0]),
                           (-offset[1], offset[0])]:
            if new_offset == offset:
                new_coord = (coord[0] + offset[0], coord[1] + offset[1])
                new_cost = cost + 1
            else:
                new_coord = coord
                new_cost = cost + 1000

            if (0 <= new_coord[0] < height and
                    0 <= new_coord[1] < width and
                    maze[new_coord] != '#'):
                heappush(queue, (new_cost, new_coord, new_offset))
    return 0


def tests():
    """Tests for this module."""
    input_string = '''\
    ###############
    #.......#....E#
    #.#.###.#.###.#
    #.....#.#...#.#
    #.###.#####.#.#
    #.#.#.......#.#
    #.#.#####.###.#
    #...........#.#
    ###.#.#####.#.#
    #...#.....#.#.#
    #.#.#.###.#.#.#
    #.....#...#.#.#
    #.###.#.#.#.#.#
    #S..#.....#...#
    ###############'''.replace(' ', '')

    maze, start, end = parse(input_string)
    assert dijkstra(maze, start, end) == 7036

    input_string = '''\
    #################
    #...#...#...#..E#
    #.#.#.#.#.#.#.#.#
    #.#.#.#...#...#.#
    #.#.#.#.###.#.#.#
    #...#.#.#.....#.#
    #.#.#.#.#.#####.#
    #.#...#.#.#.....#
    #.#.#####.#.###.#
    #.#.#.......#...#
    #.#.###.#####.###
    #.#.#...#.....#.#
    #.#.#.#####.###.#
    #.#.#.........#.#
    #.#.#.#########.#
    #S#.............#
    #################'''.replace(' ', '')

    maze, start, end = parse(input_string)
    assert dijkstra(maze, start, end) == 11048


def main(input_string: str) -> int:
    """Finds the cost of the optimal path in a maze string."""
    maze, start, end = parse(input_string)
    return dijkstra(maze, start, end)


if __name__ == '__main__':
    tests()
    print(main(stdin.read()))
