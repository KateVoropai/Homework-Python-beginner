from typing import Optional

from subclasses.mutant import Mutant

class Hulk(Mutant):

    def __init__(self, name: Optional[str] = "Hulk", weapon: Optional[str] = "Cudgel", weapon_damage: Optional[int] = 17, max_damage: Optional[int] = 18, point: Optional[int] = 5, health: Optional[int] = 116):
        super().__init__(name, weapon, weapon_damage, max_damage, point, health)

    def super_ability(self, enemy):
        super().super_ability(enemy)
        self.print_ability_hulk(enemy)
        self.scoring(self.point)

hulk = Hulk(name= "Hulk", weapon= "Cudgel", weapon_damage= 17, max_damage= 18, point= 5, health= 116)

red_hulk = Hulk(name= "Red Hulk", weapon= "Sword", weapon_damage= 18, max_damage= 19, point= 5, health= 117)