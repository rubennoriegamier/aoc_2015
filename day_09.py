import fileinput
from collections import defaultdict
from sys import maxsize


def main():
    distances = parse_distances(map(str.rstrip, fileinput.input()))

    print(part_1(distances))
    print(part_2(distances))


def parse_distances(raw_distances):
    distances = defaultdict(list)

    for location_a, _, location_b, _, distance in map(str.split, raw_distances):
        distances[location_a].append((location_b, int(distance)))
        distances[location_b].append((location_a, int(distance)))

    return distances


def part_1(distances):
    traveled = set()

    def solve(location, total_distance=0, min_distance=maxsize):
        if location in traveled or total_distance >= min_distance:
            return min_distance

        traveled.add(location)
        if len(traveled) < len(distances):
            for next_location, distance in distances[location]:
                min_distance = solve(next_location, total_distance + distance, min_distance)
        else:
            min_distance = total_distance
        traveled.discard(location)

        return min_distance

    return min(map(solve, distances))


def part_2(distances):
    traveled = set()

    def solve(location, total_distance=0):
        if location in traveled:
            return 0

        traveled.add(location)
        if len(traveled) < len(distances):
            total_distance = max(solve(next_location, total_distance + distance)
                                 for next_location, distance in distances[location])
        traveled.discard(location)

        return total_distance

    return max(map(solve, distances))


if __name__ == '__main__':
    main()
