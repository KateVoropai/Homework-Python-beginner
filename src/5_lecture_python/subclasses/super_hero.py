from abstract_class.personage import Personage

class SuperHero(Personage):
    
    def __init__(self, name, weapon_name, weapon_damage, armor_name, defense = 15):
        super().__init__(name, weapon_name, weapon_damage, health = 170)
        self.armor_name = armor_name
        self.defense = defense

    def __str__(self):
        return  f"{self.name} is a SuperHero" \
                f"Weapon: {self.weapon_name}" \
                f"Current Health: {self._health}" \
                f"Armor: {self.armor_name}"

    def _take_damage(self, damage, defense):
        total_damage = damage - defense
        self._health -= total_damage



    

    