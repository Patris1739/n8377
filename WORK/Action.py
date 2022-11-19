class Person:
    name = ''
    health = 100
    mood = 100
    money = 100

    def __init__(self, name='', health=100, mood=100, money=100):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
         return f'==={self.name}=== \n' \
                f' Здровье: {self.health} \n' \
                f' Настроение : {self.mood} \n' \
                f' Деньги : {self.money} \n' \

    def change_state(self, health, mood, money):
        self.health += health
        self.mood += mood
        self.money += money