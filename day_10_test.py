from itertools import pairwise
from unittest import TestCase, main

from day_10 import next_sequence


class TestDay10(TestCase):
    def test_next_sequence(self):
        for sequence, next_sequence_ in pairwise([[1], [1, 1], [2, 1], [1, 2, 1, 1], [1, 1, 1, 2, 2, 1]]):
            with self.subTest(sequence=sequence):
                self.assertEqual(list(next_sequence(sequence)), next_sequence_)


if __name__ == '__main__':
    main()
