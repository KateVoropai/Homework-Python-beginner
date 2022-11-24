def find_secret_number(secret, guess, hint):
    for i in range(len(secret)):
        if int(secret[i]) == int(guess[i]):
            hint['A'] += 1
        else:
            hint['B'] += 1
    return f"{hint['A']}A{hint['B']}B"
    
secret_number = input("Введите секретное число ")
guess_number = input("Введите предпологаемое число ")
bulls_and_cows = ['A', 'B']
hint = dict.fromkeys(bulls_and_cows, 0)
print(find_secret_number(secret_number, guess_number, hint))