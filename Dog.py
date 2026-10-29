
import random

class Dog:
    def ask_name(self):
        self.name = input("Як звуть собаку?")

    def __init__(self):
        self.angry = 5
        self.alive = True
        self.HP = 10
        self.luck = 1

    def angry_up(self):
        if not self.alive:
            return

        chance = random.randint(1, 3 + self.luck)

        if chance != 1:
            self.angry += 1
            print("Собака розізлилася")
        else:
            print("Все ок")

        if self.angry >= 10:
            print("ГАВ!")
            fight = random.randint(1, 3)

            if fight == 1:
                print("Бійки не було")
                self.angry -= 1
            else:
                print("Була бійка")
                self.HP -= 1
                self.angry += 1

        if self.HP <= 0:
            self.alive = False
            print("Собака більше не з нами :(")


dog = Dog()
dog.ask_name()

while dog.alive:
    input("Натисни Enter для продовження")
    dog.angry_up()
    print("Злість:", dog.angry)
    print("HP:", dog.HP)




