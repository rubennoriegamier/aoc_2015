def main():
    movements = input().rstrip()

    print(part_1(movements))
    print(part_2(movements))


def part_1(movements):
    y = 0
    x = 0
    houses = {(y, x)}

    for movement in movements:
        match movement:
            case '^':
                y += 1
            case 'v':
                y -= 1
            case '>':
                x += 1
            case '<':
                x -= 1
        houses.add((y, x))

    return len(houses)


def part_2(movements):
    y_1 = 0
    x_1 = 0
    y_2 = 0
    x_2 = 0
    houses = {(y_1, x_1)}

    for idx, movement in enumerate(movements):
        if idx % 2 == 0:
            match movement:
                case '^':
                    y_1 += 1
                case 'v':
                    y_1 -= 1
                case '>':
                    x_1 += 1
                case '<':
                    x_1 -= 1
            houses.add((y_1, x_1))
        else:
            match movement:
                case '^':
                    y_2 += 1
                case 'v':
                    y_2 -= 1
                case '>':
                    x_2 += 1
                case '<':
                    x_2 -= 1
            houses.add((y_2, x_2))

    return len(houses)


if __name__ == '__main__':
    main()
