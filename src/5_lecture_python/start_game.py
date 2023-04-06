from random import randint
from units.vampires.baron_blood import BaronBlood
from units.vampires.morbius import Morbius
from units.mutants.hulk import Hulk
from units.mutants.magnus import Magnus
from units.super_heroes.captain_america import CaptainAmerica
from units.super_heroes.iron_man import IronMan
from units.transformers.bumblbee import Bumblebee
from units.transformers.megatron import Megatron


def battle(first_fighter, second_fighter):

    print("Начинается бой между")
    print(first_fighter.__str__())
    print(second_fighter.__str__())

    while first_fighter._health > 0 and second_fighter._health > 0:
        n = randint(1, 2)
        if n == 1:
            first_fighter.attack_weapons(second_fighter)
            print_results(first_fighter, second_fighter)
        else:
            second_fighter.attack_weapons(first_fighter)  
            print_results(first_fighter, second_fighter)
    if first_fighter._health > second_fighter._health:
        print(f"{first_fighter.name} победил!")
    elif second_fighter._health > first_fighter._health:
        print(f"{second_fighter.name} победил!")

def print_results(first_fighter, second_fighter):
    print(f"{first_fighter.name} наносит удар {second_fighter.weapon}")
    print(f"{first_fighter.name}: {first_fighter._health} здоровья")
    print(f"{second_fighter.name}: {second_fighter._health} здоровья")

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

input_first_player_choice = input("Введите цифру первого игрока (Hulk - 1, Magnus -2,  Baron_Blood - 3, Morbius - 4, Captain_America - 5, Iron_Man - 6, Bumblebee - 7, Megatron - 8): ")
input_second_player_choice = input("Введите цифру второго игрока (Hulk - 1, Magnus -2,  Baron_Blood - 3, Morbius - 4, Captain_America - 5, Iron_Man - 6, Bumblebee - 7, Megatron - 8): ")

try:
    first_fighter = list_heroes.get(input_first_player_choice)()
    second_fighter = list_heroes.get(input_second_player_choice)()
except:
    print("Ошибка ввода")
    input_first_player_choice = input("Введите цифру первого игрока (Hulk - 1, Magnus -2,  Baron_Blood - 3, Morbius - 4, Captain_America - 5, Iron_Man - 6, Bumblebee - 7, Megatron - 8): ")
    input_second_player_choice = input("Введите цифру второго игрока (Hulk - 1, Magnus -2,  Baron_Blood - 3, Morbius - 4, Captain_America - 5, Iron_Man - 6, Bumblebee - 7, Megatron - 8): ")

first_fighter, second_fighter = list_heroes.get(input_first_player_choice)(), list_heroes.get(input_second_player_choice)()


if __name__ == '__main__':
    
    battle(first_fighter, second_fighter)