from Character import Character

player1 = Character(name='Arnold', damage=15)
player2 = Character(name='Roberto',damage=10)

print(player1,'\n')
print(player2, '\n')


while player1.is_alive() and player2.is_alive():
    player1.attack(player2)
    player2.attack(player1)

print(player1, '\n')
print(player2, '\n')