from abstract_class.personage import Personage

class Vampire(Personage):

    def __init__(self, name, weapon, weapon_damage, damage, point, health= 130, amount_points= 0):
        super().__init__(name, weapon, weapon_damage, damage, point, health, amount_points)
        
    def __str__(self):
        return  f"""
                {self.name} is a Vampire
                Weapon: {self.weapon}
                Current Health: {self.health}
"""
    
    def attack_left_arm(self, enemy):
        super().attack_left_arm(enemy)
        self.scoring(self.point)

    def attack_right_arm(self, enemy):
        super().attack_right_arm(enemy)
        self.scoring((self.point)*3)

    def attack_left_leg(self, enemy):
        super().attack_left_leg(enemy)
        self.scoring(self.point)

    def attack_right_leg(self, enemy):
        super().attack_right_leg(enemy)
        self.scoring((self.point)*2)
    
    def attack_weapons(self, enemy):
        super().attack_weapons(enemy)
        self.scoring(self.point)
    
    def defend(self):
        self.health += 4 
        self.print_defend_vampire()
    

        
    


    
    