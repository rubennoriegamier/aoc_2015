import fileinput
from collections import deque
from functools import partial, reduce
from itertools import accumulate, chain
from operator import mul


def main():
    weights = list(map(int, fileinput.input()))

    print(part_1(weights))
    print(part_2(weights))


def subsets_that_add_up_to_objetive(objetive, numbers, size=None):
    numbers = sorted((number,) for number in numbers)
    subsets = deque()
    subsets.append(())

    for number in numbers:
        for _ in range(len(subsets)):
            subset = subsets.popleft()
            subset_sum = sum(subset)

            if subset_sum == objetive:
                if size is None or len(subset) == size:
                    yield subset
            elif subset_sum < objetive and (size is None or len(subset) < size):
                subsets.append(subset)
                subsets.append(subset + number)
    yield from (subset for subset in subsets if (size is None or len(subset) == size) and sum(subset) == objetive)


def quantum_entanglement(subset):
    return reduce(mul, subset)


def part_1(weights):
    group_weight = sum(weights) // 3

    min_size = next(min_size for min_size, subset_sum in enumerate(accumulate(weights[::-1]), 1)
                    if subset_sum >= group_weight)
    for subset in chain.from_iterable(map(partial(sorted, key=quantum_entanglement),
                                          map(partial(subsets_that_add_up_to_objetive, group_weight, weights),
                                              range(min_size, len(weights) - 1)))):
        weights = (weight for weight in weights if weight not in subset)

        if any(subsets_that_add_up_to_objetive(group_weight, weights)):
            return quantum_entanglement(subset)


def part_2(weights):
    group_weight = sum(weights) // 4

    min_size_1 = next(min_size for min_size, subset_sum in enumerate(accumulate(weights[::-1]), 1)
                      if subset_sum >= group_weight)
    for subset_1 in chain.from_iterable(map(partial(sorted, key=quantum_entanglement),
                                            map(partial(subsets_that_add_up_to_objetive, group_weight, weights),
                                                range(min_size_1, len(weights) - 2)))):
        weights_2 = [weight for weight in weights if weight not in subset_1]
        min_size_2 = next(min_size for min_size, subset_sum in enumerate(accumulate(weights_2[::-1]), 1)
                          if subset_sum >= group_weight)

        for subset_2 in chain.from_iterable(map(partial(sorted, key=quantum_entanglement),
                                                map(partial(subsets_that_add_up_to_objetive, group_weight, weights_2),
                                                    range(min_size_2, len(weights_2) - 1)))):
            weights_3 = (weight for weight in weights if weight not in subset_2)

            if any(subsets_that_add_up_to_objetive(group_weight, weights_3)):
                return quantum_entanglement(subset_1)


if __name__ == '__main__':
    main()
