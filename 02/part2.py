"""Day 2: Red-Nosed Reports

This module takes input from stdin in the form of several lists of numbers
organized in rows. It then counts how many rows are considered "safe", where
a safe sequence is one where all elements either increase or decrease by a
maximum of 3. Lists that increase or decrease by more or stay the same are
considered unsafe.

Further, an unsafe list can be made safe by removing at most one element and
creating a resulting list which is safe. (The "Problem Dampener").
"""

import sys
from part1 import parse


def check_report(report: list[int]) -> int:
    """Determines whether a sequence is safe (only increases or decreases by 3
    or less.) If a sequence is safe, the function returns -1. If unsafe, it
    returns the index at which the safety error occurred.

    >>> check_report([7, 6, 4, 2, 1])
    -1
    >>> check_report([1, 2, 7, 8, 9])
    1
    >>> check_report([1, 3, 2, 4, 5])
    1
    >>> check_report([1, 2, 4, 5])
    -1
    >>> check_report([8, 6, 4, 4, 1])
    2
    >>> check_report([8, 6, 4, 1])
    -1
    """
    # If unsafe, return False immediately.
    delta = report[1] - report[0]
    if abs(delta) > 3 or delta == 0:
        return 0

    # Determine whether the sequence is increasing or decreasing.
    sign = delta / abs(delta)

    for i in range(2, len(report)):
        delta = int((report[i] - report[i-1]) * sign)
        if delta > 3 or delta <= 0:
            return i - 1

    return -1


def main(input_string: str) -> int:
    """Calculate the number of safe reports in a list, given the Problem
    Dampener.

    >>> input_string = '''\\
    ... 7 6 4 2 1
    ... 1 2 7 8 9
    ... 9 7 6 2 1
    ... 1 3 2 4 5
    ... 8 6 4 4 1
    ... 1 3 6 7 9'''
    >>> main(input_string)
    4
    """

    reports = parse(input_string)

    count = 0

    for report in reports:
        result = check_report(report)

        # First failure
        if result != -1:
            # Remove elements around failure and generate new reports
            new_reports = []
            for i in range(-1, 2):
                new_reports.append(report[:result+i] + report[result+i+1:])

            # If any new report succeeds, break and consider it safe
            for new_report in new_reports:
                if check_report(new_report) == -1:
                    count += 1
                    break
        else:
            count += 1

    return count


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(main(sys.stdin.read()))
