from abstract_class.personage import Personage

class Transformer(Personage):
    
    def __init__(self, name, weapon_name, weapon_damage, living_metal=15):
        super().__init__(name, weapon_name, weapon_damage, health=160)
        self.living_metal = living_metal

    def __str__(self):
        return  f"""
                {self.name} is a Transformer
                Weapon: {self.weapon_name}
                Current Health: {self._health}
"""

    
    def attack(self):
        pass 

    