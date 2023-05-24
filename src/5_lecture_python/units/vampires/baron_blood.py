from typing import Optional

from subclasses.vampire import Vampire

class BaronBlood(Vampire):

    def __init__(self, name: Optional[str] = "Baron Blood", weapon: Optional[str] = "Vampire sword", weapon_damage: Optional[int] = 15, max_damage: Optional[int] = 20, health: Optional[int] = 132,  point: Optional[int] = 4):
        super().__init__(name, weapon, weapon_damage, max_damage, health, point)

    def super_ability(self, enemy):
        super().super_ability(enemy)
        self.print_ability_baron_blood(enemy)
        self.scoring(self.point)

baron_blood = BaronBlood(name= "Baron Blood", weapon= "Vampire sword", weapon_damage= 15, max_damage= 20, health= 132,  point= 4)    

dracula = BaronBlood(name= "Dracula", weapon= "Dagger", weapon_damage= 17, max_damage= 18, health= 136,  point= 5)