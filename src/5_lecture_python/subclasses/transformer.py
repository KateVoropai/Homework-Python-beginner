from abstract_class.personage import Personage

class Transformer(Personage):
    
    def __init__(self, name, weapon, weapon_damage, damage, living_metal, point, health= 120, amount_points= 0):
        super().__init__(name, weapon, weapon_damage, damage, point, health, amount_points)
        self.living_metal = living_metal

    def __str__(self):
        return  f"""
                {self.name} is a Transformer
                Weapon: {self.weapon}
                Current Health: {self.health}
"""
    def attack_left_arm(self, enemy):
        super().attack_left_arm(enemy)
        self.scoring(self.point)

    def attack_right_arm(self, enemy):
        super().attack_right_arm(enemy)
        self.scoring(self.point)

    def attack_left_leg(self, enemy):
        super().attack_left_leg(enemy)
        self.scoring((self.point)*2)

    def attack_right_leg(self, enemy):
        super().attack_right_leg(enemy)
        self.scoring((self.point)*3)

    def attack_weapons(self, enemy):
        super().attack_weapons(enemy)
        self.scoring(self.point)

    def defend(self):
        self.health += self.living_metal
        self.print_defend_transformer()
        
        
        