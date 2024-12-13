"""Day 12: Garden Groups, Part 1
"""

from sys import stdin
import numpy as np
from part1 import Field


class FieldPart2(Field):
    """A class to represent the field of crops."""
    def calculate(self) -> int:
        """Calculates the total cost of fencing."""
        # West, Northwest, North, and northeast
        offsets = ((0, -1), (-1, -1), (-1, 0), (-1, 1))
        rows, cols = self.field.shape

        for (r, c), crop in np.ndenumerate(self.field):
            root = self.find_root((r, c))
            self.area[root] = self.area.get(root, 0) + 1
            self.perimeter[root] = self.perimeter.get(root, 0)

            neighbors = []
            for dr, dc in offsets:
                nr, nc = r + dr, c + dc
                if (not (0 <= nr < rows and 0 <= nc < cols) or
                        self.field[nr, nc] != crop):
                    neighbors.append(0)
                else:
                    neighbors.append(1)
            # I couldn't think of a way to easily test this except to hardcode
            # the different combinations in.
            if neighbors in [[0, 0, 0, 0],
                             [0, 1, 0, 0],
                             [0, 0, 0, 1],
                             [0, 1, 0, 1],
                             [0, 1, 1, 1]]:
                self.perimeter[root] += 4
            elif neighbors in [[1, 1, 0, 0],
                               [0, 1, 1, 0],
                               [1, 1, 0, 1],
                               [0, 0, 1, 1]]:
                self.perimeter[root] += 2
            elif neighbors in [[1, 0, 1, 0],
                               [1, 1, 1, 0]]:
                self.perimeter[root] -= 2

        return sum(self.area[x] * self.perimeter[x] for x in self.area)


def tests():
    """Tests for this module."""
    input_string = "AAAA\nBBCD\nBBCC\nEEEC"
    field = FieldPart2(input_string)
    field.group_field()
    assert field.calculate() == 80
    input_string = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
    field = FieldPart2(input_string)
    field.group_field()
    assert field.calculate() == 436


def main(input_string: str) -> int:
    """Calculates the total cost for the input string."""
    field = FieldPart2(input_string)
    field.group_field()
    return field.calculate()


if __name__ == '__main__':
    tests()
    print(main(stdin.read()))
