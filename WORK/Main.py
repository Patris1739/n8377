import random
from Person import Person
#from Action import Action


man = Person(name='Майкл', money=100, mood=100, health=100)
man2 = Person(name='Арнольд', money=100, mood=100, health=100)
man3 = Person(name='Вильям', money=100, mood=100, health=100)
#go_to_park = Action(name = 'Сходить в парк', money = 0, mood = 15, health = 3)
#man.do(go_to_park)


while True:
    answear=0
    print(man)
    print(man2)
    print(man3)

    try:
        man.change_state(
          money=random.randint(50, 100),
          mood=random.randint(-20, -10),
          health=random.randint(-10, -5)
        )
    except Exception:
        answear+=1

    try:
        man2.change_state(
            money=random.randint(50, 100),
            mood=random.randint(-20, -10),
            health=random.randint(-10, -5)
        )
    except Exception:
        answear +=1
    try:
        man3.change_state(
            money=random.randint(50, 100),
            mood=random.randint(-20, -10),
            health=random.randint(-10, -5)
        )

    except Exception:
        answear+=1
    if answear>2:
        break






