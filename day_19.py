import re
from operator import itemgetter
from os import linesep
from random import shuffle
from sys import stdin


def main():
    raw_replacements, molecule = stdin.read().rstrip().split(linesep * 2)
    replacements = parse_replacements(raw_replacements)

    print(part_1(replacements, molecule))
    print(part_2(replacements, molecule))


def parse_replacements(raw_replacements):
    return list(map(itemgetter(0, 2), map(str.split, raw_replacements.split(linesep))))


def part_1(replacements, molecule):
    # noinspection PyTypeChecker
    return len({f'{molecule[:start]}{new_value}{molecule[stop:]}'
                for old_value, new_value in replacements
                for start, stop in map(re.Match.span, re.finditer(old_value, molecule))})


def part_2(replacements, molecule):
    replacements = [(re.compile(old_value), new_value) for new_value, old_value in replacements]

    # Testing random decompositions :P
    while True:
        shuffle(replacements)
        molecule_ = molecule
        count = 0

        while molecule_ != 'e':
            for old_value_re, new_value in replacements:
                molecule_, subs, = old_value_re.subn(new_value, molecule_)

                if subs > 0:
                    count += subs
                    break
            else:
                break
        else:
            return count


if __name__ == '__main__':
    main()
