"""Day 10: Hoof It, Part 1
"""

from sys import stdin
import numpy as np


class TopoMap:
    """Class for the topographic map."""
    def __init__(self, input_string: str):
        lines = input_string.splitlines()
        self.topomap = np.array([[int(x) for x in line] for line in lines])
        self.shape = self.topomap.shape
        self.height, self.width = self.shape
        self.routemap = np.zeros(self.shape, dtype=int)
        self.zeros = [(int(i), int(j)) for i, j in
                      np.column_stack(np.where(self.topomap == 0))]
        self.score = 0

    def get_neighbors(self, coord: tuple[int, int]) -> list[tuple[int, int]]:
        """Returns valid neighbor coordinates for a specified coordinate."""
        neighbors = []
        for offset in ((0, 1), (-1, 0), (0, -1), (1, 0)):
            n = tuple(map(sum, zip(coord, offset)))
            if (0 <= n[0] < self.height) and (0 <= n[1] < self.width):
                neighbors.append(n)
        return neighbors

    def update_routemap(self, coord: tuple[int, int]) -> int:
        """Updates the routemap, which serves as the cache for the routes. Each
        cell is equal to the number of 9s that cell can reach.
        """

        # Reached destination
        if self.topomap[coord] == 9 and self.routemap[coord] == 0:
            self.routemap[coord] = 1
            return 1
        # We've already checked this location
        if self.routemap[coord] != 0:
            # THIS IS THE ONLY LINE CHANGED FROM PART 1!!!
            return self.routemap[coord]

        n = self.get_neighbors(coord)
        n = [x for x in n if self.topomap[x] == self.topomap[coord] + 1]

        # This is a dead end:
        if len(n) == 0:
            return 0
        if self.topomap[coord] == 0:
            self.routemap = np.zeros(self.shape, dtype=int)
            self.routemap[coord] += sum(self.update_routemap(x) for x in n)
            self.score += self.routemap[coord]
        self.routemap[coord] += sum(self.update_routemap(x) for x in n)
        return self.routemap[coord]


def tests():
    """Tests for the module."""
    input_test = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''
    t = TopoMap(input_test)
    for zero in t.zeros:
        t.update_routemap(zero)
    assert t.score == 81


def main(input_string: str) -> int:
    """Calculates the total score for the topographic map."""
    t = TopoMap(input_string)
    for zero in t.zeros:
        t.update_routemap(zero)
    return t.score


if __name__ == '__main__':
    tests()
    print(main(stdin.read()))
