from unittest import TestCase, main

from day_22 import part_1_and_2


class TestDay22(TestCase):
    def setUp(self):
        self._games = [(10, 250, 13, 8), (10, 250, 14, 8)]

    def test_part_1(self):
        for (player_hp, player_mana, boss_hp, boss_damage), min_mana in zip(self._games, [226, 641]):
            with self.subTest(player_hp=player_hp, player_mana=player_mana, boss_hp=boss_hp, boss_damage=boss_damage):
                self.assertEqual(part_1_and_2(player_hp, player_mana, boss_hp, boss_damage), min_mana)


if __name__ == '__main__':
    main()
