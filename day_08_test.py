from unittest import TestCase, main

from day_08 import part_1, part_2


class TestDay08(TestCase):
    def setUp(self):
        self._strings = [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']

    def test_part_1(self):
        self.assertEqual(part_1(self._strings), 12)

    def test_part_2(self):
        self.assertEqual(part_2(self._strings), 19)


if __name__ == '__main__':
    main()
