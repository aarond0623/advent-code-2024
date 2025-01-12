"""Day 18: RAM Run, Part 2"""

from sys import stdin
import part1


def find_blockage(size: int, blocks: list[tuple[int, int]]) -> tuple[int, int]:
    """Finds the first block that will make it impossible to navigate the maze
    using a binary search.
    """
    low = 0
    high = len(blocks) - 1
    path = 0
    while low <= high:
        mid = (low + high) // 2
        maze = part1.create_maze(size, blocks[:mid + 1])
        path = part1.dijkstra(maze, (0, 0), (size - 1, size - 1))

        if path > 0:
            low = mid + 1
        else:
            high = mid - 1

    return blocks[low]


def tests():
    """Tests for this module."""
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
    1,2
    5,5
    2,5
    6,5
    1,4
    0,4
    6,4
    1,1
    '''.replace(' ', '')
    blocks = part1.parse(input_string)
    maze = part1.create_maze(7, blocks)
    assert part1.dijkstra(maze, (0, 0), (6, 6)) > 0

    maze[(6, 1)] = False
    assert part1.dijkstra(maze, (0, 0), (6, 6)) == 0

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
    1,2
    5,5
    2,5
    6,5
    1,4
    0,4
    6,4
    1,1
    6,1
    1,0
    0,5
    1,6
    2,0
    '''.replace(' ', '')
    blocks = part1.parse(input_string)
    assert find_blockage(7, blocks) == (6, 1)


def main(input_string: str) -> tuple[int, int]:
    """Finds the block that prevents passage in the maze."""
    blocks = part1.parse(input_string)
    return find_blockage(71, blocks)


if __name__ == '__main__':
    tests()
    block = main(stdin.read())
    print(f"{block[0]},{block[1]}")
