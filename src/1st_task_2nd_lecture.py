def modified_tuple(some_tuple):
    some_list = []
    for num in some_tuple:
            if num % 2 == 0:
                some_list.append(num * 2)
            else:
                some_list.append(num - 2)
    return tuple(some_list)

def modified_tuple_2(some_tuple):      #2 вариант решения, без создания some_list=[] 
    for num in range(len(some_tuple)):
        if some_tuple[num] % 2 == 0:
            some_tuple[num] = some_tuple[num] * 2
        else:
            some_tuple[num] = some_tuple[num] - 2
    return tuple(some_tuple)

entered_list = input("Введите список чисел: ").split()
my_list = [int(i) for i in entered_list]
print(modified_tuple(tuple(my_list)))
print(modified_tuple_2(my_list))