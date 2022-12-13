def input_numbers():
    val = True
    while val:
        secret_number = input("Введите секретное число ")
        guess_number = input("Введите предполагаемое число ")
        if len(guess_number) != len(secret_number):
            print('Please, input correct data.')
        else:
            val = False
    return secret_number, guess_number

def find_secret_number(secret, guess, A = 0, B = 0):
    for i in range(len(guess)):
        if secret[i] == guess[i]:
            A += 1
        if guess[i] in secret and secret[i] != guess[i]:
            B += 1
    return f"{A}A{B}B"
    

secret_number, guess_number = input_numbers()
print(find_secret_number(secret_number, guess_number))
