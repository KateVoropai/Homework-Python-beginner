from subclasses.mutant import Mutant

class Hulk(Mutant):

    def __init__(self, name= "Hulk", weapon= "Cudgel", weapon_damage= 17, health= 116, point= 4):
        super().__init__(name, weapon, weapon_damage, health, point)

    def super_ability(self, enemy):
        enemy.health -= 10
    


