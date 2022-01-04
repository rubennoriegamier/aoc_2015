import fileinput
import re
from itertools import accumulate, chain, cycle, islice, repeat

INT_RE = re.compile(r'\d+')


def main():
    reindeer = list(map(parse_reindeer, fileinput.input()))

    print(part_1(reindeer, 2_503))
    print(part_2(reindeer, 2_503))


def parse_reindeer(raw_reindeer):
    return tuple(map(int, INT_RE.findall(raw_reindeer)))


def part_1(reindeer, seconds):
    return max(seconds // (fly_for + rest_for) * speed * fly_for + min(fly_for, seconds % (fly_for + rest_for)) * speed
               for speed, fly_for, rest_for in reindeer)


def part_2(reindeer, seconds):
    points = [0 for _ in reindeer]

    for progress in islice(zip(*(accumulate(cycle(chain(repeat(speed, fly_for), repeat(0, rest_for))))
                                 for speed, fly_for, rest_for in reindeer)), seconds):
        lead_kms = max(progress)

        for idx, kms in enumerate(progress):
            if kms == lead_kms:
                points[idx] += 1

    return max(points)


if __name__ == '__main__':
    main()
