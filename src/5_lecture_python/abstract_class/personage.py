from abc import ABC, abstractmethod

class Personage(ABC):
    def __init__(self, name, weapon_name, weapon_damage, health):
        self.name = name
        self.weapon_name = weapon_name 
        self.weapon_damage = weapon_damage
        self._health = health

    @abstractmethod        
    def __str__(self):
        pass 

    @abstractmethod
    def attack(self):
        pass 

    def _take_damage(self, damage):
        self._health -= damage
        return self._health
