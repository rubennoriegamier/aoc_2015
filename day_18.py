import fileinput
from functools import partial
from operator import eq

import numpy as np
# noinspection PyProtectedMember
from numpy.lib.stride_tricks import as_strided


def main():
    lights = parse_lights(map(str.rstrip, fileinput.input()))

    print(part_1(lights, 100))
    print(part_2(lights, 100))


def parse_lights(raw_lights):
    return list(map(list, map(partial(map, partial(eq, '#')), raw_lights)))


def part_1(lights, steps):
    height = len(lights)
    width = len(lights[0])
    lights_ = np.zeros((height + 2, width + 2), bool)
    lights_[1:-1, 1:-1] = lights
    lights = lights_
    neighbors_on = np.empty((height, width), np.byte)
    aux = np.empty((height, width), bool)

    for _ in range(steps):
        as_strided(lights, (height, width, 3, 3), (lights.shape[0], 1, lights.shape[0], 1)) \
            .sum((2, 3), out=neighbors_on)
        neighbors_on -= lights[1:-1, 1:-1]
        np.logical_not(lights[1:-1, 1:-1], out=aux)
        np.greater_equal(neighbors_on, 2, out=lights[1:-1, 1:-1], where=lights[1:-1, 1:-1])
        np.less_equal(neighbors_on, 3, out=lights[1:-1, 1:-1], where=lights[1:-1, 1:-1])
        np.equal(neighbors_on, 3, out=lights_[1:-1, 1:-1], where=aux)

    return lights.sum()


def part_2(lights, steps):
    height = len(lights)
    width = len(lights[0])
    lights_ = np.zeros((height + 2, width + 2), bool)
    lights_[1:-1, 1:-1] = lights
    lights = lights_
    neighbors_on = np.empty((height, width), np.byte)
    aux = np.empty((height, width), bool)

    for _ in range(steps):
        as_strided(lights, (height, width, 3, 3), (lights.shape[0], 1, lights.shape[0], 1)) \
            .sum((2, 3), out=neighbors_on)
        neighbors_on -= lights[1:-1, 1:-1]
        np.logical_not(lights[1:-1, 1:-1], out=aux)
        np.greater_equal(neighbors_on, 2, out=lights[1:-1, 1:-1], where=lights[1:-1, 1:-1])
        np.less_equal(neighbors_on, 3, out=lights[1:-1, 1:-1], where=lights[1:-1, 1:-1])
        np.equal(neighbors_on, 3, out=lights_[1:-1, 1:-1], where=aux)

        lights[1, 1] = True
        lights[1, -2] = True
        lights[-2, 1] = True
        lights[-2, -2] = True

    return lights.sum()


if __name__ == '__main__':
    main()
