def find_element(s):
    duplicates = []
    for i in s:
        if s.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    return duplicates
            
nums = [3, 1, 3, 4, 2]
print(find_element(nums))