nums = [1, 3, 4, 2, 2]
counter = 0
for num in nums:
    nums_count = nums. count(num)
    if nums_count == 2:
        r_element = num
        nums.remove(num)
        counter += 1
if counter == 1:
    print(r_element)
else:
    print('Повторяющийся элемент не единтсвенный, либо повторений нет')



