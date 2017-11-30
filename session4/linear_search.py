numbers = [5, -2, 8, 29, 6, 89, 63]
x = int(input("Enter your number: "))
found = False
found_index = -1
#find_first, find_one
for index, num in enumerate(numbers):
    if num == x:
        found_index = index
        found = True
        break


if found == False:
    print("Not found")
else:
    print("Found {0} at index {1}".format(x, index))
