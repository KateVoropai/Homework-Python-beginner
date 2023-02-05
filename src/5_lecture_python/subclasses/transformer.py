from abstract_class.personage import Personage

class Transformer(Personage):
    
    def __init__(self, name, weapon_name, weapon_damage, living_metal = 15):
        super().__init__(name, weapon_name, weapon_damage, health = 160)
        self.living_metal = living_metal

    def __str__(self):
        return  f"{self.name} is a Transformer" \
                f"Weapon: {self.weapon_name}" \
                f"Current Health: {self._health}"

    
    def _take_damage(self, damage, living_metal):
        total_damage = damage - living_metal
        self._health -= total_damage



    