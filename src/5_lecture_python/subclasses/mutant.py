from abstract_class.personage import Personage

class Mutant(Personage):

    def __init__(self, name, weapon_name, weapon_damage, regeneration = 15):
        super().__init__(name, weapon_name, weapon_damage, health = 150)
        self.regeneration = regeneration

    def __str__(self):
        return  f"{self.name} is a Mutant" \
                f"Weapon: {self.weapon_name}" \
                f"Current Health: {self._health}" 
        

    def _take_damage(self, damage, regeneration):
        total_damage = damage - regeneration
        self._health -= total_damage






