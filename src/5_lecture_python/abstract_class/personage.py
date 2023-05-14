from abc import ABC, abstractmethod
from random import randint

class Personage(ABC):
    def __init__(self, name, weapon, weapon_damage, max_damage, health, point, amount_points):
        self.name = name
        self.weapon = weapon
        self.weapon_damage = weapon_damage
        self.max_damage = max_damage
        self._health = health
        self._point = point
        self.amount_points = amount_points


    @abstractmethod        
    def __str__(self):
        pass

    @abstractmethod
    def attack_left_arm(self, enemy):
        enemy.health -= self.amount_damage()
        if enemy.health < 0:
            enemy.health = 0 
        self.print_attack_left_arm(enemy)
        pass 

    @abstractmethod
    def attack_right_arm(self, enemy):
        enemy.health -= self.amount_damage()
        if enemy.health < 0:
            enemy.health = 0 
        self.print_attack_right_arm(enemy)
        pass 

    @abstractmethod
    def attack_left_leg(self, enemy):
        enemy.health -= self.amount_damage()
        if enemy.health < 0:
            enemy.health = 0 
        self.print_attack_left_leg(enemy)
        pass 

    @abstractmethod
    def attack_right_leg(self, enemy):
        enemy.health -= self.amount_damage()
        if enemy.health < 0:
            enemy.health = 0 
        self.print_attack_right_leg(enemy)
        pass 

    @abstractmethod
    def attack_weapons(self, enemy):
        enemy.health -= self.weapon_damage
        if enemy.health < 0:
            enemy.health = 0 
        self.print_attack_weapons(enemy)
        pass
    
    @abstractmethod
    def defend(self):
        pass

    def amount_damage(self):
        random_value = randint(8, self.max_damage)
        return random_value

    def scoring(self, point):
        self.amount_points += point
    
    def super_ability(self, enemy):
        enemy.health -= self.max_damage
        if enemy.health < 0:
            enemy.health = 0 

    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, health):
        self._health = health

    @property
    def point(self):
        return self._point
    
    @point.setter
    def point(self, point):
        self._point = point
    
    def print_attack_weapons(self, enemy):
        print(f"{self.name} наносит удар сопернику с помощью {self.weapon}!" '\n'
            f"{enemy.name}: здоровье {enemy.health}")
        
    def print_attack_left_arm(self, enemy):
        print(f"{self.name} наносит удар сопернику левой рукой!" '\n'
            f"{enemy.name}: здоровье {enemy.health}")
        
    def print_attack_right_arm(self, enemy):
        print(f"{self.name} наносит удар сопернику правой рукой!" '\n'
            f"{enemy.name}: здоровье {enemy.health}")
    
    def print_attack_left_leg(self, enemy):
        print(f"{self.name} наносит удар сопернику левой ногой!" '\n'
            f"{enemy.name}: здоровье {enemy.health}")
    
    def print_attack_right_leg(self, enemy):
        print(f"{self.name} наносит удар сопернику правой ногой!" '\n'
            f"{enemy.name}: здоровье {enemy.health}")
        
    def print_defenf_mutant(self):
        print(f"{self.name} запустил процесс регенерации! {self.name}: здоровье {self.health}")

    def print_defend_transformer(self):
        print(f"{self.name} трансформировал дополнительную броню! {self.name}: здоровье {self.health}")

    def print_defend_vampire(self):
        print(f"{self.name} пьет кровь! {self.name}: здоровье {self.health}")

    def print_defend_super_hero(self):
        print(f"{self.name} защищается с помощью {self.armor_name}! {self.name}: здоровье {self.health}")  

    def print_ability_hulk(self, fighter):
        print(f"{self.name} загипнотизировал {fighter.name}!" '\n'
            f"{fighter.name}: здоровье {fighter.health}")
    
    def print_ability_magnus(self, fighter):
        print(f"{self.name} кусает за нос {fighter.name}!" '\n'
            f"{fighter.name}: здоровье {fighter.health}")
        
    def print_ability_captain_america(self, fighter):
        print(f"{self.name} бьёт молнией {fighter.name}!" '\n'
            f"{fighter.name}: здоровье {fighter.health}")
        
    def print_ability_iron_man(self, fighter):
        print(f"{self.name} бросает гранату в {fighter.name}!" '\n'
            f"{fighter.name}: здоровье {fighter.health}")
        
    def print_ability_megatron(self, fighter):
        print(f"{self.name} бросается подшипкиками в {fighter.name}!" '\n'
            f"{fighter.name}: здоровье {fighter.health}")
        
    def print_ability_bumblebee(self, fighter):
        print(f"{self.name} плюется моторным маслом в {fighter.name}!" '\n'
            f"{fighter.name}: здоровье {fighter.health}")
    
    def print_ability_baron_blood(self, fighter):
        print(f"{self.name} кусает за пятку {fighter.name}!" '\n'
            f"{fighter.name}: здоровье {fighter.health}")
        
    def print_ability_morbius(self, fighter):
        print(f"{self.name} бьёт в левый глаз {fighter.name}!" '\n'
            f"{fighter.name}: здоровье {fighter.health}")
        
    def print_attacker(self):
        print(f"Атакует {self.name}!")

    def print_defender(self):
        print(f"{self.name} уклоняется от удара!")