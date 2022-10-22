# 1 решение
def maxi_xor(some_list):
    max_xor = 0
    for i in my_list:
        for j in my_list:
            xor = i ^ j
            if max_xor < xor:
                max_xor = xor
    return max_xor

entered_list = input("Введите список чисел: ").split()
my_list = [int(i) for i in entered_list]
print(maxi_xor(my_list))


# 2 решение
def maxi_xor(some_list):
    maxi_num = max(some_list)
    maxi_xor = 0
    for i in some_list:
        xor = i ^ maxi_num
        if maxi_xor < xor:
            maxi_xor = xor
    return maxi_xor

entered_list = input("Введите список чисел: ").split()
my_list = [int(i) for i in entered_list]
print(maxi_xor(my_list))





