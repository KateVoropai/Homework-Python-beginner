def prime_numbers(num):
    for i in range(3, (int(num**0.5)+1)):
        if num % i == 0:
            return False
    return True
        
def find_prime_numbers(my_list):
    list_prime_numbers = [2]   #первое простое число
    for num in my_list[2::2]:
        if prime_numbers(num) == True:
            list_prime_numbers.append(num)
    return list_prime_numbers
    

my_list = [i for i in range(1, 100001)]
print(find_prime_numbers(my_list))