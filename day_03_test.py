from unittest import TestCase, main

from day_03 import part_1, part_2


class TestDay03(TestCase):
    def test_part_1(self):
        for movements, houses in zip(['>', '^>v<', '^v^v^v^v^v'], [2, 4, 2]):
            with self.subTest(movements=movements):
                self.assertEqual(part_1(movements), houses)

    def test_part_2(self):
        for movements, houses in zip(['^v', '^>v<', '^v^v^v^v^v'], [3, 3, 11]):
            with self.subTest(movements=movements):
                self.assertEqual(part_2(movements), houses)


if __name__ == '__main__':
    main()
