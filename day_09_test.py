from unittest import TestCase, main

from day_09 import parse_distances, part_1, part_2


class TestDay09(TestCase):
    def setUp(self):
        self._distances = parse_distances(['London to Dublin = 464',
                                           'London to Belfast = 518',
                                           'Dublin to Belfast = 141'])

    def test_part_1(self):
        self.assertEqual(part_1(self._distances), 605)

    def test_part_2(self):
        self.assertEqual(part_2(self._distances), 982)


if __name__ == '__main__':
    main()
