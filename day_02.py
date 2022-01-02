import fileinput


def main():
    dimensions = list(map(parse_dimensions, fileinput.input()))

    print(part_1(dimensions))
    print(part_2(dimensions))


def parse_dimensions(raw_dimensions):
    return tuple(map(int, raw_dimensions.split('x')))


def part_1(dimensions):
    return sum((a * b + a * c + b * c) * 2 + a * b for a, b, c in map(sorted, dimensions))


def part_2(dimensions):
    return sum(a * 2 + b * 2 + a * b * c for a, b, c in map(sorted, dimensions))


if __name__ == '__main__':
    main()
