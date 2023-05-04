from subclasses.mutant import Mutant

class Hulk(Mutant):

    def __init__(self, name= "Hulk", weapon= "Cudgel", weapon_damage= 17, point= 5, health= 116):
        super().__init__(name, weapon, weapon_damage, point, health)

    def super_ability(self, enemy):
        enemy.health -= 10
        self.scoring(self.point)
    


