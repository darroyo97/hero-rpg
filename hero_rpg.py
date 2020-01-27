#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee


class Character:
    def __init__(self, name, health, power):
        self.health = health
        self.power = power

    # def alive(self):
    #     if self.health > 0:
    #         return True

    # def attack(self, enemy):
    #     if self.alive() == True:
    #         enemy.health -= self.power
    #         print(f'You do {self.power} damage to the {enemy.name}')
    #         if enemy.alive() != True
    #         print(f'The {enemy.name} is dead')


class Hero(Character):
    def __init__(self):
        super(Hero, self).__init__("Hero", 10, 5)

    def alive(self):
        if self.health > 0:
            return True

    def attack(self, goblin):
        if self.alive() == True:
            goblin.health -= self.power
            print(f'You do {self.power} damage to the goblin')
            if goblin.alive() != True:
                print("The goblin is dead.")


class Goblin(Character):
    def __init__(self):
        super(Goblin, self).__init__("Goblin", 6, 2)

    def alive(self):
        if self.health > 0:
            return True

    def attack(self, hero):
        if self.alive() == True:
            hero.health -= self.power
            print(f'The goblin does {self.power} to you')
            if hero.alive() != True:
                print("You are dead.")


hero = Hero()
goblin = Goblin()


def main():
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2

    while goblin.alive() and hero.alive():
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The goblin has {} health and {} power.".format(
            goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive():
            goblin.attack(hero)


main()
