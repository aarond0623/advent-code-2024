"""Day 18: RAM Run, Part 1"""

from sys import stdin
from heapq import heappush, heappop
import numpy as np
from numpy.typing import NDArray


def parse(input_string: str) -> list[tuple[int, int]]:
    """Parses a string of comma-separate integers into tuples."""
    blocks = []
    for line in input_string.splitlines():
        nums = [int(x) for x in line.split(',')]
        blocks.append((nums[0], nums[1]))
    return blocks


def create_maze(size: int, blocks: list[tuple[int, int]]) -> NDArray[np.bool_]:
    """Creates a numpy array of booleans representing a maze, with a list of
    blocks representing walls in the maze.
    """
    maze = np.full((size, size), True)
    for block in blocks:
        maze[block] = False
    return maze


def dijkstra(maze: NDArray[np.bool_],
             start: tuple[int, int],
             end: tuple[int, int]) -> int:
    """Finds the shortest path through the maze and returns the length."""
    queue: list[tuple[int, tuple[int, int]]] = []
    visited = set()

    # Initial position
    heappush(queue, (0, start))

    while queue:
        cost, coord = heappop(queue)

        if coord == end:
            return cost

        if coord in visited:
            continue
        visited.add(coord)

        for offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_coord = (coord[0] + offset[0], coord[1] + offset[1])

            if (0 <= new_coord[0] < maze.shape[0] and
                    0 <= new_coord[1] < maze.shape[1] and
                    maze[new_coord]):
                heappush(queue, (cost + 1, new_coord))
    return 0


def tests():
    """Tests for this module."""
    input_string = '''\
    5,4
    4,2
    4,5
    '''.replace(' ', '')

    assert parse(input_string) == [(5, 4), (4, 2), (4, 5)]

    input_string = '''\
    5,4
    4,2
    4,5
    3,0
    2,1
    6,3
    2,4
    1,5
    0,6
    3,3
    2,6
    5,1
    '''.replace(' ', '')

    maze = create_maze(7, parse(input_string))
    assert dijkstra(maze, (0, 0), (6, 6)) == 22


def main(input_string: str) -> int:
    """Finds the length of the optimal path through the maze."""
    blocks = parse(input_string)[:1024]
    maze = create_maze(71, blocks)
    return dijkstra(maze, (0, 0), (70, 70))  # Nice


if __name__ == '__main__':
    tests()
    print(main(stdin.read()))
