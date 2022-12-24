def bubble_sort(my_list: list[int]) -> list[int]:
    for i in range(len(my_list)):
        for j in range(len(my_list) - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list        
        

def merge_sort(my_list: list[int]) -> list[int]:
    if len(my_list) <= 1:
        return my_list
    middle = len(my_list)//2
    left = merge_sort(my_list[:middle])
    right = merge_sort(my_list[middle:])
    return merge_list(left, right)
    
def merge_list(left: list[int], right: list[int]) -> list[int]:
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    if i < len(left):
        sorted_list += left[i:]
    if j < len(right):
        sorted_list += right[j:]
    return sorted_list

entered_list = input("Введите список чисел: ").split()
my_list = [int(i) for i in entered_list]
print(bubble_sort(my_list))
print(merge_sort(my_list))