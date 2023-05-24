from typing import Optional

from subclasses.transformer import Transformer

class Bumblebee(Transformer):

    def __init__(self, name: Optional[str] = "Bumblebee", weapon: Optional[str] = "Blaster", weapon_damage: Optional[int] = 19, max_damage: Optional[int] = 17, living_metal: Optional[int] = 6, health: Optional[int] = 135, point: Optional[int] = 8):
        super().__init__(name, weapon, weapon_damage, max_damage, living_metal, health, point)

    def super_ability(self, enemy):
        super().super_ability(enemy)
        self.print_ability_bumblebee(enemy)
        self.scoring(self.point)

bumblebee = Bumblebee(name= "Bumblebee", weapon= "Blaster", weapon_damage= 19, max_damage= 17, living_metal= 6, health= 135,  point= 8)    

optimus_prime = Bumblebee(name= "Optimus Prime", weapon= "Laser Cannon", weapon_damage= 18, max_damage= 19, living_metal= 7, health= 130,  point= 8)