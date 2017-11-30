nums = [-99, -23, -10, 0, 12, 29, 63, 77, 108]
x = int(input("Enter a number: "))

found = False
lo = 0
hi = len(nums)

while hi > lo:
    mid = (lo + hi)//2
    num = nums[mid]
    if x == num:
        found = True
        print("Found")
    elif x < num:
        hi = mid
        print("Left")
    else:
        lo = mid + 1 #vi_mid_lam_tron_gan_lo_nen_can_+1
        print(lo, hi)
        print("Right")
if not found:
    print("Not found")
