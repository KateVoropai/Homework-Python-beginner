from subclasses.super_hero import SuperHero

class IronMan(SuperHero):

    def __init__(self, name= "Iron Man", weapon= "Plasma cutting", weapon_damage= 19, health= 118, point= 7, armor_name= "Mark LXXXV", defense= 3):
        super().__init__(name, weapon, weapon_damage, health, point, armor_name, defense)

    def super_ability(self, enemy):
        enemy.health -= 13
        self.scoring(self.point)
        
