from unittest import TestCase, main

from day_01 import part_1, part_2


class TestDay01(TestCase):
    def test_part_1(self):
        for parenthesis, floor in zip(['(())', '()()', '(((', '(()(()(', '))(((((', '())', '))(', ')))', ')())())'],
                                      [0, 0, 3, 3, 3, -1, -1, -3, -3]):
            with self.subTest(parenthesis=parenthesis):
                self.assertEqual(part_1(parenthesis), floor)

    def test_part_2(self):
        for parenthesis, position in zip([')', '()())'], [1, 5]):
            with self.subTest(parenthesis=parenthesis):
                self.assertEqual(part_2(parenthesis), position)


if __name__ == '__main__':
    main()
