from berserk import Berserk
from OOP.Character import Character
from Samurai import Samurai
from Assasin import Assasin
from Ninja import Ninja


player1 = Berserk(name='Kratos', damage=10)
player2 = Character(name='Tor', damage=15)
player3 = Samurai(name='Samurai ', damage=20)
player4 = Assasin(name='Assasin ', damage=20)
player5 = Ninja(name='Ninja ', damage=25)




print(f'{player1}\n')
print(f'{player2}\n')
print(f'{player3}\n')
print(f'{player4}\n')
print(f'{player5}\n')


while player1.is_alive() and player2.is_alive() and player3.is_alive():
    player1.attack(player2)
    player1.attack(player3)
    player1.attack(player5)
    player2.attack(player1)
    player2.attack(player4)
    player3.attack(player2)
    player3.attack(player5)
    player3.attack(player4)
    player4.attack(player2)
    player5.attack(player3)

print(f'{player1}\n')
print(f'additional damage: {player1.count_additional_damage()}')
print(f'{player2}\n')
print(f'{player3}\n')
print(f'{player4}\n')
print(f'{player5}\n')