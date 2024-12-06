"""Day 5: Print Queue, Part 1
"""

import sys


def parse(input_string: str) -> tuple[list[tuple[int, ...]], list[list[int]]]:
    """Parses a block of text containing the page rules and page sequences and
    returns a tuple with the list of rules, as tuples, and the list of page
    sequences.

    >>> input_string = '''\\
    ... 47|53
    ... 97|13
    ...
    ... 75,47,61,53,29
    ... 97,61,53,29,13'''

    >>> parse(input_string)
    ([(47, 53), (97, 13)], [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13]])
    """
    rules = []
    pages_list = []
    rules_lines, pages_lines = [x.split() for x in input_string.split('\n\n')]

    for line in rules_lines:
        rules.append(tuple(int(x) for x in line.split('|')))

    for line in pages_lines:
        pages_list.append([int(x) for x in line.split(',')])

    return rules, pages_list


def main(input_string: str) -> int:
    """Adds up the middle page number of all page lists that conform to the
    rules list provided. Rules are in the form of tuples where the first page
    number must come before the second.

    >>> input_string = '''\\
    ... 47|53
    ... 97|13
    ... 97|61
    ... 97|47
    ... 75|29
    ... 61|13
    ... 75|53
    ... 29|13
    ... 97|29
    ... 53|29
    ... 61|53
    ... 97|53
    ... 61|29
    ... 47|13
    ... 75|47
    ... 97|75
    ... 47|61
    ... 75|61
    ... 47|29
    ... 75|13
    ... 53|13
    ...
    ... 75,47,61,53,29
    ... 97,61,53,29,13
    ... 75,29,13
    ... 75,97,47,61,53
    ... 61,13,29
    ... 97,13,75,29,47'''

    >>> main(input_string)
    143
    """
    rules, pages_list = parse(input_string)

    total = 0

    for pages in pages_list:
        relevant_rules = [x for x in rules if x[0] in pages and x[1] in pages]
        for rule in relevant_rules:
            if pages.index(rule[0]) > pages.index(rule[1]):
                break
        else:
            total += pages[len(pages) // 2]

    return total


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(main(sys.stdin.read()))
