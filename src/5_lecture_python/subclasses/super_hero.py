from abstract_class.personage import Personage

class SuperHero(Personage):
    
    def __init__(self, name, weapon, weapon_damage, armor_name, defense, health= 120):
        super().__init__(name, weapon, weapon_damage, health)
        self.armor_name = armor_name
        self.defense = defense

    def __str__(self):
        return  f"""
                {self.name} is a SuperHero
                Weapon: {self.weapon}
                Current Health: {self.health}
                Armor: {self.armor_name}
"""
    def attack_left_arm(self, enemy):
        enemy.health -= 12
        
    def attack_right_arm(self, enemy):
        enemy.health -= 18

    def attack_left_leg(self, enemy):
        enemy.health -= 13

    def attack_right_leg(self, enemy):
        enemy.health -= 17 

    def attack_weapons(self, enemy):
        enemy.health -= self.weapon_damage
    
    def defend(self):
        self.health += self.defense
    


        

    

    