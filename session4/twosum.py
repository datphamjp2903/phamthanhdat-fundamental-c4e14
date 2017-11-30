nums = [-7, -6, -1, 0, 7, 1, 5, 9] #ung_dung_tron_mau
#linear_search

for i in range(0, len(nums) -1):
    numx = nums[i]
    numz = 0
    found = False
    for j in range(i+1, len(nums)):
        if numx + nums[j] == 0:
            numz = nums[j]
            found = True
            break

    if found:
        print("Found {0} and {1}".format(numx, numz))
