from subclasses.super_hero import SuperHero

class CaptainAmerica(SuperHero):

    def __init__(self, name: str, weapon: str, weapon_damage: int, max_damage: int, health: int, point: int, armor_name: str, defense: int):
        super().__init__(name, weapon, weapon_damage, max_damage, health, point, armor_name, defense)

    def super_ability(self, enemy):
        super().super_ability(enemy)
        self.print_ability_captain_america(enemy)
        self.scoring(self.point)
    
captain_america = CaptainAmerica(name= "Captain America", weapon= "Infinity Gauntlet", weapon_damage= 18, max_damage= 18, health= 121, point= 6, armor_name= "Shield", defense= 4)

tor = CaptainAmerica(name= "Tor", weapon= "Hammer", weapon_damage= 16, max_damage= 17, health= 125, point= 6, armor_name= "Impenetrable Shield", defense= 5) 