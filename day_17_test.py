from unittest import TestCase, main

from day_17 import part_1, part_2


class TestDay17(TestCase):
    def setUp(self):
        self._containers = [20, 15, 10, 5, 5]
        self._liters = 25

    def test_part_1(self):
        self.assertEqual(part_1(self._containers, self._liters), 4)

    def test_part_2(self):
        self.assertEqual(part_2(self._containers, self._liters), 3)


if __name__ == '__main__':
    main()
