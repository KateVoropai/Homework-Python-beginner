def permutation_string(string: str, permutation = '') -> str:
    if len(string) == 0:
        print(permutation)
        
    for i in range(len(string)):
        new_permutation = permutation + string[i]
        new_string = string[:i] + string[i+1:]
        permutation_string(new_string, new_permutation)
    
    return ''
    
string = input()
print(permutation_string(string))