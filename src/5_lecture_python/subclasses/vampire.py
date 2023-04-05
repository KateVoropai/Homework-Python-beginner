from abstract_class.personage import Personage

class Vampire(Personage):

    def __init__(self, name, weapon, weapon_damage, health= 170):
        super().__init__(name, weapon, weapon_damage, health)
        

    def __str__(self):
        return  f"""
                {self.name} is a Vampire
                Weapon: {self.weapon}
                Current Health: {self._health}
"""
    
    def attack_left_arm(self, enemy):
        enemy._health -= 1
        print(f"{self.name} наносит удар левой рукой")

    def attack_right_arm(self, enemy):
        enemy._health -= 1
        print(f"{self.name} наносит удар правой рукой")

    def attack_left_leg(self, enemy):
        enemy._health -= 2
        print(f"{self.name} наносит удар левой ногой")

    def attack_right_leg(self, enemy):
        enemy._health -= 2
        print(f"{self.name} наносит удар правой ногой")
    
    def attack_weapons(self, enemy):
        enemy._health -= self.weapon_damage
        #print(f"{self.name} наносит удар {self.weapon}")

    def drink_blood(self):
        self._health += 5    
        
    


    
    