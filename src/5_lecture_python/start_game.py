from random import randint
from units.vampires.baron_blood import BaronBlood
from units.vampires.morbius import Morbius
from units.mutants.hulk import Hulk
from units.mutants.magnus import Magnus
from units.super_heroes.captain_america import CaptainAmerica
from units.super_heroes.iron_man import IronMan
from units.transformers.bumblbee import Bumblebee
from units.transformers.megatron import Megatron

list_heroes = {
            '1': Hulk,
            '2': Magnus,
            '3': BaronBlood,
            '4': Morbius,
            '5': CaptainAmerica,
            '6': IronMan,
            '7': Bumblebee,
            '8': Megatron
} 

for kye, value in list_heroes.items():
    heroes = list_heroes.get(kye)()
    name_heroes = heroes.name
    print(kye, name_heroes)

input_first_player_choice = input("Введите цифру для первого игрока: ")
input_second_player_choice = input("Введите цифру для второго игрока: ")

try:
    first_fighter = list_heroes.get(input_first_player_choice)()
except:
    print("Ошибка ввода")
    input_first_player_choice = input("Введите цифру для первого игрока: ")

try:
    second_fighter = list_heroes.get(input_second_player_choice)()
except:
    print("Ошибка ввода")
    input_second_player_choice = input("Введите цифру для второго игрока: ")

first_fighter, second_fighter = list_heroes.get(input_first_player_choice)(), list_heroes.get(input_second_player_choice)()


def battle(first_fighter, second_fighter):

    print("Начинается бой между:")
    print(first_fighter.__str__())
    print(second_fighter.__str__())

    attacker = None
    defender = None

    n = randint(1, 2)
    if n == 1:
        attacker = first_fighter
        defender = second_fighter
    else:
        attacker = second_fighter
        defender = first_fighter

    print(f"{attacker.name} атакует первым!")
    
    stop = True
    while first_fighter._health > 0 and second_fighter._health > 0 and stop:
    
        action_attacker = input("Чем нанести удар? Оружием - 1, Левой/Правой рукой - 2/3, Левой/Правой ногой -4/5: ")
        if action_attacker not in '12345' or not action_attacker.isdigit:
            print("Ошибка ввода! Введите правильную цифру!")
            action_attacker = input("Чем нанести удар? Оружием - 1, Левой/Правой рукой - 2/3, Левой/Правой ногой -4/5: ")

        action_defender = randint(1, 30)
        if action_defender > 15:
            if action_attacker == '1':
                attacker.attack_weapons(defender)
                print_results(attacker, defender, action_attacker)
            elif action_attacker == '2':
                attacker.attack_left_arm(defender)
                print_results(attacker, defender, action_attacker)
            elif action_attacker == '3':
                attacker.attack_right_arm(defender)
                print_results(attacker, defender, action_attacker)
            elif action_attacker == '4':
                attacker.attack_left_leg(defender)
                print_results(attacker, defender, action_attacker)
            elif action_attacker == '5':
                attacker.attack_right_leg(defender)
                print_results(attacker, defender, action_attacker)
            
            if defender._health > 0:
                answer = input("Продолжать бой? (да/нет): ")
                if answer != 'да' and answer != 'нет':
                    print("Введите правильный ответ!")
                    answer = input("Продолжать бой? (да/нет): ")
                if answer == 'нет':
                    stop = False
        
        if action_defender <= 15:
            print(f"{defender.name} уклоняется от удара!")
            if (isinstance(defender, CaptainAmerica) or isinstance(defender, IronMan)) and defender._health < 100:
                defender.defend()
            elif (isinstance(defender, Hulk) or isinstance(defender, Magnus)) and defender._health < 90:
                defender.regenerate()
            elif (isinstance(defender, Bumblebee) or isinstance(defender, Megatron)) and defender._health < 100:
                defender.repair()
            elif (isinstance(defender, BaronBlood) or isinstance(defender, Morbius)) and defender._health < 110:
                defender.drink_blood()
        
        if attacker._health > 0 and stop:
            attacker, defender = defender, attacker
            print(f"Атакует {attacker.name}!")

    if first_fighter._health > second_fighter._health:
        print(f"{first_fighter.name} победил!")
    elif second_fighter._health > first_fighter._health:
        print(f"{second_fighter.name} победил!")

def print_results(attacker, defender, action_attacker):
    if action_attacker == '1':
        print(f"{attacker.name} наносит удар сопернику с помощью {attacker.weapon}!")
        print(f"{defender.name}: текущее здоровье {defender._health}")
    if action_attacker == '2':
        print(f"{attacker.name} наносит удар левой рукой!")
        print(f"{defender.name}: текущее здоровье {defender._health}")
    if action_attacker == '3':
        print(f"{attacker.name} наносит удар правой рукой!")
        print(f"{defender.name}: текущее здоровье {defender._health}")
    if action_attacker == '4':
        print(f"{attacker.name} наносит удар левой ногой!")
        print(f"{defender.name}: текущее здоровье {defender._health}")
    if action_attacker == '5':
        print(f"{attacker.name} наносит удар правой ногой!")
        print(f"{defender.name}: текущее здоровье {defender._health}")

if __name__ == '__main__':
    battle(first_fighter, second_fighter)