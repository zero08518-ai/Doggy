import random

class Hero:
    def __init__(self):
        self.enraged = False
        self.hero_hp = 10

    def attack(self, dragon, sword):
        sword.check_damage()
        dragon.dragon_hp -= sword.sword_dam

        dragon.dragon_hp = max(0, dragon.dragon_hp)


class Dragon:
    def __init__(self):
        self.dragon_hp = 15
    def fire_attack(self, hero, fireball):
        hero.hero_hp -= fireball.fire_dam

        hero.hero_hp = max(0, hero.hero_hp)

class Sword:
    def __init__(self, hero):
        self.hero = hero
        self.sword_dam = random.randint(1, 3)

    def check_damage(self):
        if self.hero.hero_hp <= 5 and not self.hero.enraged:
            self.sword_dam += 2
            self.hero.enraged = True


class Fireball:
    def __init__(self):
        self.fire_dam = random.randint(1, 2)


hero = Hero()
sword = Sword(hero)
dragon = Dragon()
fireball = Fireball()

while hero.hero_hp > 0 and dragon.dragon_hp > 0:
    turn = random.randint(1, 2)

    if turn == 1:
        dragon.fire_attack(hero, fireball)

        if hero.hero_hp > 0:
            hero.attack(dragon, sword)

    else:
        hero.attack(dragon, sword)

        if dragon.dragon_hp > 0:
            dragon.fire_attack(hero, fireball)

    print("The Hero's HP:", hero.hero_hp)
    print("The Dragon's HP:", dragon.dragon_hp)

if hero.hero_hp <= 0:
    print("The Dragon wins!")
elif dragon.dragon_hp <= 0:
    print("The Hero wins!")
    