from unittest import TestCase, main

from day_24 import part_1, part_2


class TestDay24(TestCase):
    def setUp(self):
        self._weights = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

    def test_part_1(self):
        self.assertEqual(part_1(self._weights), 99)

    def test_part_2(self):
        self.assertEqual(part_2(self._weights), 44)


if __name__ == '__main__':
    main()
