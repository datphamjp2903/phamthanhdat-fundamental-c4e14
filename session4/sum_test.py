nums = [5, -100, 8, 29, 63, 73]
sum = 0

for index, num in enumerate(nums):
    sum += num
print(sum)
#find_min
min_num = nums[0]

for num in nums:
    if min_num > num:
        min_num = num
print("Min: ", min_num)
