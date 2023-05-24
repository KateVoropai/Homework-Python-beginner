from typing import Optional

from subclasses.vampire import Vampire

class Morbius(Vampire):

    def __init__(self, name: Optional[str] = 'Morbius', weapon: Optional[str] = 'Axe', weapon_damage: Optional[int] = 16, max_damage: Optional[int] = 16, health: Optional[int] = 130, point: Optional[int] = 6):
        super().__init__(name, weapon, weapon_damage, max_damage, health, point)

    def super_ability(self, enemy):
        super().super_ability(enemy)
        self.print_ability_morbius(enemy)
        self.scoring(self.point)
        

morbius = Morbius(name= "Morbius", weapon= "Axe", weapon_damage= 16, max_damage= 16, health= 130, point= 6)

damon = Morbius(name= "Damon", weapon= "Magic Wand", weapon_damage= 18, max_damage= 19, health= 135, point= 5)