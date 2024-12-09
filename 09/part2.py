"""Day 9: Disk Fragmenter, Part 2
"""

from sys import stdin
from part1 import map_disk


def transform_filesystem(slices: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Transforms a filesystem in the following way:

    Starting with files furthest to the right, try to find continguous free
    space to place it. If no such free space exists, proceed to the next file.
    For example, the following filesystem would be transformed as shown:

    00...111...2...333.44.5555.6666.777.888899 -- Start
    0099.111...2...333.44.5555.6666.777.8888.. -- Move 9s
    0099.1117772...333.44.5555.6666.....8888.. -- 8s can't move. 7s can.
    0099.111777244.333....5555.6666.....8888.. -- 6s and 5s can't move. 4s can.
    00992111777.44.333....5555.6666.....8888.. -- 3s can't move. 2 can.

    The return value is a list of lists of slices, where the index of each list
    corresponds to the file ID.
    """
    new_slices = slices
    free_space = [(x[0][1], x[1][0]) for x in zip(slices, slices[1:])
                  if x[0][1] != x[1][0]]
    for i, file in reversed(list(enumerate(slices))):
        filesize = file[1] - file[0]
        for j, space in enumerate(free_space):
            if space[0] > file[0]:
                break
            if space[1] - space[0] >= filesize:
                new_slices[i] = (space[0], space[0] + filesize)
                free_space[j] = (space[0] + filesize, space[1])
                break
    return new_slices


def calculate_checksum(filesystem: list[tuple[int, int]]) -> int:
    """Calculates the filesystem checksum by multiplying the file index by the
    current position in the filesystem for each file."""
    total = 0
    for i, file in enumerate(filesystem):
        total += sum(i * x for x in range(*file))
    return total


def tests():
    """Tests for this module."""
    input_test = "2333133121414131402"
    input_test = [int(x) for x in input_test]
    expected = [(0, 2), (5, 8), (4, 5), (15, 18), (12, 14), (22, 26),
                (27, 31), (8, 11), (36, 40), (2, 4)]
    filesystem = transform_filesystem(map_disk(input_test))
    assert filesystem == expected

    assert calculate_checksum(filesystem) == 2858


def main():
    """Print the filesystem checksum based on stdin input."""
    disk = [int(x) for x in stdin.read().splitlines()[0]]
    print(calculate_checksum(transform_filesystem(map_disk(disk))))


if __name__ == '__main__':
    tests()
    main()
