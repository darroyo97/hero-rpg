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
        super(Hero, self).__init__("Hero", 1000, 5)

    def attack(self, enemy):
        power = self.power
        if random.randint(0, 100) < 20:
            power = self.power * 2
            print('Critical hit!')
        enemy.health -= power
        print("The {} does {} damage to {}".format(
            self.name, power, enemy.name))
        if enemy.name == "Medic":
            if random.randint(0, 100) < 20:
                enemy.health + 2
                print(f' {enemy.name} used health regain !')

        if enemy.alive() != True:

            print(f'The {enemy.name} is dead')


class Goblin(Character):
    def __init__(self):
        super(Goblin, self).__init__("Goblin", 6, 2)


class Zombie(Character):
    def __init__(self):
        super(Zombie, self).__init__("Zombie", 10, 1)


class Medic(Character):
    def __init__(self):
        super(Medic, self).__init__("Medic", 1000, 2)


hero = Hero()
goblin = Goblin()
zombie = Zombie()
medic = Medic()
enemy_list = [medic]
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
