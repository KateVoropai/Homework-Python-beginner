def permutation_string(lst, i):
    if i == len(lst):
        return ''
    else:
        for j in range(len(lst)):
            if i == j:
                continue
            lst[i], lst[j] = lst[j], lst[i]
            print(*lst)
    return permutation_string(lst, i + 1)

my_string = '123'
lst = list(my_string)
i = 0
print(permutation_string(lst, i))
