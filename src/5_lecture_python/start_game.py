from random import randint, choice

from units.vampires.baron_blood import baron_blood, dracula
from units.vampires.morbius import morbius, damon
from units.mutants.hulk import hulk, red_hulk
from units.mutants.magnus import magnus, magneto
from units.super_heroes.captain_america import captain_america, tor
from units.super_heroes.iron_man import iron_man, spider_man
from units.transformers.bumblbee import bumblebee, optimus_prime
from units.transformers.megatron import megatron, follen

list_heroes = {
            '1': hulk,
            '2': red_hulk,
            '3': magnus,
            '4': magneto,
            '5': captain_america,
            '6': tor,
            '7': iron_man,
            '8': spider_man,
            '9': bumblebee,
            '10': optimus_prime,
            '11': megatron,
            '12': follen,
            '13': baron_blood,
            '14': dracula,
            '15': morbius,
            '16': damon
} 

for kye, value in list_heroes.items():
    heroes = list_heroes.get(kye)
    name_heroes = heroes.name
    print(kye, name_heroes)

def check_input_players(input_player_choice):
    flag = True
    while flag == True:
        if input_player_choice.isdigit() and 0 < int(input_player_choice) < 17: 
            fighter = input_player_choice
            flag = False
        else:
            input_player_choice = input("Ошибка ввода! Введите соответствующую цифру для игрока: ")     
    return  fighter

def action_defender(defender):
    return getattr(defender, 'defend')()

def action_attacker(attacker, defender):
    attack_fighter = choice(['attack_weapons', 'attack_left_arm', 'attack_right_arm', 'attack_left_leg', 'attack_right_leg'])
    return getattr(attacker, attack_fighter)(defender)

def action_super_ability(attacker, defender):
    return getattr(attacker, 'super_ability')(defender)

def check_winner(first_fighter, second_fighter):
    if first_fighter.health > second_fighter.health:
        return f"{first_fighter.name} победил! Количество очков: {first_fighter.amount_points}"
    
    elif second_fighter.health > first_fighter.health:
        return f"{second_fighter.name} победил! Количество очков: {second_fighter.amount_points}"
    
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

        if action > 15:
            defender.print_defender()
            action_defender(defender)
        elif 1 <= action <= 7:
            action_attacker(attacker, defender)
        elif 7 < action <= 15:
            action_super_ability(attacker, defender)

        if defender.health == 0:
            False
        else:
            attacker, defender = defender, attacker
            attacker.print_attacker()
            
    print(check_winner(first_fighter, second_fighter))


if __name__ == '__main__':
    first_fighter = list_heroes.get(check_input_players(input("Введите цифру для первого игрока: ")))
    second_fighter = list_heroes.get(check_input_players(input("Введите цифру для второго игрока: ")))

    main(first_fighter, second_fighter)