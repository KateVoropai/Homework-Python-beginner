from subclasses.mutant import Mutant

class Magnus(Mutant):
    
    def __init__(self, name= "Magnus", weapon= "Sword", weapon_damage= 16, health= 119, point= 3):
        super().__init__(name, weapon, weapon_damage, health, point)

    def super_ability(self, enemy):
        enemy.health -= 12
    

