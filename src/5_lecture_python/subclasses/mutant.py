from abstract_class.personage import Personage

class Mutant(Personage):

    def __init__(self, name, weapon, weapon_damage, point, health= 110, amount_points= 0):
        super().__init__(name, weapon, weapon_damage, health, point, amount_points)
        
    def __str__(self):
        return  f"""
                {self.name} is a Mutant
                Weapon: {self.weapon}
                Current Health: {self.health}
"""
    def attack_left_arm(self, enemy):
        enemy.health -= 14
        self.scoring((self.point*2))

    def attack_right_arm(self, enemy):
        enemy.health -= 15
        self.scoring(self.point)

    def attack_left_leg(self, enemy):
        enemy.health -= 13
        self.scoring(self.point)

    def attack_right_leg(self, enemy):
        enemy.health -= 17
        self.scoring(self.point)

    def attack_weapons(self, enemy):
        enemy.health -= self.weapon_damage
        self.scoring((self.point)*3)

    def regenerate(self):
        self.health += 3


        






