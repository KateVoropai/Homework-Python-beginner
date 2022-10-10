def xor(some_list):
    maxi_xor = 0
    for i in range((len(my_list)) - 1):
        new_list = my_list[i + 1:]
        for j in new_list:
            a = j ^ my_list[i]
            maxi_xor = max(a, maxi_xor)
    return maxi_xor

my_list = [3, 10, 5, 25, 2, 8]
print(xor(my_list))