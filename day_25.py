import re

INT_RE = re.compile(r'\d+')


def main():
    row, col = map(int, INT_RE.findall(input()))

    print(part_1(row, col))


def part_1(row, col):
    n = 20_151_125

    for _ in range(sum(range(1, row + col)) - row):
        n = n * 252_533 % 33_554_393

    return n


if __name__ == '__main__':
    main()
