# 1 решение
def index_of_nums(some_list):
    for i in range(len(some_list)):
        for j in range(len(some_list)):
            if i == j:
                continue
            if target == some_list[i] + some_list[j]:
                return i, j

entered_list = input("Введите список чисел: ").split()
target = int(input())
my_list = [int(i) for i in entered_list]
print(index_of_nums(my_list))


# 2 решение
def index_of_nums(some_list, target):
    d = {}
    for index, value in enumerate(some_list):
            if target - value in d:
                return some_list.index(target - value), index
            d[value] = index

entered_list = input("Введите список чисел: ").split()
target = int(input())
my_list = [int(i) for i in entered_list]
print(index_of_nums(my_list, target))