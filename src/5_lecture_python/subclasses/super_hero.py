from abstract_class.personage import Personage

class SuperHero(Personage):
    
    def __init__(self, name, weapon, weapon_damage, armor_name, defense, point, health= 120, amount_points= 0):
        super().__init__(name, weapon, weapon_damage, point, health, amount_points)
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
        self.scoring(self.point)
        
    def attack_right_arm(self, enemy):
        enemy.health -= 18
        self.scoring((self.point)*3)

    def attack_left_leg(self, enemy):
        enemy.health -= 13
        self.scoring(self.point)

    def attack_right_leg(self, enemy):
        enemy.health -= 17 
        self.scoring(self.point)

    def attack_weapons(self, enemy):
        enemy.health -= self.weapon_damage
        self.scoring((self.point)*2)

    def armor_defend(self):
        self.health += self.defense


        

    

    