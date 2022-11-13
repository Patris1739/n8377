from OOP.Character import Character
import random

class Ninja(Character):
    max_health = 100
    def __init__(self, name='',health=100, damage=1, defence=0):
        Character.__init__(self, name,health, damage, defence)

    def count_addition_damage(self):
        return (self.max_health - self.health) / self.max_health * self.damage

    def attack(self, target):
        if random.randint(1, 100) > 50:
            target.take_damage(self.damage + self.count_addition_damage())



    def take_damage(self, damage):
        if random.randint(1, 100) > 50:
            self.health -= damage
