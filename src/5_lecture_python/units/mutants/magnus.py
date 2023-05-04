from subclasses.mutant import Mutant

class Magnus(Mutant):
    
    def __init__(self, name= "Magnus", weapon= "Sword", weapon_damage= 16, point= 4, health= 119):
        super().__init__(name, weapon, weapon_damage, point, health)

    def super_ability(self, enemy):
        enemy.health -= 12
        self.scoring(self.point)
    

