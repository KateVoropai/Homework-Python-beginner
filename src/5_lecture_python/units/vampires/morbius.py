from subclasses.vampire import Vampire

class Morbius(Vampire):

    def __init__(self, name= "Morbius", weapon= "Blade", weapon_damage= 16, health= 130, point= 4):
        super().__init__(name, weapon, weapon_damage, health, point)

    def super_ability(self, enemy):
        enemy.health -= 15
        

