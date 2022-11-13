from OOP.Character import Character
import random

class Assasin(Character):
    max_health = 150

    def __init__(self, name='', health=150, damage=20, defense=0):
        Character.__init__(self, name, health, damage, defense)
        self.max_health = self.health

    def attack(self, target: Character):
        krit=random.randint(2,5)
        if krit==3:
            target.take_damage(self.damage+900)
        else:
            target.take_damage(self.damage)