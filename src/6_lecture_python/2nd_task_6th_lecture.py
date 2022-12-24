def delete_duplicate(my_list: list[int]) -> list[int]:
    list_without_duplicate = list(set(my_list))
    return list_without_duplicate 
           
entered_list = input("Введите список чисел: ").split()
my_list = [int(i) for i in entered_list]
print(delete_duplicate(my_list))