from typing import Optional

from subclasses.super_hero import SuperHero

class CaptainAmerica(SuperHero):

    def __init__(self, name: Optional[str] = "Captain America", weapon: Optional[str] = "Infinity Gauntlet", weapon_damage: Optional[int] = 18, max_damage: Optional[int] = 18, health: Optional[int] = 121, point: Optional[int] = 6, armor_name: Optional[str] = "Shield", defense: Optional[int] = 4):
        super().__init__(name, weapon, weapon_damage, max_damage, health, point, armor_name, defense)

    def super_ability(self, enemy):
        super().super_ability(enemy)
        self.print_ability_captain_america(enemy)
        self.scoring(self.point)
    
captain_america = CaptainAmerica(name= "Captain America", weapon= "Infinity Gauntlet", weapon_damage= 18, max_damage= 18, health= 121, point= 6, armor_name= "Shield", defense= 4)

tor = CaptainAmerica(name= "Tor", weapon= "Hammer", weapon_damage= 16, max_damage= 17, health= 125, point= 6, armor_name= "Impenetrable Shield", defense= 5) 