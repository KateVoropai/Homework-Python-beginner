def duplicate_element(some_list):
    duplicate = []
    for i in some_list:
        if some_list.count(i) > 1 and i not in duplicate:
            duplicate.append(i)
    return duplicate
            
def duplicate_element_opt(some_list):
    some_list.sort()
    for i in range(0,len(some_list)-1):
        if some_list[i] == some_list[i+1]:
            return some_list[i]
        
entered_list = input("Введите список чисел: ").split()
my_list = [int(i) for i in entered_list]
print(duplicate_element(my_list))
print(duplicate_element_opt(my_list))
