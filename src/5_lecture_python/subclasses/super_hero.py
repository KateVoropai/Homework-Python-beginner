from abstract_class.personage import Personage

class SuperHero(Personage):
    
    def __init__(self, name, weapon, weapon_damage, damage, health, point, armor_name, defense, amount_points= 0):
        super().__init__(name, weapon, weapon_damage, damage, health, point, amount_points)
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
        self.scoring(self.point)

    def attack_weapons(self, enemy):
        super().attack_weapons(enemy)
        self.scoring((self.point)*2)

    def defend(self):
        self.health += self.defense
        self.print_defend_super_hero()

