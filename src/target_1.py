nums = [2, 7, 11, 15]
for num in nums:
    index_of_num = nums.index(num)
    for i in range(len(nums)):
        if i == index_of_num:
            continue
        elif num + nums[i] == 9:
            a = i
            b = index_of_num
print(a, b)


