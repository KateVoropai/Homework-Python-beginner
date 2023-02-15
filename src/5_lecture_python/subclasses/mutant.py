from abstract_class.personage import Personage

class Mutant(Personage):

    def __init__(self, name, weapon_name, weapon_damage):
        super().__init__(name, weapon_name, weapon_damage, health=150)
        self.hand_strike = 5
    
    def __str__(self):
        return  f"""
                {self.name} is a Mutant
                Weapon: {self.weapon_name}
                Current Health: {self._health}
"""

    def attack(self, enemy):
        enemy._take_damage(self.weapon_damage)
        print(f"{self.name} strikes {enemy.name} with {self.weapon_name}!")
        
        enemy._take_damage(self.hand_strike)
        print(f"{self.name} strikes with his hand")
    







