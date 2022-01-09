from functools import cache


def main():
    boss_hp = int(input().split()[-1])
    boss_damage = int(input().split()[-1])

    print(part_1_and_2(50, 500, boss_hp, boss_damage))
    print(part_1_and_2(50, 500, boss_hp, boss_damage, hard=True))


def part_1_and_2(player_hp, player_mana, boss_hp, boss_damage, /, hard=False):
    boss_damage_with_shield = max(1, boss_damage - 7)

    @cache
    def player_turn(player_hp_, player_mana_, boss_hp_, shield, poison, recharge):
        if hard:
            if player_hp_ <= 1:
                return float('inf')
            player_hp_ -= 1
        if poison > 0:
            if boss_hp_ <= 3:
                return 0
            boss_hp_ -= 3
            poison -= 1
        if shield > 0:
            shield -= 1
        if recharge > 0:
            player_mana_ += 101
            recharge -= 1

        if player_mana_ < 53:
            return float('inf')

        if boss_hp_ <= 4:
            return 53
        min_mana = 53 + boss_turn(player_hp_, player_mana_ - 53, boss_hp_ - 4, shield, poison, recharge)

        if player_mana_ >= 73:
            if boss_hp_ <= 2:
                return min(min_mana, 73)
            min_mana = min(min_mana,
                           73 + boss_turn(player_hp_ + 2, player_mana_ - 73, boss_hp_ - 2, shield, poison, recharge))

            if player_mana_ >= 113:
                if shield == 0:
                    min_mana = min(min_mana,
                                   113 + boss_turn(player_hp_, player_mana_ - 113, boss_hp_, 6, poison, recharge))

                if player_mana_ >= 173:
                    if poison == 0:
                        min_mana = min(min_mana,
                                       173 + boss_turn(player_hp_, player_mana_ - 173, boss_hp_, shield, 6, recharge))

                    if player_mana_ >= 229:
                        if recharge == 0:
                            min_mana = min(min_mana,
                                           229 + boss_turn(player_hp_, player_mana_ - 229, boss_hp_, shield, poison, 5))

        return min_mana

    def boss_turn(player_hp_, player_mana_, boss_hp_, shield, poison, recharge):
        if poison > 0:
            if boss_hp_ <= 3:
                return 0
            boss_hp_ -= 3
            poison -= 1
        if shield > 1:
            player_hp_ -= boss_damage_with_shield
            shield -= 1
        else:
            player_hp_ -= boss_damage
        if player_hp_ <= 0:
            return float('inf')
        if recharge > 0:
            player_mana_ += 101
            recharge -= 1

        return player_turn(player_hp_, player_mana_, boss_hp_, shield, poison, recharge)

    return player_turn(player_hp, player_mana, boss_hp, 0, 0, 0)


if __name__ == '__main__':
    main()
