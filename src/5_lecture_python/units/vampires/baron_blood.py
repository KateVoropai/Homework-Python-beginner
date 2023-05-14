from subclasses.vampire import Vampire

class BaronBlood(Vampire):

    def __init__(self, name: str, weapon: str, weapon_damage: int, max_damage: int, health: int,  point: int):
        super().__init__(name, weapon, weapon_damage, max_damage, health, point)

    def super_ability(self, enemy):
        super().super_ability(enemy)
        self.print_ability_baron_blood(enemy)
        self.scoring(self.point)

baron_blood = BaronBlood(name= "Baron Blood", weapon= "Vampire sword", weapon_damage= 15, max_damage= 20, health= 132,  point= 4)    

dracula = BaronBlood(name= "Dracula", weapon= "Dagger", weapon_damage= 17, max_damage= 18, health= 136,  point= 5)