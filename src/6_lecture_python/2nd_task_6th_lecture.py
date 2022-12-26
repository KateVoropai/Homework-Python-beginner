def delete_duplicate(my_list: list[int]) -> list[int]:
    without_duplicate = {}
    for i in my_list:
        without_duplicate[i] = i
    
    return [i for i in without_duplicate.keys()]
           
entered_list = input("Введите список чисел: ").split()
my_list = [int(i) for i in entered_list]
print(delete_duplicate(my_list))