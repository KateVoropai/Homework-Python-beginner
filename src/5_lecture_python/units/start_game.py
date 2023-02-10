from random import randint
from units.vampires import baron_blood
from units.mutants import hulk


def battle(self, baron_blood, hulk):

    print("Starting battle between")
    print(baron_blood.__str__())
    print(hulk.__str__())

    while baron_blood.health > 0 and hulk.health > 0:
        n = randint(1, 2)
        if n == 1:
            baron_blood.attack(hulk)
        else:
            hulk.attack(baron_blood)  
    if baron_blood.health > hulk.health:
        print(f"{baron_blood.name} won!")
    elif hulk.health > baron_blood.health:
        print(f" {hulk.name} won!")


if __name__ == "__main__":
    baron_blood
    hulk
    battle(baron_blood, hulk)