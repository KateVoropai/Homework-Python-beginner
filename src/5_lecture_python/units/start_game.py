from random import randint
from units.vampires import baron_blood
from units.mutants import hulk


def battle(baron_blood, hulk1):

    print("Starting battle between")
    print(baron_blood.__str__())
    print(hulk1.__str__())

    while baron_blood._health > 0 and hulk1._health > 0:
        n = randint(1, 2)
        if n == 1:
            baron_blood.attack(hulk1)
        else:
            hulk1.attack(baron_blood)  
    if baron_blood._health > hulk1._health:
        print(f"{baron_blood.name} won!")
    elif hulk1._health > baron_blood._health:
        print(f" {hulk1.name} won!")


battle(baron_blood, hulk)