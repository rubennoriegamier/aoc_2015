import fileinput
from functools import cache
from string import digits


def main():
    instructions = list(map(str.split, map(str.rstrip, fileinput.input())))

    print(part_1(instructions))
    print(part_2(instructions))


def part_1(instructions):
    instructions = {wire: instruction for *instruction, _, wire in instructions}

    @cache
    def solve(wire):
        instruction = instructions[wire]

        if instruction[0] == 'NOT':
            return ~solve(instruction[1])

        op_1 = int(instruction[0]) if instruction[0][0] in digits else solve(instruction[0])

        if len(instruction) == 1:
            return op_1

        op_2 = int(instruction[2]) if instruction[2][0] in digits else solve(instruction[2])

        match instruction[1]:
            case 'AND':
                return op_1 & op_2
            case 'OR':
                return op_1 | op_2
            case 'LSHIFT':
                return op_1 << op_2
            case 'RSHIFT':
                return op_1 >> op_2
            case _:
                raise NotImplementedError()

    return solve('a')


def part_2(instructions):
    a = part_1(instructions)
    instructions = instructions.copy()

    for idx in range(len(instructions)):
        if instructions[idx][2] == 'b':
            instructions[idx] = [str(a), '->', 'b']

    return part_1(instructions)


if __name__ == '__main__':
    main()
