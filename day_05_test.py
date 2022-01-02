from unittest import TestCase, main

from day_05 import part_1, part_2


class TestDay05(TestCase):
    def test_part_1(self):
        self.assertEqual(part_1(['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp',
                                 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']), 2)

    def test_part_2(self):
        self.assertEqual(part_2(['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']), 2)


if __name__ == '__main__':
    main()
