from itertools import accumulate


def main():
    parenthesis = input()

    print(part_1(parenthesis))
    print(part_2(parenthesis))


def part_1(parenthesis):
    return sum(map({'(': 1, ')': -1}.get, parenthesis))


def part_2(parenthesis):
    return next(idx for idx, floor in enumerate(accumulate(map({'(': 1, ')': -1}.get, parenthesis)), 1) if floor < 0)


if __name__ == '__main__':
    main()
