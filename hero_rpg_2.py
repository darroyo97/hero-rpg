import random


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


class Goblin(Character):
    def __init__(self):
        super(Goblin, self).__init__("Goblin", 6, 2)


class Zombie(Character):
    def __init__(self):
        super(Zombie, self).__init__("Zombie", 10, 1)


hero = Hero()
goblin = Goblin()
zombie = Zombie()
enemy_list = [zombie, goblin]
enemy_char = random.choice(enemy_list)


def main(enemy):

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


main(enemy_char)
