import fileinput

THINGS = {'children': 3,
          'cats': 7,
          'samoyeds': 2,
          'pomeranians': 3,
          'akitas': 0,
          'vizslas': 0,
          'goldfish': 5,
          'trees': 3,
          'cars': 2,
          'perfumes': 1}


def main():
    aunts = list(map(parse_aunt, map(str.rstrip, fileinput.input())))

    print(part_1(aunts))
    print(part_2(aunts))


def parse_aunt(raw_aunt):
    _, _, thing_1, count_1, thing_2, count_2, thing_3, count_3 = raw_aunt.split()

    return {thing_1[:-1]: int(count_1[:-1]), thing_2[:-1]: int(count_2[:-1]), thing_3[:-1]: int(count_3)}


def part_1(aunts):
    return next(n for n, aunt in enumerate(aunts, 1) if all(THINGS[thing] == count for thing, count in aunt.items()))


def part_2(aunts):
    for n, aunt in enumerate(aunts, 1):
        ok = True

        for thing, count in aunt.items():
            match thing:
                case 'cats' | 'trees':
                    ok = ok and count > THINGS[thing]
                case 'pomeranians' | 'goldfish':
                    ok = ok and count < THINGS[thing]
                case _:
                    ok = ok and count == THINGS[thing]

        if ok:
            return n


if __name__ == '__main__':
    main()
