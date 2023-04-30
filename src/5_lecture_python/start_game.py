from random import randint, choice
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

def check_input_players(input_player_choice):
    flag = True
    while flag == True:
        if input_player_choice.isdigit() and 0 < int(input_player_choice) < 9: 
            fighter = input_player_choice
            flag = False
        else:
            input_player_choice = input("Ошибка ввода! Введите соответствующую цифру для игрока: ")     
    return  fighter

def action_defender(defender):
    defend_fighter = {
        'Captain America': 'defend', 
        'Iron Man': 'defend', 
        'Hulk': 'regenerate', 
        'Magnus': 'regenerate', 
        'Megatron': 'repair', 
        'Bumblebee': 'repair', 
        'Baron Blood': 'drink_blood',
        'Morbius': 'drink_blood'
    }
    return getattr(defender, defend_fighter.get(defender.name))()

def who_winner(first_fighter, second_fighter):
    if first_fighter.health > second_fighter.health:
        return f"{first_fighter.name} победил!"
    elif second_fighter.health > first_fighter.health:
        return f"{second_fighter.name} победил!"
    
def print_result(attacker, defender):
    attack_fighter = choice(['attack_weapons', 'attack_left_arm', 'attack_right_arm', 'attack_left_leg', 'attack_right_leg'])
    print(*getattr(attacker, 'print_info_attack')(defender, attack_fighter), sep= '\n')
    return attack_fighter

def action_attacker(attacker, defender):
    return getattr(attacker, print_result(attacker, defender))(defender)
    
def main(first_fighter, second_fighter):

    print("Начинается бой между:")
    print(first_fighter.__str__())
    print(second_fighter.__str__())

    attacker = choice([first_fighter, second_fighter])
    if attacker is first_fighter:
        defender = second_fighter
    else:
        defender = first_fighter

    print(f"{attacker.name} атакует первым!")
    
    while first_fighter.health > 0 and second_fighter.health > 0 and True:
        
        action = randint(1, 30)
        if defender.health > 0:
            if action < 15:
                action_attacker(attacker, defender)
            elif action > 15:
                print(f"{defender.name} уклоняется от удара!")
                action_defender(defender)
        else:
            False

        if defender.health > 0 and True:
            attacker, defender = defender, attacker
            print(f"Атакует {attacker.name}!")

    print(who_winner(first_fighter, second_fighter))


if __name__ == '__main__':
    first_fighter = list_heroes.get(check_input_players(input("Введите цифру для первого игрока: ")))()
    second_fighter = list_heroes.get(check_input_players(input("Введите цифру для второго игрока: ")))()

    main(first_fighter, second_fighter)