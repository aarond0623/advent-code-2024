"""Day 9: Disk Fragmenter, Part 1
"""

from sys import stdin


def map_disk(sequence: list[int]) -> list[tuple[int, int]]:
    """Takes as input a list of integers representing the disk map. Disk maps
    are represented by digits that alternately represent the size of a file and
    the size of free space on the drive. For example, in the following disk
    map, files are represented by index and space is represented by .

    Disk map: [1, 2, 3, 4, 5]
    Files:    0..111....22222

    The function returns a list of tuples representing slices for files. In the
    example above, the function would return:

    [(0, 1), (3, 6), (10, 15)]
    """
    index = 0
    slices = []
    for (i, digit) in enumerate(sequence):
        if i % 2 == 0:  # This is a file
            slices.append((index, index+digit))
        index += digit
    return slices


def transform_filesystem(slices: list[tuple[int, int]]) -> list[list[tuple[int, int]]]:
    """Transforms a filesystem in the following way:

    All free space at the beginning of the disk is filled with data from the
    end of the filesystem. For example, the file system below would be
    transformed as shown:

    0..111....22222
    022111222......

    The return value is a list of lists of slices, where the index of each list
    corresponds to the file ID. The above would be returned like this:

    [[(0, 1)], [(3, 6)], [(1, 3), (6, 9)]]
    """
    new_slices: list[list[tuple[int, int]]] = [[] for _ in slices]
    free_space = [(x[0][1], x[1][0]) for x in zip(slices, slices[1:])
                  if x[0][1] != x[1][0]]
    i = 0
    j = len(slices) - 1
    while i < len(free_space) and free_space[i][0] < slices[j][1]:
        s1, s2 = free_space[i]
        f1, f2 = slices[j]

        if (s2 - s1) == (f2 - f1):
            new_slices[j].append((s1, s2))
            j -= 1
            i += 1
        if (s2 - s1) > (f2 - f1):
            new_slices[j].append((s1, s1 + f2 - f1))
            j -= 1
            free_space[i] = (s1 + f2 - f1, s2)
        if (s2 - s1) < (f2 - f1):
            new_slices[j].append((s1, s2))
            slices[j] = (f1, f2 - (s2 - s1))
            i += 1

    for i in range(j):
        new_slices[i].append(slices[i])

    # Handle the in-progress slice:
    if new_slices[j] != [] and new_slices[j][-1][1] == slices[j][0]:
        new_slices[j][-1] = (new_slices[j][-1][0], slices[j][1])
    else:
        new_slices[j].append(slices[j])

    return new_slices


def calculate_checksum(filesystem: list[list[tuple[int, int]]]) -> int:
    """Calculates the filesystem checksum by multiplying the file index by the
    current position in the filesystem for each file."""
    total = 0
    for i, files in enumerate(filesystem):
        for file in files:
            total += sum(i * x for x in range(*file))
    return total


def tests():
    """Tests for this module."""
    assert map_disk([1, 2, 3, 4, 5]) == [(0, 1), (3, 6), (10, 15)]

    input_test = "2333133121414131402"
    input_test = [int(x) for x in input_test]
    expected = [(0, 2), (5, 8), (11, 12), (15, 18), (19, 21), (22, 26),
                (27, 31), (32, 35), (36, 40), (40, 42)]
    assert map_disk(input_test) == expected

    expected = [[(0, 1)], [(3, 6)], [(1, 3), (6, 9)]]
    assert transform_filesystem(map_disk([1, 2, 3, 4, 5])) == expected

    expected = [[(0, 2)],
                [(5, 8)],
                [(11, 12)],
                [(15, 18)],
                [(19, 21)],
                [(22, 26)],
                [(18, 19), (21, 22), (26, 28)],
                [(12, 15)],
                [(4, 5), (8, 11)],
                [(2, 4)]]
    assert transform_filesystem(map_disk(input_test)) == expected

    filesystem = transform_filesystem(map_disk([1, 2, 3, 4, 5]))
    assert calculate_checksum(filesystem) == 60

    filesystem = transform_filesystem(map_disk(input_test))
    assert calculate_checksum(filesystem) == 1928


def main():
    """Print the filesystem checksum based on stdin input."""
    disk = [int(x) for x in stdin.read().splitlines()[0]]
    print(calculate_checksum(transform_filesystem(map_disk(disk))))

if __name__ == '__main__':
    tests()
    main()
