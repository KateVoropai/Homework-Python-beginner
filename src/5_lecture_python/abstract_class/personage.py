from abc import ABC, abstractmethod

class Personage(ABC):
    def __init__(self, name, weapon, weapon_damage, health):
        self.name = name
        self.weapon = weapon
        self.weapon_damage = weapon_damage
        self._health = health

    @abstractmethod        
    def __str__(self):
        pass

    @abstractmethod
    def attack_left_arm(self, enemy):
        pass 

    @abstractmethod
    def attack_right_arm(self, enemy):
        pass 

    @abstractmethod
    def attack_left_leg(self, enemy):
        pass 

    @abstractmethod
    def attack_right_leg(self, enemy):
        pass 

    @abstractmethod
    def attack_weapons(self, enemy):
        pass