from abstract_class.personage import Personage

class SuperHero(Personage):
    
    def __init__(self, name, weapon_name, weapon_damage, armor_name, defense=15):
        super().__init__(name, weapon_name, weapon_damage, health=170)
        self.armor_name = armor_name
        self.defense = defense

    def __str__(self):
        return  f"""
                {self.name} is a SuperHero
                Weapon: {self.weapon_name}
                Current Health: {self._health}
                Armor: {self.armor_name}
"""

    def attack(self):
        pass 


    

    