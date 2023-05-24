from typing import Optional

from subclasses.super_hero import SuperHero

class IronMan(SuperHero):

    def __init__(self, name: Optional[str] = "Iron Man", weapon: Optional[str] = "Plasma cutting", weapon_damage: Optional[int] = 19, max_damage: Optional[int] = 17, health: Optional[int] = 118, point: Optional[int] = 7, armor_name: Optional[str] = "Mark LXXXV", defense: Optional[int] = 3):
        super().__init__(name, weapon, weapon_damage, max_damage, health, point, armor_name, defense)

    def super_ability(self, enemy):
        super().super_ability(enemy)
        self.print_ability_iron_man(enemy)
        self.scoring(self.point)

iron_man = IronMan(name= "Iron Man", weapon= "Plasma cutting", weapon_damage= 19, max_damage= 17, health= 118, point= 7, armor_name= "Mark LXXXV", defense= 3)        

spider_man = IronMan(name= "Spider Man", weapon= "Spider Web", weapon_damage= 16, max_damage= 20, health= 119, point= 7, armor_name= "Suit Armor", defense= 4)