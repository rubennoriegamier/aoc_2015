from unittest import TestCase, main

from day_13 import parse_happiness_relations, part_1, part_2


class TestDay13(TestCase):
    def setUp(self):
        self._happiness_relations = parse_happiness_relations(
            ['Alice would gain 54 happiness units by sitting next to Bob.',
             'Alice would lose 79 happiness units by sitting next to Carol.',
             'Alice would lose 2 happiness units by sitting next to David.',
             'Bob would gain 83 happiness units by sitting next to Alice.',
             'Bob would lose 7 happiness units by sitting next to Carol.',
             'Bob would lose 63 happiness units by sitting next to David.',
             'Carol would lose 62 happiness units by sitting next to Alice.',
             'Carol would gain 60 happiness units by sitting next to Bob.',
             'Carol would gain 55 happiness units by sitting next to David.',
             'David would gain 46 happiness units by sitting next to Alice.',
             'David would lose 7 happiness units by sitting next to Bob.',
             'David would gain 41 happiness units by sitting next to Carol.'])

    def test_part_1(self):
        self.assertEqual(part_1(self._happiness_relations), 330)

    def test_part_2(self):
        self.assertEqual(part_2(self._happiness_relations), 286)


if __name__ == '__main__':
    main()
