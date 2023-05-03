from abstract_class.personage import Personage

class Vampire(Personage):

    def __init__(self, name, weapon, weapon_damage, point, health= 130, amount_points= 0):
        super().__init__(name, weapon, weapon_damage, point, health, amount_points)
        
    def __str__(self):
        return  f"""
                {self.name} is a Vampire
                Weapon: {self.weapon}
                Current Health: {self.health}
"""
    
    def attack_left_arm(self, enemy):
        enemy.health -= 11
        self.scoring(self.point)

    def attack_right_arm(self, enemy):
        enemy.health -= 12
        self.scoring((self.point)*3)

    def attack_left_leg(self, enemy):
        enemy.health -= 14
        self.scoring(self.point)

    def attack_right_leg(self, enemy):
        enemy.health -= 15
        self.scoring((self.point)*2)
    
    def attack_weapons(self, enemy):
        enemy.health -= self.weapon_damage
        self.scoring(self.point)
    
    def drink_blood(self):
        self.health += 4 
    

        
    


    
    