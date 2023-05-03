from abstract_class.personage import Personage

class Transformer(Personage):
    
    def __init__(self, name, weapon, weapon_damage, living_metal, point, health= 120, amount_points= 0):
        super().__init__(name, weapon, weapon_damage, point, health, amount_points)
        self.living_metal = living_metal

    def __str__(self):
        return  f"""
                {self.name} is a Transformer
                Weapon: {self.weapon}
                Current Health: {self.health}
"""
    def attack_left_arm(self, enemy):
        enemy.health -= 12
        self.scoring(self.point)

    def attack_right_arm(self, enemy):
        enemy.health -= 16
        self.scoring(self.point)

    def attack_left_leg(self, enemy):
        enemy.health -= 14
        self.scoring((self.point)*2)

    def attack_right_leg(self, enemy):
        enemy.health -= 15
        self.scoring((self.point)*3)

    def attack_weapons(self, enemy):
        enemy.health -= self.weapon_damage
        self.scoring(self.point)

    def repair(self):
        self.health += self.living_metal
        
        
        