from abstract_class.personage import Personage

class SuperHero(Personage):
    
    def __init__(self, name, weapon, weapon_damage, armor_name, defense):
        super().__init__(name, weapon, weapon_damage, health= 170)
        self.armor_name = armor_name
        self.defense = defense

    def __str__(self):
        return  f"""
                {self.name} is a SuperHero
                Weapon: {self.weapon}
                Current Health: {self._health}
                Armor: {self.armor_name}
"""

    def attack_left_arm(self, enemy):
        enemy.health -= 2

    def attack_right_arm(self, enemy):
        enemy.health -= 2

    def attack_left_leg(self, enemy):
        enemy.health -= 3

    def attack_right_leg(self, enemy):
        enemy.health -= 3 

    def attack_weapons(self, enemy):
        enemy._health -= self.weapon_damage
    

    def defend(self):
        self._health += self.defense
        print(f"{self.name} защищается от удара с помощью {self.armor_name}")
        

    

    