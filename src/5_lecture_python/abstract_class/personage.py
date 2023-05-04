from abc import ABC, abstractmethod

class Personage(ABC):
    def __init__(self, name, weapon, weapon_damage, health, point, amount_points):
        self.name = name
        self.weapon = weapon
        self.weapon_damage = weapon_damage
        self._health = health
        self._point = point
        self.amount_points = amount_points


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
                'attack_left_arm':  f"{self.name} наносит удар левой рукой!" '\n'
                                    f"{fighter.name}: здоровье {fighter.health}",

                'attack_right_arm': f"{self.name} наносит удар правой рукой!" '\n'
                                    f"{fighter.name}: здоровье {fighter.health}",

                'attack_left_leg': f"{self.name} наносит удар левой ногой!" '\n'
                            f"{fighter.name}: здоровье {fighter.health}",

                'attack_right_leg': f"{self.name} наносит удар правой ногой!" '\n'
                            f"{fighter.name}: здоровье {fighter.health}",

                'attack_weapons': f"{self.name} наносит удар с помощью {self.weapon}!" '\n'
                            f"{fighter.name}: здоровье {fighter.health}"
                }
        return print_attack.get(name_attack)
    
    def print_info_defend(self, name_attack):
        print_defend = {
                'regenerate': f"{self.name} запустил процесс регенерации! Здоровье: {self.health}",
                'repair': f"{self.name} починил себя! Здоровье: {self.health}",
                'drink_blood': f"{self.name} пьет кровь! Здоровье: {self.health}",
                'armor_defend': f"{self.name} защищается с помощью брони! Здоровье: {self.health}"
                }
        return print_defend.get(name_attack)
    
    def print_info_super_ability(self, fighter):
        print_super_ability = {
                'Captain America': f"{self.name} бьёт молнией {fighter.name}!" '\n'
                                f"{fighter.name}: здоровье {fighter.health}", 

                'Iron Man': f"{self.name} бросает гранату в {fighter.name}!" '\n'
                                f"{fighter.name}: здоровье {fighter.health}",

                'Hulk': f"{self.name} загипнотизировал {fighter.name}!" '\n'
                        f"{fighter.name}: здоровье {fighter.health}",

                'Magnus': f"{self.name} кусает за нос {fighter.name}!" '\n'
                        f"{fighter.name}: здоровье {fighter.health}",

                'Megatron': f"{self.name} бросается подшипкиками в {fighter.name}!" '\n'
                            f"{fighter.name}: здоровье {fighter.health}",

                'Bumblebee': f"{self.name} плюется моторным маслом в {fighter.name}!" '\n'
                            f"{fighter.name}: здоровье {fighter.health}",

                'Baron Blood': f"{self.name} кусает за пятку {fighter.name}!" '\n'
                            f"{fighter.name}: здоровье {fighter.health}",

                'Morbius': f"{self.name} бьёт в левый глаз {fighter.name}!" '\n'
                            f"{fighter.name}: здоровье {fighter.health}"
                }
        return print_super_ability.get(self.name)
    
    @property
    def point(self):
        return self._point
    
    @point.setter
    def point(self, point):
        self._point = point
    
    def scoring(self, point):
        self.amount_points += point
    

    def super_ability(self, enemy):
        pass