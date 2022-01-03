import fileinput
import re
from functools import partial
from itertools import chain, starmap
from operator import add, sub

SCAPED_RE = re.compile(r'\\\\|\\"|\\x[0-9a-f]{2}')


def main():
    strings = list(map(str.rstrip, fileinput.input()))

    print(part_1(strings))
    print(part_2(strings))


def part_1(strings):
    # noinspection PyTypeChecker
    return sum(map(partial(add, 1),
                   starmap(sub, map(re.Match.span,
                                    chain.from_iterable(map(SCAPED_RE.finditer, strings)))))) * -1 + len(strings) * 2


def part_2(strings):
    return sum(map(r'\"'.__contains__, chain.from_iterable(strings))) + len(strings) * 2


if __name__ == '__main__':
    main()
