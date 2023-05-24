from typing import Optional

from subclasses.transformer import Transformer

class Megatron(Transformer):

    def __init__(self, name: Optional[str] = "Megatron", weapon: Optional[str] = "Plasma cannon", weapon_damage: Optional[int] = 18, max_damage: Optional[int] = 16, living_metal: Optional[int] = 3, health: Optional[int] = 120, point: Optional[int] = 7):
        super().__init__(name, weapon, weapon_damage, max_damage, living_metal, health, point)

    def super_ability(self, enemy):
        super().super_ability(enemy)
        self.print_ability_megatron(enemy)
        self.scoring(self.point)
        
megatron = Megatron(name= "Megatron", weapon= "Plasma cannon", weapon_damage= 18, max_damage= 16, living_metal= 3, health= 120, point= 7)  

follen = Megatron(name= "Follen", weapon= "Laser Sword", weapon_damage= 17, max_damage= 15, living_metal= 4, health= 116, point= 8)