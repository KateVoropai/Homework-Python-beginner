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
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, health):
        self._health = health
    
    def print_info_attack(self, fighter, name_attack):
        print_attack = {
                'attack_left_arm':  [f"{self.name} наносит удар левой рукой!",
                                    f"{fighter.name}: текущее здоровье {fighter.health}"],

                'attack_right_arm': [f"{self.name} наносит удар правой рукой!",
                                    f"{fighter.name}: текущее здоровье {fighter.health}"],

                'attack_left_leg': [f"{self.name} наносит удар левой ногой!",
                            f"{fighter.name}: текущее здоровье {fighter.health}"],

                'attack_right_leg': [f"{self.name} наносит удар правой ногой!",
                            f"{fighter.name}: текущее здоровье {fighter.health}"],

                'attack_weapons': [f"{self.name} наносит удар с помощью {self.weapon}!", 
                            f"{fighter.name}: текущее здоровье {fighter.health}"]
        }
        return print_attack.get(name_attack)
    
    def print_info_defend(self):
        print_defend = {
                'defend': [f"И защищается с помощью {self.armor_name}! Текущее здоровье {self.health}"],
                'regenerate': [f"{self.name} запустил процесс регенерации! Текущее здоровье {self.health}"],
                'repair': [f"{self.name} починил себя! Текущее здоровье {self.health}"],
                'drink_blood': [f"{self.name} пьет кровь! Текущее здоровье {self.health}"]
        }
        return print_defend
    
    # @property
    # def point(self):
    #     return self.__point
    
    # @point.setter
    # def point(self, point):
    #     self.__point = point

    def super_ability(self, enemy):
        pass