from subclasses.transformer import Transformer

class Megatron(Transformer):

    def __init__(self, name= "Megatron", weapon= "Plasma cannon", weapon_damage= 18, living_metal= 3):
        super().__init__(name, weapon, weapon_damage, living_metal)


    