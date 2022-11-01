def modified_tuple(some_tuple):
    some_list = []
    for num in some_tuple:
            if num % 2 == 0:
                some_list.append(num * 2)
            else:
                some_list.append(2)
    return tuple(some_list)
                

entered_list = input("Введите список чисел: ").split()
my_list = [int(i) for i in entered_list]
print(modified_tuple(tuple(my_list)))