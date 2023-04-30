from abstract_class.personage import Personage

class Vampire(Personage):

    def __init__(self, name, weapon, weapon_damage, health= 130):
        super().__init__(name, weapon, weapon_damage, health)
        
    def __str__(self):
        return  f"""
                {self.name} is a Vampire
                Weapon: {self.weapon}
                Current Health: {self.health}
"""
    
    def attack_left_arm(self, enemy):
        enemy.health -= 11

    def attack_right_arm(self, enemy):
        enemy.health -= 12

    def attack_left_leg(self, enemy):
        enemy.health -= 14

    def attack_right_leg(self, enemy):
        enemy.health -= 15
    
    def attack_weapons(self, enemy):
        enemy.health -= self.weapon_damage
    
    def drink_blood(self):
        self.health += 4 
    

        
    


    
    