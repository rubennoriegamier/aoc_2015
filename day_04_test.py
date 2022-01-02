from unittest import TestCase, main

from day_04 import part_1, part_2


class TestDay04(TestCase):
    def setUp(self):
        self._secrets = ['abcdef', 'pqrstuv']

    def test_part_1(self):
        for secret, n in zip(self._secrets, [609_043, 1_048_970]):
            with self.subTest(secret=secret):
                self.assertEqual(part_1(secret), n)

    def test_part_2(self):
        for secret, n in zip(self._secrets, [6_742_839, 5_714_438]):
            with self.subTest(secret=secret):
                self.assertEqual(part_2(secret), n)


if __name__ == '__main__':
    main()
