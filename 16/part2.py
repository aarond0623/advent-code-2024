"""Day 16: Reindeer Maze, Part 2

Implements Dijkstra's algortihm to find the most cost-effective path and counts
all cells part of an optimal path.

Much credit to HyperNeutrino (https://www.youtube.com/watch?v=BJhpteqlVPM) for
showing how to adapt the original Dijkstra's algorithm to count all cells.
"""

from sys import stdin
from collections import deque
from heapq import heappush, heappop
import numpy as np
from numpy.typing import NDArray
from part1 import parse


def dijkstra(maze: NDArray[np.str_],
             start: tuple[int, int],
             end: tuple[int, int]) -> int:
    """Finds the most cost-effective path in the maze and returns that cost."""
    height, width = maze.shape
    # Queue contains cost, position, and offset (i.e. direction)
    queue: list[tuple[float, tuple[int, int], tuple[int, int]]] = []
    best_cost = float('inf')
    # Keep track of the lowest cost to get to each position
    lowest_cost = {(start, (0, 1)): 0.0}
    # Backtrack map
    backtrack: dict[tuple[tuple[int, int], tuple[int, int]],
                    set[tuple[tuple[int, int], tuple[int, int]]]] = {}
    end_states = set()

    # Initial position and direction:
    heappush(queue, (0.0, start, (0, 1)))

    while queue:
        cost, coord, offset = heappop(queue)

        if cost > lowest_cost.get((coord, offset), float('inf')):
            continue

        if coord == end:
            if cost > best_cost:
                break
            best_cost = cost
            end_states.add((coord, offset))

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
                l_cost = lowest_cost.get((new_coord, new_offset), float('inf'))
                if new_cost > l_cost:
                    continue
                if new_cost < l_cost:
                    backtrack[(new_coord, new_offset)] = set()
                    lowest_cost[(new_coord, new_offset)] = new_cost
                backtrack[(new_coord, new_offset)].add((coord, offset))
                heappush(queue, (new_cost, new_coord, new_offset))

    states = deque(end_states)
    seen = set(end_states)

    while states:
        state = states.popleft()
        for last in backtrack.get(state, []):
            if last in seen:
                continue
            seen.add(last)
            states.append(last)

    return len({x for x, _ in seen})



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
    assert dijkstra(maze, start, end) == 45

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
    assert dijkstra(maze, start, end) == 64


def main(input_string: str) -> int:
    """Finds the cost of the optimal path in a maze string."""
    maze, start, end = parse(input_string)
    return dijkstra(maze, start, end)


if __name__ == '__main__':
    tests()
    print(main(stdin.read()))
