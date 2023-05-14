from subclasses.mutant import Mutant

class Hulk(Mutant):

    def __init__(self, name: str, weapon: str, weapon_damage: int, max_damage: int, point: int, health: int):
        super().__init__(name, weapon, weapon_damage, max_damage, point, health)

    def super_ability(self, enemy):
        super().super_ability(enemy)
        self.print_ability_hulk(enemy)
        self.scoring(self.point)

hulk = Hulk(name= "Hulk", weapon= "Cudgel", weapon_damage= 17, max_damage= 18, point= 5, health= 116)

red_hulk = Hulk(name= "Red Hulk", weapon= "Sword", weapon_damage= 18, max_damage= 19, point= 5, health= 117)