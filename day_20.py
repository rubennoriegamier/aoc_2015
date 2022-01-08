from itertools import count

import numpy as np


def main():
    min_presents = int(input())

    print(part_1(min_presents))
    print(part_2(min_presents))


def part_1(min_presents):
    min_presents = min_presents // 10
    presents = np.ones(min_presents, np.int32)

    for elf in count(2):
        presents[elf - 1::elf] += elf
        if presents[elf - 1] >= min_presents:
            return elf


def part_2(min_presents):
    min_presents = min_presents // 11
    presents = np.zeros(min_presents, np.int32)

    for elf in count(1):
        presents[elf - 1:elf * 50:elf] += elf
        if presents[elf - 1] >= min_presents:
            return elf


if __name__ == '__main__':
    main()
