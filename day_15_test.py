from unittest import TestCase, main

from day_15 import parse_ingredient, part_1, part_2


class TestDay15(TestCase):
    def setUp(self):
        self._ingredients = list(map(parse_ingredient,
                                     ['Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
                                      'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3']))

    def test_part_1(self):
        self.assertEqual(part_1(self._ingredients), 62_842_880)

    def test_part_2(self):
        self.assertEqual(part_2(self._ingredients), 57_600_000)


if __name__ == '__main__':
    main()
