from OOP.Character import Character

class Samurai(Character):
    combo = 0
    max_combo = 5




    def __init__(self, name='', health=100, damage=1, defence=0, max_combo=5):
        Character.__init__(self, name, health, damage, defence)
        self.max_combo = max_combo

    def attack(self, target):
        target.take_damage(self.damage + self.damage * 0.1 * self.combo)

        self.combo += 1
        if self.combo > self.max_combo:
            self.combo = 0
            # self.combo = (self.combo + 1) % self.max_combo Можно изменить код на такой