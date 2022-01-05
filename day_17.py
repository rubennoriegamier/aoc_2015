import fileinput
from functools import cache, partial
from itertools import takewhile
from operator import ge
from sys import maxsize


def main():
    containers = list(map(int, fileinput.input()))

    print(part_1(containers, 150))
    print(part_2(containers, 150))


def part_1(containers, liters, max_containers=maxsize):
    @cache
    def solve(containers_, liters_, max_containers_):
        combinations = 0
        containers_ = tuple(takewhile(partial(ge, liters_), containers_))

        for idx, container in enumerate(containers_):
            if container < liters_:
                if max_containers_ >= 2:
                    combinations += solve(containers_[idx + 1:], liters_ - container, max_containers_ - 1)
            else:
                combinations += 1

        return combinations

    return solve(tuple(sorted(containers)), liters, max_containers)


def part_2(containers, liters):
    @cache
    def solve(containers_, liters_):
        min_containers = maxsize
        containers_ = tuple(takewhile(partial(ge, liters_), containers_))

        for idx, container in enumerate(containers_):
            if container < liters_:
                min_containers = min(min_containers, solve(containers_[idx + 1:], liters_ - container) + 1)
            else:
                return 1

        return min_containers

    return part_1(containers, liters, solve(tuple(sorted(containers)), liters))


if __name__ == '__main__':
    main()
