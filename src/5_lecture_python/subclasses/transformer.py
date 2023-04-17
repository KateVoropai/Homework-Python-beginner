from abstract_class.personage import Personage

class Transformer(Personage):
    
    def __init__(self, name, weapon, weapon_damage, living_metal, health= 180):
        super().__init__(name, weapon, weapon_damage, health)
        self.living_metal = living_metal

    def __str__(self):
        return  f"""
                {self.name} is a Transformer
                Weapon: {self.weapon}
                Current Health: {self._health}
"""
    def attack_left_arm(self, enemy):
        enemy._health -= 12

    def attack_right_arm(self, enemy):
        enemy._health -= 16

    def attack_left_leg(self, enemy):
        enemy._health -= 14

    def attack_right_leg(self, enemy):
        enemy._health -= 15

    def attack_weapons(self, enemy):
        enemy._health -= self.weapon_damage

    def repair(self):
        self._health += self.living_metal
        print(f"{self.name} починил себя! Текущее здоровье {self._health}")
        
        