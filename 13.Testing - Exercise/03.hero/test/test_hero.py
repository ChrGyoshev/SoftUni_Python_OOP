from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Warrior',10,100,50)
        self.enemy = Hero("Defender",10,100,50)

    def test_init(self):
        username = 'warrior'
        level = 10
        health = 100
        damage = 50

        hero = Hero(username, level, health,damage)

        self.assertEqual(username,hero.username)
        self.assertEqual(level,hero.level)
        self.assertEqual(health,hero.health)
        self.assertEqual(damage,hero.damage)

    def test_str_returns_proper_string(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        actual = str(self.hero)

        self.assertEqual(expected,actual)

    def test_battle_raises_when_hero_attacks_himself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_raises_if_health_is_zero(self):
        for health in [0,-50]:
            self.hero.health = health
            with self.assertRaises(Exception) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual("Your health is lower than or equal to 0. You need to rest",str(ex.exception))

    def test_battle_raises_if_enemy_health_is_zero_or_lower(self):
        for health in [0,-50]:
            self.enemy.health = health
            with self.assertRaises(Exception) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest",str(ex.exception))

    def test_draw(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)

        self.assertEqual(-400,self.hero.health)
        self.assertEqual(-400,self.enemy.health)

    def test_battle_hero_levels_up_after_win(self):
        enemy = Hero("Defender", 1, 100, 50)

        result = self.hero.battle(enemy)

        self.assertEqual("You win",result)
        self.assertEqual(11,self.hero.level)
        self.assertEqual(55,self.hero.health)
        self.assertEqual(55,self.hero.damage)

        self.assertEqual(-400,enemy.health)

    def test_battle_hero_enemy_levels_up_after_win(self):
        hero = Hero("Defender", 1, 100, 50)
        enemy = Hero("Warrior", 1, 100, 50)

        result = hero.battle(enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(2,enemy.level)
        self.assertEqual(55,enemy.health)
        self.assertEqual(55,enemy.damage)
        self.assertEqual(50,hero.health)


if __name__ == "__main__":
    main()

