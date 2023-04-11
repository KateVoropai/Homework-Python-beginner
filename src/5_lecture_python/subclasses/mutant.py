from abstract_class.personage import Personage

class Mutant(Personage):

    def __init__(self, name, weapon, weapon_damage, health= 150):
        super().__init__(name, weapon, weapon_damage, health)
    
    def __str__(self):
        return  f"""
                {self.name} is a Mutant
                Weapon: {self.weapon}
                Current Health: {self._health}
"""
    def attack_left_arm(self, enemy):
        enemy._health -= 11

    def attack_right_arm(self, enemy):
        enemy._health -= 15
    
    def attack_left_leg(self, enemy):
        enemy._health -= 13

    def attack_right_leg(self, enemy):
        enemy._health -= 17

    def attack_weapons(self, enemy):
        enemy._health -= self.weapon_damage

    def regenerate(self):
        self._health += 4
        print(f"{self.name} запустил процесс регенерации!")
        print(f"{self.name}: {self._health} здоровья")
        






