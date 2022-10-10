my_list = [3, 10, 5, 25, 2, 8]
a = 0
for num in my_list:
    for i in range(len(my_list)):
        s = num ^ my_list[i]
        if s > a:
            s, a = a, s
print(a)





