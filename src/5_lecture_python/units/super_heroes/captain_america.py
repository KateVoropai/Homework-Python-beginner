from subclasses.super_hero import SuperHero

class CaptainAmerica(SuperHero):

    def __init__(self, name= "Captain America", weapon= "Infinity Gauntlet", armor_name= "Shield", weapon_damage= 18, defense= 4, health= 121, point= 3):
        super().__init__(name, weapon, weapon_damage, armor_name, defense, health, point)

    def super_ability(self, enemy):
        enemy.health -= 11
    