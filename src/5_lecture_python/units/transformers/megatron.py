from subclasses.transformer import Transformer

class Megatron(Transformer):

    def __init__(self, name: str, weapon: str, weapon_damage: int, max_damage: int, living_metal: int, health: int, point: int):
        super().__init__(name, weapon, weapon_damage, max_damage, living_metal, health, point)

    def super_ability(self, enemy):
        super().super_ability(enemy)
        self.print_ability_megatron(enemy)
        self.scoring(self.point)
        
megatron = Megatron(name= "Megatron", weapon= "Plasma cannon", weapon_damage= 18, max_damage= 16, living_metal= 3, health= 120, point= 7)  

follen = Megatron(name= "Follen", weapon= "Laser Sword", weapon_damage= 17, max_damage= 15, living_metal= 4, health= 116, point= 8)