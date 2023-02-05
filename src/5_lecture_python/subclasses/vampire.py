from abstract_class.personage import Personage

class Vampire(Personage):

    def __init__(self, name, weapon_name, weapon_damage, regeneration = 5 ):
        super().__init__(name, weapon_name, weapon_damage, health = 170)
        self.regeneration = regeneration

    def __str__(self):
        return  f"{self.name} is a Vampire" \
                f"Weapon: {self.weapon_name}" \
                f"Current Health: {self._health}" 

    def drink_blood(self, regeneration):
        self._health += regeneration

    


    
    