import fileinput


def main():
    instructions = list(map(parse_instruction, fileinput.input()))

    print(part_1(instructions))
    print(part_2(instructions))


def parse_instruction(raw_instruction: str):
    return raw_instruction.split(maxsplit=1)[0]


def part_1(instructions):
    a = 0
    b = 0

    for instruction in instructions[1:instructions.index('jmp')]:
        if instruction == 'inc':
            a += 1
        else:
            a *= 3

    while a > 1:
        b += 1
        if a % 2 == 0:
            a >>= 1
        else:
            a *= 3
            a += 1

    return b


def part_2(instructions):
    a = 1
    b = 0

    for instruction in instructions[instructions.index('jmp') + 1:instructions.index('jio', 1)]:
        if instruction == 'inc':
            a += 1
        else:
            a *= 3

    while a > 1:
        b += 1
        if a % 2 == 0:
            a >>= 1
        else:
            a *= 3
            a += 1

    return b


if __name__ == '__main__':
    main()
