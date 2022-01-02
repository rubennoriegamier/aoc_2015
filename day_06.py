import fileinput

import numpy as np


def main():
    instructions = list(map(parse_instruction, fileinput.input()))

    print(part_1(instructions))
    print(part_2(instructions))


def parse_instruction(raw_instruction):
    instruction, yx_start, _, yx_stop = raw_instruction.rsplit(maxsplit=3)
    y_start, x_start = map(int, yx_start.split(','))
    y_stop, x_stop = map(int, yx_stop.split(','))

    return instruction, (slice(y_start, y_stop + 1), slice(x_start, x_stop + 1))


def part_1(instructions):
    lights = np.zeros((1_000, 1_000), bool)

    for instruction, slices in instructions:
        match instruction:
            case 'turn on':
                lights[slices] = True
            case 'turn off':
                lights[slices] = False
            case 'toggle':
                np.logical_not(lights[slices], out=lights[slices])

    return lights.sum()


def part_2(instructions):
    lights = np.zeros((1_000, 1_000), np.int16)
    aux = np.empty_like(lights, bool)

    for instruction, slices in instructions:
        match instruction:
            case 'turn on':
                lights[slices] += 1
            case 'turn off':
                np.greater(lights[slices], 0, out=aux[slices])
                np.subtract(lights[slices], 1, out=lights[slices], where=aux[slices])
            case 'toggle':
                lights[slices] += 2

    return lights.sum()


if __name__ == '__main__':
    main()
