from subclasses.vampire import Vampire

if __name__ == "__main__":

    baron_blood = Vampire("Baron Blood", weapon_name= "Vampire sword", weapon_damage= 5)
    baron_blood.drink_blood()
    print(baron_blood)