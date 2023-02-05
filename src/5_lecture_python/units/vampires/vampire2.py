from subclasses.vampire import Vampire

if __name__ == "__main__":

    morbius = Vampire("Morbius", weapon_name= "Blade", weapon_damage= 6)
    morbius.drink_blood()
    print(morbius)