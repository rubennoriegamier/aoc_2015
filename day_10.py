from itertools import groupby


def main():
    sequence = list(map(int, input()))

    print(part_1_and_2(sequence, 40))
    print(part_1_and_2(sequence, 50))


def next_sequence(sequence):
    for digit, digits in groupby(sequence):
        yield sum(1 for _ in digits)
        yield digit


def part_1_and_2(sequence, times):
    for _ in range(times):
        sequence = next_sequence(sequence)

    return sum(1 for _ in sequence)


if __name__ == '__main__':
    main()
