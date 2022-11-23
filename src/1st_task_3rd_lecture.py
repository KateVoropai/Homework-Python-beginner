def find_prime_numbers(my_list):
    prime_numbers = [2]   #первое простое число
    for num in my_list[2::2]:
        flag = True
        for i in range(3, num, 2):
            if num % i == 0:
                flag = False
                break
        if flag == True:
            prime_numbers.append(num)
    return prime_numbers
    

my_list = [i for i in range(1, 100001)]
print(find_prime_numbers(my_list))