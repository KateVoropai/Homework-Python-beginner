def sorted_nums(some_nums):
    new_nums = []
    for num in some_nums:
        if num <= 9:
            new_nums.append(num)
    return new_nums
def target(new_nums):
    for num in new_nums:
        a = 9 - num
        if new_nums.count(a) > 1:
            ind = [i for i, num in enumerate(nums) if num == a]
            return ind
    else:
        if a in new_nums:
            index_of_a = nums.index(a) 
            index_of_num = nums.index(num)
    return index_of_a, index_of_num       
nums = [2, 7, 11, 15]
new_nums = sorted_nums(nums)
print(target(new_nums))