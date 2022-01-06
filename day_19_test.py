from unittest import TestCase, main

from day_19 import parse_replacements, part_1, part_2


class TestDay19(TestCase):
    def test_part_1(self):
        replacements = parse_replacements('''
H => HO
H => OH
O => HH'''.lstrip())
        molecule = 'HOH'

        self.assertEqual(part_1(replacements, molecule), 4)

    def test_part_2(self):
        replacements = parse_replacements('''
e => H
e => O
H => HO
H => OH
O => HH'''.lstrip())

        for molecule, steps in [('HOH', 3), ('HOHOHO', 6)]:
            with self.subTest(molecule=molecule):
                self.assertEqual(part_2(replacements, molecule), steps)


if __name__ == '__main__':
    main()
