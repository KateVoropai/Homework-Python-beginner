def delete_duplicate(my_list: list[int]) -> set[int]:
    list_without_duplicate = set()
    for i in my_list:
        list_without_duplicate.add(i)

    return list_without_duplicate 

           
entered_list = input("Введите список чисел: ").split()
my_list = [int(i) for i in entered_list]
print(delete_duplicate(my_list))
