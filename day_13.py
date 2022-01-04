import fileinput
from collections import Counter
from itertools import chain, pairwise, permutations
from operator import itemgetter


def main():
    happiness_relations = parse_happiness_relations(map(str.rstrip, fileinput.input()))

    print(part_1(happiness_relations))
    print(part_2(happiness_relations))


def parse_happiness_relations(raw_happiness_relations):
    happiness_relations = Counter()

    for name_1, _, sign, happiness, *_, name_2 in map(str.split, map(itemgetter(slice(0, -1)),
                                                                     raw_happiness_relations)):
        happiness = int(happiness) if sign == 'gain' else -int(happiness)
        happiness_relations[name_1, name_2] += happiness
        happiness_relations[name_2, name_1] += happiness

    return happiness_relations


def part_1(happiness_relations):
    names = list(set(chain.from_iterable(happiness_relations)))

    return max(sum(map(happiness_relations.get, pairwise(chain([names[0]], permutation, [names[0]]))))
               for permutation in permutations(names[1:]))


def part_2(happiness_relations):
    names = set(chain.from_iterable(happiness_relations))

    return max(sum(map(happiness_relations.get, pairwise(permutation))) for permutation in permutations(names))


if __name__ == '__main__':
    main()
