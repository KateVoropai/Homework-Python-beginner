from subclasses.transformer import Transformer

class Megatron(Transformer):

    def __init__(self, name= "Megatron", weapon= "Plasma cannon", weapon_damage= 10, living_metal= 5):
        super().__init__(name, weapon, weapon_damage, living_metal)


    