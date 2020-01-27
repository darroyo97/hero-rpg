#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee


class Character:
    def __init__(self, name, health, power):
        self.health = health
        self.power = power
        self.name = name

    def alive(self):
        if self.health > 0:
            return True

    def attack(self, enemy):

        if enemy.name != "Zombie" and self.alive() == True:
            enemy.health -= self.power
            print(f'{self.name} does {self.power} damage to the {enemy.name}')
            if enemy.alive() != True:
                print(f'The {enemy.name} is dead')


class Hero(Character):
    def __init__(self):
        super(Hero, self).__init__("Hero", 10, 5)

    # def attack(self, goblin):
    #     if self.alive() == True:
    #         goblin.health -= self.power
    #         print(f'You do {self.power} damage to the goblin')
    #         if goblin.alive() != True:
    #             print("The goblin is dead.")


class Goblin(Character):
    def __init__(self):
        super(Goblin, self).__init__("Goblin", 6, 2)

    # def attack(self, hero):
    #     if self.alive() == True:
    #         hero.health -= self.power
    #         print(f'The goblin does {self.power} to you')
    #         if hero.alive() != True:
    #             print("You are dead.")


class Zombie(Character):
    def __init__(self):
        super(Zombie, self).__init__("Zombie", 10, 1)


hero = Hero()
goblin = Goblin()
zombie = Zombie()


def main(enemy):
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2

    while enemy.alive() and hero.alive():
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The {} has {} health and {} power.".format(
            enemy.name, enemy.health, enemy.power))
        print()
        print("What do you want to do?")
        print(f'1. fight {enemy.name}')
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(enemy)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.alive():
            enemy.attack(hero)


main(zombie)
