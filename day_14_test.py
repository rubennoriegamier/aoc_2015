from unittest import TestCase, main

from day_14 import parse_reindeer, part_1, part_2


class TestDay14(TestCase):
    def setUp(self):
        self._reindeer = list(map(parse_reindeer,
                                  ['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
                                   'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.']))

    def test_part_1(self):
        self.assertEqual(part_1(self._reindeer, 1_000), 1_120)

    def test_part_2(self):
        self.assertEqual(part_2(self._reindeer, 1_000), 689)


if __name__ == '__main__':
    main()
