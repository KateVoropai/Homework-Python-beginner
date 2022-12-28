def string_permutations(lst: list[str], i: int) -> str: 
    if i == len(my_string): 
        print(''.join(lst))
    else: 
        for j in range(i, len(my_string)): 
            lst[i], lst[j] = lst[j], lst[i] 
            string_permutations(lst, i+1) 
            lst[i], lst[j] = lst[j], lst[i]  
    return ''
  
my_string = input()
lst = list(my_string) 
i = 0
print(string_permutations(lst, i))