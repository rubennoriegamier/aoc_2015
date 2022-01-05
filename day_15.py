import fileinput
import re
from functools import reduce
from operator import itemgetter, mul

INT_RE = re.compile(r'-?\d+')


def main():
    ingredients = list(map(parse_ingredient, fileinput.input()))

    print(part_1(ingredients))
    print(part_2(ingredients))


def parse_ingredient(raw_ingredient):
    return tuple(map(int, INT_RE.findall(raw_ingredient)))


def split_number(number, count):
    if count == 1:
        yield number,
    else:
        for split in range(number + 1):
            for splits in split_number(number - split, count - 1):
                yield (split,) + splits


def part_1(ingredients):
    property_getters = list(map(itemgetter, range(4)))

    return max(reduce(mul, (max(sum(map(mul, distribution, map(property_getter, ingredients))), 0)
                            for property_getter in property_getters))
               for distribution in split_number(100, len(ingredients)))


def part_2(ingredients):
    property_getters = list(map(itemgetter, range(4)))
    calories_getter = itemgetter(4)

    return max(reduce(mul, (max(sum(map(mul, distribution, map(property_getter, ingredients))), 0)
                            for property_getter in property_getters))
               for distribution in split_number(100, len(ingredients))
               if sum(map(mul, distribution, map(calories_getter, ingredients))) == 500)


if __name__ == '__main__':
    main()
