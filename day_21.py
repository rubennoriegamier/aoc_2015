WEAPONS = [(8, 4),
           (10, 5),
           (25, 6),
           (40, 7),
           (74, 8)]
ARMOR = [(0, 0),
         (13, 1),
         (31, 2),
         (53, 3),
         (75, 4),
         (102, 5)]
RINGS = [(0, 0, 0),
         (25, 1, 0),
         (50, 2, 0),
         (100, 3, 0),
         (20, 1, 0),
         (40, 2, 0),
         (80, 3, 0)]


def main():
    boss_stats = int(input().split()[-1]), int(input().split()[-1]), int(input().split()[-1])

    print(part_1(boss_stats))
    print(part_2(boss_stats))


def part_1(boss_stats):
    return min(weapon_cost + armor_cost + ring_1_cost + ring_2_cost
               for weapon_cost, weapon_damage in WEAPONS
               for armor_cost, armor_armor in ARMOR
               for ring_1_cost, ring_1_damage, ring_1_armor in RINGS
               for ring_2_cost, ring_2_damage, ring_2_armor in RINGS
               if (ring_1_cost != ring_2_cost or ring_1_cost == 0) and
               boss_stats[0] / max(weapon_damage + ring_1_damage + ring_2_damage - boss_stats[2], 1)
               <= 100 / max(boss_stats[1] - armor_armor - ring_1_armor - ring_2_armor, 1))


def part_2(boss_stats):
    return max(weapon_cost + armor_cost + ring_1_cost + ring_2_cost
               for weapon_cost, weapon_damage in WEAPONS
               for armor_cost, armor_armor in ARMOR
               for ring_1_cost, ring_1_damage, ring_1_armor in RINGS
               for ring_2_cost, ring_2_damage, ring_2_armor in RINGS
               if (ring_1_cost != ring_2_cost or ring_1_cost == 0) and
               boss_stats[0] / max(weapon_damage + ring_1_damage + ring_2_damage - boss_stats[2], 1)
               > 100 / max(boss_stats[1] - armor_armor - ring_1_armor - ring_2_armor, 1))


if __name__ == '__main__':
    main()
