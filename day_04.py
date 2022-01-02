from hashlib import md5
from itertools import count


def main():
    secret = input().rstrip()

    print(part_1(secret))
    print(part_2(secret))


def part_1(secret):
    return next(n for n in count(1) if md5(f'{secret}{n}'.encode()).hexdigest()[:5] == '00000')


def part_2(secret):
    return next(n for n in count(1) if md5(f'{secret}{n}'.encode()).hexdigest()[:6] == '000000')


if __name__ == '__main__':
    main()
