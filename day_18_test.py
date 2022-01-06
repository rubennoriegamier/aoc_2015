from unittest import TestCase, main

from day_18 import parse_lights, part_1, part_2


class TestDay17(TestCase):
    def test_part_1(self):
        self.assertEqual(part_1(parse_lights(['.#.#.#',
                                              '...##.',
                                              '#....#',
                                              '..#...',
                                              '#.#..#',
                                              '####..']), 4), 4)

    def test_part_2(self):
        self.assertEqual(part_2(parse_lights(['##.#.#',
                                              '...##.',
                                              '#....#',
                                              '..#...',
                                              '#.#..#',
                                              '####.#']), 5), 17)


if __name__ == '__main__':
    main()
