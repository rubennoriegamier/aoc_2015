import json


def main():
    json_ = json.loads(input())

    print(part_1(json_))
    print(part_2(json_))


def part_1(json_):
    if isinstance(json_, int):
        return json_
    if isinstance(json_, list):
        return sum(map(part_1, json_))
    if isinstance(json_, dict):
        return sum(map(part_1, json_.values()))
    return 0


def part_2(json_):
    if isinstance(json_, int):
        return json_
    if isinstance(json_, list):
        return sum(map(part_2, json_))
    if isinstance(json_, dict):
        values = json_.values()

        return 0 if 'red' in values else sum(map(part_2, values))
    return 0


if __name__ == '__main__':
    main()
