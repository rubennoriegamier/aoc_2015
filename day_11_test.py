from unittest import TestCase, main

from day_11 import part_1_and_2


class TestDay11(TestCase):
    def test_part_1_and_2(self):
        for password, next_password in [['abcdefgh', 'abcdffaa'], ['ghijklmn', 'ghjaabcc']]:
            with self.subTest(password=password):
                self.assertEqual(part_1_and_2(password), next_password)


if __name__ == '__main__':
    main()
