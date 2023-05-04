from subclasses.transformer import Transformer

class Bumblebee(Transformer):

    def __init__(self, name= "Bumblebee", weapon= "Blaster", weapon_damage= 19, living_metal= 6, health= 135,  point= 8):
        super().__init__(name, weapon, weapon_damage, living_metal, health, point)

    def super_ability(self, enemy):
        enemy.health -= 14
        self.scoring(self.point)
    