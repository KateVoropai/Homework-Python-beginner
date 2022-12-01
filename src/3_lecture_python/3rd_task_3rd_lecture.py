def find_secret_number(secret, guess, A, B):
    guess_nums = []
    secret_nums = []
    for i in range(len(guess)):
        if secret[i] == guess[i]:
            A += 1
        elif secret[i] != guess[i]:
            secret_nums.append(secret[i])
            guess_nums.append(guess[i])
    if len(guess_nums) > 0:
        for j in guess_nums[::-1]:
            if j in secret_nums:
                B += 1
                guess_nums.remove(j)
                secret_nums.remove(j)            
    return f"{A}A{B}B"
    
secret_number = input("Введите секретное число ")
guess_number = input("Введите предполагаемое число ")
A = 0
B = 0
if len(guess_number) < len(secret_number) or len(guess_number) > len(secret_number):
    guess_number = input(f"Секретное число {len(secret_number)} значное, введите равнозначное число ")
print(find_secret_number(list(secret_number), list(guess_number), A, B))