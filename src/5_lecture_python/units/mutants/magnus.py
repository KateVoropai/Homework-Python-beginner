from subclasses.mutant import Mutant

class Magnus(Mutant):
    
    def __init__(self, name: str, weapon: str, weapon_damage: int, max_damage: int, point: int, health: int):
        super().__init__(name, weapon, weapon_damage, max_damage, point, health)

    def super_ability(self, enemy):
        super().super_ability(enemy)
        self.print_ability_magnus(enemy)
        self.scoring(self.point)
    
magnus = Magnus(name= "Magnus", weapon= "Sword", weapon_damage= 16, max_damage= 19, point= 4, health= 119)

magneto = Magnus(name= "Magneto", weapon= "Metal cudgel", weapon_damage= 15, max_damage= 20, point= 4, health= 120)