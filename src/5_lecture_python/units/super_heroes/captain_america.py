from subclasses.super_hero import SuperHero

class CaptainAmerica(SuperHero):

    def __init__(self, name= "Captain America", weapon= "Infinity Gauntlet", weapon_damage= 18, armor_name= "Shield", defense= 5):
        super().__init__(name, weapon, weapon_damage, armor_name, defense)

