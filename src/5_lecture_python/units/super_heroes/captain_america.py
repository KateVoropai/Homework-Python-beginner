from subclasses.super_hero import SuperHero

class CaptainAmerica(SuperHero):

    def __init__(self, name= "Captain America", weapon= "Infinity Gauntlet", weapon_damage= 18, health= 121, point= 6, armor_name= "Shield", defense= 4):
        super().__init__(name, weapon, weapon_damage, health, point, armor_name, defense)

    def super_ability(self, enemy):
        enemy.health -= 11
        self.scoring(self.point)
    