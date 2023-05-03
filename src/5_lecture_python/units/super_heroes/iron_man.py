from subclasses.super_hero import SuperHero

class IronMan(SuperHero):

    def __init__(self, name= "Iron Man", weapon= "Plasma cutting", armor_name= "Mark LXXXV", weapon_damage= 19, defense= 3, health= 118, point= 4):
        super().__init__(name, weapon, weapon_damage, armor_name, defense, health, point)

    def super_ability(self, enemy):
        enemy.health -= 13
        
