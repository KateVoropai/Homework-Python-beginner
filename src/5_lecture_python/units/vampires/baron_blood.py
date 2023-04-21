from subclasses.vampire import Vampire

class BaronBlood(Vampire):

    def __init__(self, name= "Baron Blood", weapon= "Vampire sword", weapon_damage= 15, health= 132):
        super().__init__(name, weapon, weapon_damage, health)

 