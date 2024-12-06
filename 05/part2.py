"""Day 5: Print Queue, Part 2
"""

import sys
from part1 import parse


def order_rules(rules: list[tuple[int, ...]]) -> dict[int, int]:
    """Returns an ordering dictionary based on how many times a page appears
    in the second position.

    >>> rules = [(1, 3), (2, 3), (1, 2)]
    >>> order_rules(rules)
    {2: 1, 3: 2}
    """
    second_pages = [x[1] for x in rules]
    unique_pages = set(second_pages)
    page_orders = {}
    for page in unique_pages:
        page_orders[page] = second_pages.count(page)
    return page_orders


def main(input_string: str) -> int:
    """Adds up the middle page number of all page lists that don't conform to
    the rules list provided after being ordered correctly. Rules are in the
    form of tuples where the first page number must come before the second.

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
    123
    """
    rules, pages_list = parse(input_string)

    total = 0

    for pages in pages_list:
        flag = False
        relevant_rules = [x for x in rules if x[0] in pages and x[1] in pages]
        for rule in relevant_rules:
            if pages.index(rule[0]) > pages.index(rule[1]):
                flag = True
                break

        if flag:
            page_orders = order_rules(relevant_rules)
            sorted_pages = sorted(pages, key=lambda x:page_orders.get(x, 0))
            total += sorted_pages[len(pages) // 2]

    return total


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(main(sys.stdin.read()))
