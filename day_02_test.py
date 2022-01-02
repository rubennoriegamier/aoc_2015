from unittest import TestCase, main

from day_02 import parse_dimensions, part_1, part_2


class TestDay02(TestCase):
    def setUp(self):
        self._dimensions = list(map(parse_dimensions, ['2x3x4', '1x1x10']))

    def test_part_1(self):
        self.assertEqual(part_1(self._dimensions), 58 + 43)

    def test_part_2(self):
        self.assertEqual(part_2(self._dimensions), 34 + 14)


if __name__ == '__main__':
    main()
