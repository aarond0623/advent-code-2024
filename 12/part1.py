"""Day 12: Garden Groups, Part 1
"""

from sys import stdin
import numpy as np


class Field:
    """A class to represent the field of crops."""
    def __init__(self, input_string: str):
        lines = input_string.splitlines()
        self.field = np.array([list(line) for line in lines])
        self.area: dict[tuple[int, int], int] = {}
        self.perimeter: dict[tuple[int, int], int] = {}
        # Keeps track of the "parent node" for each group, i.e. which cell a
        # cell stems from
        self.parent: dict[tuple[int, int], tuple[int, int]] = {}

    def find_root(self, coord: tuple[int, int]) -> tuple[int, int]:
        """Finds the root of a coordinate."""
        if self.parent[coord] != coord:
            self.parent[coord] = self.find_root(self.parent[coord])
        return self.parent[coord]

    def merge_regions(self, coord1: tuple[int, int], coord2: tuple[int, int]):
        """Merge two groups together by setting their root to be the same."""
        root1 = self.find_root(coord1)
        root2 = self.find_root(coord2)
        if root1 != root2:
            self.parent[root2] = root1

    def group_field(self):
        """Generates groups of crops"""
        directions = ((-1, 0), (0, -1))     # Only check north and west
        for (r, c), crop in np.ndenumerate(self.field):
            coord = (r, c)
            self.parent[coord] = coord
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nc >= 0:
                    if self.field[nr, nc] == crop:
                        self.merge_regions(coord, (nr, nc))

    def calculate(self) -> int:
        """Calculates the total cost of fencing."""
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        rows, cols = self.field.shape

        for (r, c), crop in np.ndenumerate(self.field):
            root = self.find_root((r, c))
            self.area[root] = self.area.get(root, 0) + 1
            self.perimeter[root] = self.perimeter.get(root, 0)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (not (0 <= nr < rows and 0 <= nc < cols) or
                        self.field[nr, nc] != crop):
                    self.perimeter[root] += 1
        return sum(self.area[x] * self.perimeter[x] for x in self.area)


def tests():
    """Tests for this module."""
    input_string = "AAAA\nBBCD\nBBCC\nEEEC"
    field = Field(input_string)
    field.group_field()
    assert field.calculate() == 140
    input_string = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    field = Field(input_string)
    field.group_field()
    assert field.calculate() == 772


def main(input_string: str) -> int:
    """Calculates the total cost for the input string."""
    field = Field(input_string)
    field.group_field()
    return field.calculate()


if __name__ == '__main__':
    tests()
    print(main(stdin.read()))
