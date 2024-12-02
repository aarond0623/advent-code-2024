"""Day 2: Red-Nosed Reports

This module takes input from stdin in the form of several lists of numbers
organized in rows. It then calculates counts how many rows are considered
"safe", where a safe sequence is one where all elements either increase or
decrease by a maximum of 3. Lists that increase or decrease by more or stay the
same are considered unsafe."""

import sys


def parse(input_string: str) -> list[list[int]]:
    """Parses rows of integers into a list of lists."""
    reports = []
    for report in [x.split() for x in input_string.split('\n') if x != '']:
        reports.append([int(x) for x in report])
    return reports


def main(input_string: str) -> int:
    """Calculates the number of safe reports in a list.

    >>> input_string = '''\\
    ... 7 6 4 2 1
    ... 1 2 7 8 9
    ... 9 7 6 2 1
    ... 1 3 2 4 5
    ... 8 6 4 4 1
    ... 1 3 6 7 9'''
    >>> main(input_string)
    2
    """
    reports = parse(input_string)

    count = 0

    for report in reports:
        # If unsafe, break immediately.
        delta = report[1] - report[0]
        if abs(delta) > 3 or delta == 0:
            continue

        # Determine whether the sequence is increasing or decreasing.
        sign = delta / abs(delta)

        safe = True
        for i in range(2, len(report)):
            delta = int((report[i] - report[i - 1]) * sign)
            if delta > 3 or delta <= 0:
                safe = False
                break

        if safe:
            count += 1

    return count


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(main(sys.stdin.read()))
