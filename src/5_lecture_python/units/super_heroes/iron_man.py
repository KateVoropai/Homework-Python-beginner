from subclasses.super_hero import SuperHero

class IronMan(SuperHero):

    def __init__(self, name= "Iron Man", weapon= "Plasma cutting", weapon_damage= 9, armor_name= "Mark LXXXV", defense= 4):
        super().__init__(name, weapon, weapon_damage, armor_name, defense)


