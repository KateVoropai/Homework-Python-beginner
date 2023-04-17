from abstract_class.personage import Personage

class SuperHero(Personage):
    
    def __init__(self, name, weapon, weapon_damage, armor_name, defense, health= 160):
        super().__init__(name, weapon, weapon_damage, health)
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
        enemy._health -= 12

    def attack_right_arm(self, enemy):
        enemy._health -= 18

    def attack_left_leg(self, enemy):
        enemy._health -= 13

    def attack_right_leg(self, enemy):
        enemy._health -= 17 

    def attack_weapons(self, enemy):
        enemy._health -= self.weapon_damage
    
    def defend(self):
        self._health += self.defense
        print(f"И защищается с помощью {self.armor_name}! Текущее здоровье {self._health}")


        

    

    