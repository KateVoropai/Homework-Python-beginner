from abstract_class.personage import Personage

class Vampire(Personage):

    def __init__(self, name, weapon_name, weapon_damage):
        super().__init__(name, weapon_name, weapon_damage, health=170)
        self.regeneration = 5
        self.bite = 4

    def __str__(self):
        return  f"{self.name} is a Vampire" \
                f"Weapon: {self.weapon_name}" \
                f"Current Health: {self._health}" 

    def drink_blood(self, regeneration):
        self._health += regeneration
        return self._health
    
    def attack(self, enemy):
        enemy._take_damage(self.weapon_damage)
        print(f"{self.name} strikes {enemy.name} with {self.weapon_name}!")
        
        enemy._take_damage(self.bite)
        print(f"{self.name} bites {enemy.self}!")

    


    
    