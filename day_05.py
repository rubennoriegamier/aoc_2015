import fileinput
import re
from itertools import pairwise, starmap
from operator import eq

PART_2_FIRST_RULE_RE = re.compile(r'(..).*\1')
PART_2_SECOND_RULE_RE = re.compile(r'(.).\1')


def main():
    strings = list(map(str.rstrip, fileinput.input()))

    print(part_1(strings))
    print(part_2(strings))


def part_1(strings):
    return sum(1 for string in strings if
               sum(map('aeiou'.__contains__, string)) >= 3 and
               any(starmap(eq, pairwise(string))) and
               'ab' not in string and 'cd' not in string and 'pq' not in string and 'xy' not in string)


def part_2(strings):
    return sum(1 for _ in filter(PART_2_SECOND_RULE_RE.search, filter(PART_2_FIRST_RULE_RE.search, strings)))


if __name__ == '__main__':
    main()
