from subclasses.transformer import Transformer

class Bumblebee(Transformer):

    def __init__(self, name= "Bumblebee", weapon= "Blaster", weapon_damage= 19, living_metal= 6, health= 175):
        super().__init__(name, weapon, weapon_damage, living_metal, health)
