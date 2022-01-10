from unittest import TestCase, main

from day_25 import part_1


class TestDay24(TestCase):
    def test_part_1(self):
        for row, col, n in [(5, 3, 28_094_349), (4, 6, 31_527_494)]:
            with self.subTest(row=row, col=col):
                self.assertEqual(part_1(row, col), n)


if __name__ == '__main__':
    main()
